"""
Classes and functions for looking up schema classes
based on names, types, IRIs

"""

from urllib.parse import urlparse


registry = {
    'names': {},
    'types': {},
    'paths': {}
}

# todo: add namespaces to avoid name clashes, e.g. "Person" exists in several namespaces


def register_class(target_class):
    if "openminds" in target_class.__module__:
        parts = target_class.__module__.split(".")
        name = ".".join(parts[1:3] + [target_class.__name__])  # e.g. openminds.core.Dataset
    else:
        name = target_class.__module__.split(".")[-1] + "." + target_class.__name__

    registry['names'][name] = target_class
    try:
        registry['paths'][target_class.path] = target_class
    except AttributeError:  # base classes do not have a namespace / path
        pass
    except ValueError:  # core classes do not have a namespace set
        pass            # we may want to register the path when the namespace is set
    if hasattr(target_class, 'type'):
        if isinstance(target_class.type, str):
            type_ = target_class.type
        else:
            type_ = tuple(sorted(target_class.type))
        if type_ in registry['types']:
            if isinstance(registry['types'][type_], list):
                registry['types'][type_].append(target_class)
            else:
                registry['types'][type_] = [registry['types'][type_], target_class]
        else:
            registry['types'][type_] = target_class

    if hasattr(target_class, "previous_types"):
        for prev_type in target_class.previous_types:
            if prev_type in registry['types']:
                if isinstance(registry['types'][prev_type], list):
                    registry['types'][prev_type].append(target_class)
                else:
                    registry['types'][prev_type] = [registry['types'][prev_type], target_class]
            else:
                registry['types'][prev_type] = target_class


def lookup(class_name):
    return registry['names'][class_name]


def lookup_type(class_type, client=None):
    if 'https://schema.hbp.eu/Inference' in class_type:  # temporary workaround
        class_type = list(class_type)
        class_type.remove('https://schema.hbp.eu/Inference')
    if isinstance(class_type, str):
        if class_type in registry['types']:
            return registry['types'][class_type]
        else:
            return registry['types'][(class_type,)]
    else:
        return registry['types'][tuple(sorted(class_type))]


def lookup_by_iri(iri):
    for cls in registry["names"].values():
        if hasattr(cls, "iri_map") and iri in cls.iri_map.values():
            return cls
    raise ValueError("Can't resolve iri '{}'".format(iri))


def lookup_by_id(id):
    parts = urlparse(id)
    path_parts = parts.path.split("/")
    assert path_parts[2] == "data"
    path = "/".join(path_parts[3:-1])
    return registry["paths"][path]


def generate_cache_key(qd):
    """From a query dict, generate an object suitable as a key for caching"""
    if not isinstance(qd, dict):
        raise TypeError("generate_cache_key expects a query dict. You provided '{}'".format(qd))
    cache_key = []
    for key in sorted(qd):
        value = qd[key]
        if isinstance(value, (list, tuple)):
            sub_key = []
            for sub_value in value:
                sub_key.append(generate_cache_key(sub_value))
            cache_key.append(tuple(sub_key))
        elif isinstance(value, dict):
            cache_key.append((key, str(value)))
        elif value.__class__.__name__ == "IRI":  # a bit hacky
            cache_key.append((key, str(value)))
        else:
            if not isinstance(value, (str, int, float)):
                errmsg = "Expected a string, integer or float for key '{}', not a {}"
                raise TypeError(errmsg.format(key, type(value)))
            cache_key.append((key, value))
    return tuple(cache_key)


docstring_template = """
{base}

Args
----
{args}

"""


class Registry(type):
    """Metaclass for registering Knowledge Graph classes"""

    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        cls._base_docstring = class_dict.get("__doc__", "").strip()
        register_class(cls)
        return cls

    def _get_doc(self):
        """Dynamically generate docstrings"""
        field_docs = []
        if hasattr(self, "fields"):
            def gen_path(type_):
                if type_.__module__ == "builtins":
                    return type_.__name__
                else:
                    return "~{}.{}".format(type_.__module__, type_.__name__)
            for field in self.fields:
                doc = "{} : {}\n    {}".format(field.name,
                                               ", ".join(gen_path(t) for t in field.types),
                                               field.doc)
                field_docs.append(doc)
        return docstring_template.format(base=self._base_docstring, args="\n".join(field_docs))
    __doc__ = property(_get_doc)

    @property
    def path(cls):
        if cls.namespace is None:
            raise ValueError("namespace not set")
        return cls.namespace + cls._path

    @property
    def field_names(cls):
        return [f.name for f in cls.fields]

    @property
    def required_field_names(cls):
        return [f.name for f in cls.fields if f.required]
