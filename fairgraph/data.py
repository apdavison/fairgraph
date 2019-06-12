"""

"""

try:
    from urllib.request import urlretrieve
except ImportError:  # Python 2
    from urllib import urlretrieve
try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path
from fairgraph.base import KGObject, KGProxy, KGQuery, cache


class DataObject(KGObject):
    """docstring"""

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        """docstring"""
        D = instance.data
        data = {}
        for key, value in D.items():
            if key.startswith('https://schema.hbp.eu/cscs/'):
                name = key.split('https://schema.hbp.eu/cscs/')[1]
            elif key.startswith('https://schema.hbp.eu/linkinginstance/'):
                name = key.split('https://schema.hbp.eu/linkinginstance/')[1]
            elif key.startswith('http://schema.org/'):
                name = key.split('http://schema.org/')[1]
            elif ":" in key:
                name = key.split(":")[1]
            else:
                name = None
            if name in cls.property_names:
                if name in obj_types:
                    if isinstance(value, list):
                        data[name] = [KGProxy(obj_types[name], item["@id"])
                                      for item in value]
                    elif "@list" in value:
                        assert len(value) == 1
                        data[name] = [KGProxy(obj_types[name], item["@id"])
                                      for item in value['@list']]
                    else:
                        data[name] = KGProxy(obj_types[name], value["@id"])
                else:
                    data[name] = value
        data["id"] = D["@id"]
        data["instance"] = instance
        return cls(**data)


class FileAssociation(DataObject):
    path = "cscs/core/fileassociation/v1.0.0"
    type = ["cscs:Fileassociation", "https://schema.hbp.eu/LinkingInstance"]
    property_names = ["name", "from", "to"]

    @property
    def from_(self):
        """Return the 'from' property of the file association

        (note trailing underscore since 'from' is a reserved word in Python
        """
        return getattr(self, "from")


class CSCSFile(DataObject):
    path = "cscs/core/file/v1.0.0"
    type = ["cscs:File"]
    property_names = ["name", "absolute_path", "byte_size", "content_type",
                      "last_modified", "relative_path"]

    def download(self, base_dir=".", preserve_relative_path=True):
        local_filename = Path(base_dir)
        if preserve_relative_path:
            local_filename = local_filename / self.relative_path
        else:
            local_filename = local_filename / self.name
        local_filename.parent.mkdir(parents=True, exist_ok=True)
        local_filename, headers = urlretrieve(self.absolute_path, local_filename)
        return local_filename


# todo: integrate this into the registry
obj_types = {


}