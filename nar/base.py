"""

"""

from functools import wraps
from .errors import ResourceExistsError


class KGObject(object):
    """Base class for Knowledge Graph objects"""
    cache = {}

    @classmethod
    def from_kg_instance(self, instance, client):
        raise NotImplementedError("To be implemented by child class")

    @classmethod
    def from_uri(cls, uri, client):
        return cls.from_kg_instance(client.instance_from_full_uri(uri),
                                    client)

    @classmethod
    def list(cls, client):
        """List all objects of this type in the Knowledge Graph"""
        return client.list(cls)

    def exists(self, client):
        """Check if this object already exists in the KnowledgeGraph"""
        # Note that this default implementation should in
        # many cases be over-ridden.
        if self.id:
            return True
        else:
            context = {"schema": "http://schema.org/"},
            query_filter = {
                "path": "schema:name",
                "op": "eq",
                "value": self.name
            }
            response = client.filter_query(self.path, query_filter, context)
            if response:
                self.id = response[0].data["@id"]
            return bool(response)

    def _save(self, data, client, exists_ok=True):
        """docstring"""
        if self.id:
            raise NotImplementedError("Update not yet implemented")
        else:
            if self.exists(client):
                if exists_ok:
                    return
                else:
                    raise ResourceExistsError(f"Already exists in the Knowledge Graph: {self!r}")
            instance = client.create_new_instance(self.__class__.path, data)
            self.id = instance.data["@id"]
            KGObject.cache[self.id] = self


def cache(f):
    @wraps(f)
    def wrapper(cls, instance, client):
        if instance.data["@id"] in KGObject.cache:
            obj = KGObject.cache[instance.data["@id"]]
            #print(f"Found in cache: {obj.id}")
            return obj
        else:
            obj = f(cls, instance, client)
            KGObject.cache[obj.id] = obj
            #print(f"Added to cache: {obj.id}")
            return obj
    return wrapper


class KGProxy(object):
    """docstring"""

    def __init__(self, cls, uri):
        self.cls = cls
        self.id = uri
    
    def resolve(self, client):
        """docstring"""
        if self.id in KGObject.cache:
            return KGObject.cache[self.id]
        else:
            obj = self.cls.from_uri(self.id, client)
            KGObject.cache[self.id] = obj
            return obj

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.cls!r}, {self.id!r})')


class KGQuery(object):
    """docstring"""

    def __init__(self, cls, filter, context):
        self.cls = cls
        self.filter = filter
        self.context = context

    def resolve(self, client):
        instances = client.filter_query(
            path=self.cls.path,
            filter=self.filter,
            context=self.context
        )
        objects = [self.cls.from_kg_instance(instance, client)
                   for instance in instances]
        for obj in objects:
            KGObject.cache[obj.id] = obj
        if len(instances) == 1:
            return objects[0]
        else:
            return objects
