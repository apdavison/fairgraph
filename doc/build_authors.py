"""
Script to build the authors.rst file
"""

import json
import requests
from pathlib import Path

def full_name(au):
    # contributors may give a pseudonym (alternateName) rather than their given and family names
    return " ".join(filter(None, (au.get("givenName"), au.get("familyName")))) or au["alternateName"]


def affiliation_key(affil):
    # affiliations are identified by their ROR ID where there is one, otherwise by name
    return affil.get("@id", affil.get("name"))


with open("authors.json") as fp:
    author_data = json.load(fp)
author_list = ", ".join(f"{full_name(au)}" for au in author_data)

with open("authors.rst.tpl") as fp:
    template = fp.read()

# all affiliations, in order of first appearance in the author list
affiliations = {}
for person in author_data:
    for affil in person["affiliation"]:
        affiliations.setdefault(affiliation_key(affil), affil)
affiliation_ids = [affil["@id"] for affil in affiliations.values() if "@id" in affil]

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


def get_affiliation_text(affil):
    if "@id" in affil:
        org = affiliation_data[affil["@id"]]
        name = [entry["value"] for entry in org["names"] if entry["lang"] == "en" and "label" in entry["types"]][0]
        location = org["locations"][0]["geonames_details"]
        city = location["name"]
        country = location["country_name"]
        parents = [rel["label"] for rel in org["relationships"] if rel["type"] == "parent"]
        if parents:
            return f"{name}, {', '.join(parents)}, {city}, {country}"
        else:
            return f"{name}, {city}, {country}"
    else:
        # an organization without a ROR ID, given by name and optionally address
        return ", ".join(filter(None, (affil["name"], affil.get("address"))))


def affiliation_number(au, affiliations):
    index = list(affiliations.keys()).index(affiliation_key(au["affiliation"][0]))  # to do: handle people with multiple affiliations
    return index + 1


affiliations_text = "\n".join(
    f"{i}. {get_affiliation_text(affil)}" for i, affil in enumerate(affiliations.values(), start=1)
)

authors_text = "\n".join(
    [f"- {full_name(au)} [{affiliation_number(au, affiliations)}]" for au in author_data]
)

with open("authors.rst", "w") as fp:
    fp.write(template.format(authors=authors_text, affiliations=affiliations_text))
