"""
Script to build the authors.rst file
"""

import json
import requests
from pathlib import Path

def full_name(au):
    return f"{au['givenName']} {au['familyName']}"

with open("authors.json") as fp:
    author_data = json.load(fp)
author_list = ", ".join(f"{full_name(au)}" for au in author_data)

with open("authors.rst.tpl") as fp:
    template = fp.read()

affiliation_ids = []
for person in author_data:
    for affil in person["affiliation"]:
        if affil["@id"] not in affiliation_ids:
            affiliation_ids.append(affil["@id"])

cache_path = ".rorid_cache"

if not Path(cache_path).exists():
    affiliation_data = {}
    for affil_id in affiliation_ids:
        response = requests.get(f"https://api.ror.org/v2/organizations/{affil_id.split('/')[-1]}")
        if response.status_code == 200:
            affiliation_data[affil_id] = response.json()
        else:
            print(response)
    with open(cache_path, "w") as fp:
        json.dump(affiliation_data, fp, indent=2)
else:
    with open(cache_path) as fp:
        affiliation_data = json.load(fp)


def get_affiliation_text(org):
    name = [entry["value"] for entry in org["names"] if entry["lang"] == "en" and "label" in entry["types"]][0]
    location = org["locations"][0]["geonames_details"]
    city = location["name"]
    country = location["country_name"]
    parents = [rel["label"] for rel in org["relationships"] if rel["type"] == "parent"]
    if parents:
        return f"{name}, {', '.join(parents)}, {city}, {country}"
    else:
        return f"{name}, {city}, {country}"

def affiliation_number(au, affiliations):
    index = list(affiliations.keys()).index(au["affiliation"][0]["@id"])  # to do: handle people with multiple affiliations
    return index + 1


affiliations_text = "\n".join(
    f"{i}. {get_affiliation_text(affiliation_data[org_id])}" for i, org_id in enumerate(affiliation_data, start=1)
)

authors_text = "\n".join(
    [f"- {full_name(au)} [{affiliation_number(au, affiliation_data)}]" for au in author_data]
)

with open("authors.rst", "w") as fp:
    fp.write(template.format(authors=authors_text, affiliations=affiliations_text))
