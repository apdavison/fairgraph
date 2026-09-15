"""
Script to generate a codemeta.json file

Run it in two steps when making a release:

    $ python build_codemeta.py                 # before the release, as part of the release commit
    $ python build_codemeta.py --download-url  # once the release is on PyPI

The first step generates all fields from the local project metadata (pyproject.toml and
authors.json), with "downloadUrl" set to null, since the release is not
yet on PyPI. The second step fills in "downloadUrl" from PyPI, and sets "dateModified" to the
date of the upload if that differs from the date the first step was run, leaving the other
fields unchanged.
"""

from datetime import date, datetime
import json
import os
import tomllib

here = os.path.dirname(__file__)
codemeta_path = os.path.join(here, "..", "codemeta.json")


def codemeta_author(author):
    # "alternateName" is not a CodeMeta term, so a pseudonym is given as the person's name
    author = dict(author)
    if "alternateName" in author and "name" not in author:
        author["name"] = author.pop("alternateName")
    return author


def generate():
    with open(os.path.join(here, "..", "pyproject.toml"), "rb") as fp:
        project = tomllib.load(fp)["project"]
    version = project["version"]
    if "dev" in version:
        raise ValueError(f"codemeta.json describes a release, not a development version ({version})")

    with open(os.path.join(here, "authors.json")) as fp:
        authors = [codemeta_author(author) for author in json.load(fp)]
    with open(os.path.join(here, "organizations.json")) as fp:
        organizations = json.load(fp)

    return {
        "@context": "https://doi.org/10.5063/schema/codemeta-2.0",
        "@type": "SoftwareSourceCode",
        "license": "https://spdx.org/licenses/Apache-2.0.html",
        "codeRepository": "https://github.com/HumanBrainProject/fairgraph",
        "contIntegration": "https://github.com/HumanBrainProject/fairgraph/actions",
        "dateModified": date.today().isoformat(),
        "downloadUrl": None,
        "issueTracker": "https://github.com/HumanBrainProject/fairgraph/issues",
        "name": "fairgraph",
        "version": version,
        "identifier": f"https://pypi.org/project/fairgraph/{version}/",
        "description": project["description"],
        "applicationCategory": "neuroscience",
        "releaseNotes": f"https://fairgraph.readthedocs.io/en/latest/release_notes.html#version-{version.replace('.', '-')}",
        "funding": "https://cordis.europa.eu/project/id/945539",
        "developmentStatus": "active",
        "referencePublication": None,
        "funder": {"@type": "Organization", "name": "European Commission"},
        "programmingLanguage": ["Python"],
        "operatingSystem": ["Linux", "Windows", "macOS"],
        "softwareRequirements": [f"Python {project['requires-python']}"] + project["dependencies"],
        "relatedLink": ["https://fairgraph.readthedocs.io"],
        "author": authors,
    }


def add_download_url(code_metadata):
    import requests

    version = code_metadata["version"]
    response = requests.get(f"https://pypi.org/pypi/fairgraph/{version}/json")
    response.raise_for_status()
    sdists = [item for item in response.json()["urls"] if item["packagetype"] == "sdist"]
    if not sdists:
        raise ValueError(f"No source distribution found on PyPI for fairgraph {version}")
    code_metadata["downloadUrl"] = sdists[0]["url"]
    # the upload may have happened on a later day than the release commit
    code_metadata["dateModified"] = datetime.fromisoformat(sdists[0]["upload_time"]).date().isoformat()
    return code_metadata


if __name__ == "__main__":
    import sys

    if "--download-url" in sys.argv[1:]:
        with open(codemeta_path) as fp:
            code_metadata = add_download_url(json.load(fp))
    else:
        code_metadata = generate()

    with open(codemeta_path, "w") as fp:
        json.dump(code_metadata, fp, indent=2)
