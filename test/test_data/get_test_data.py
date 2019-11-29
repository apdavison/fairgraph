"""
Script to retrieve/update test data
"""

import os.path
from itertools import cycle
import json
from fairgraph import KGClient, core, brainsimulation, electrophysiology, minds, uniminds

core.use_namespace("neuralactivity")

client = KGClient()


def save_nexus_query_result(module, cls):
    path = "/data/{}/?fields=all&size=10&deprecated=False".format(cls.path)
    response = client._nexus_client._http_client.get(path)
    fix_fields(response)
    filename = "{}_list_0_10.json".format(cls.__name__.lower())
    local_path = os.path.join("nexus",
                                module.__name__.split(".")[1],
                                filename)
    if "next" in response["links"]:
        del response["links"]["next"]
    with open(local_path, "w") as fp:
        json.dump(response, fp, indent=4)


def save_kg_query_result(module, cls, query_label):
    query_id = {"simple": cls.query_id,
                "resolved": cls.query_id_resolved}[query_label]
    path = "{}/{}/instances?start=0&size=10&databaseScope=INFERRED".format(
        cls.path, query_id)
    response = client._kg_query_client.get(path)
    fix_fields(response)
    filename = "{}_list_{}_0_10.json".format(cls.__name__.lower(), query_label)
    local_path = os.path.join("kgquery",
                              module.__name__.split(".")[1],
                              filename)
    with open(local_path, "w") as fp:
        json.dump(response, fp, indent=4)


def save_kg_query_spec(module, cls, query_label):
    query_id = {"simple": cls.query_id,
                "resolved": cls.query_id_resolved}[query_label]
    spec = cls.retrieve_query(query_id, client)
    filename = "{}_{}_query.json".format(cls.__name__.lower(), query_label)
    local_path = os.path.join("kgquery",
                              module.__name__.split(".")[1],
                              filename)
    with open(local_path, "w") as fp:
        json.dump(spec, fp, indent=4)


def fix_fields(data):
    replacement_names = cycle([
        "Neil;Armstrong;neil.armstrong@nasa.gov",
        "Yvonne;Brill;unknown@example.com",
        "Frank;Whittle;unknown@example.com",
        "Johanna;Weber;unknown@example.com",
        "Frank;Borman;unknown@example.com",
        "Kalpana;Chawla;unknown@example.com",
        "Igor;Sikorsky;unknown@example.com",
        "Elsie;McGill;unknown@example.com",
        "Leonardo;da Vinci;unknown@example.com",
        "Katherine;Johnson;unknown@example.com"
    ])

    def nested_dict_iter(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                #print(key)
                if isinstance(value, (list, dict)):
                    nested_dict_iter(value)
                else:
                    if key == "givenName" and "schema" not in value:
                        obj["givenName"], obj["familyName"], obj["email"] = next(replacement_names).split(";")
                        break
                    elif key == "http://schema.org/givenName":
                        obj["http://schema.org/givenName"], obj["http://schema.org/familyName"], obj["http://schema.org/email"] = next(replacement_names).split(";")
                        break
                    elif isinstance(value, str) and "object.cscs.ch" in value:
                        obj[key] = value[:31]
        elif isinstance(obj, (list, dict)):
            for item in obj:
                nested_dict_iter(item)
        else:
            pass

    data = nested_dict_iter(data)
    return data


for module in (core, brainsimulation, electrophysiology, minds, uniminds):
    for cls in module.list_kg_classes():
        save_nexus_query_result(module, cls)
        for label in ("simple", "resolved"):
            save_kg_query_result(module, cls, label)
            save_kg_query_spec(module, cls, label)
        cls.store_queries(client)

#save_kg_query_result(brainsimulation, brainsimulation.MEModel, "resolved")
#save_nexus_query_result(uniminds, uniminds.Person)
