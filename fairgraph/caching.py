
from collections import defaultdict


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


object_cache = {}  # for caching based on object ids
save_cache = defaultdict(dict)  # for caching based on queries
