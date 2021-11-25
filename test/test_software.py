# encoding: utf-8
"""
Tests of the "software" module
"""

from datetime import date
import json
from fairgraph.software import Software, OperatingSystem, SoftwareCategory, ProgrammingLanguage, License
from fairgraph.core import Person, Organization
from fairgraph.commons import License
try:
    import pyxus
    have_pyxus = True
except ImportError:
    have_pyxus = False
import pytest

class MockInstance(object):

    def __init__(self, data):
        self.data = data


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestSoftware(object):

    def test__build_data(self):

        input_data = dict(
            name="PyNN v0.9.4",
            version="0.9.4",
            summary="A Python package for simulator-independent specification of neuronal network models",
            description="PyNN (pronounced 'pine') is a simulator-independent language for building neuronal network models.",
            #identifier=Identifier("RRID:SCR_002715"),
            citation=("Davison AP, Brüderle D, Eppler JM, Kremkow J, Muller E, Pecevski DA, Perrinet L and Yger P (2009) "
                      "PyNN: a common interface for neuronal network simulators. "
                      "Front. Neuroinform. 2:11 doi:10.3389/neuro.11.011.2008"),
            license=License("CeCILL v2"),
            release_date=date(2019, 3, 22),
            previous_version=None,
            contributors=[Person("Davison", "Andrew", "andrew.davison@unic.cnrs-gif.fr")],
            project=None,
            image="https://neuralensemble.org/static/photos/pynn_logo.png",
            download_url="https://files.pythonhosted.org/packages/a2/1c/78b5d476900254c2c638a29a343ea12985ea16b12c7aed8cec252215c848/PyNN-0.9.4.tar.gz",
            access_url="https://pypi.org/project/PyNN/0.9.4/",
            categories=None,
            subcategories=None,
            operating_system=[OperatingSystem("Linux"), OperatingSystem("MacOS"), OperatingSystem("Windows")],
            release_notes="http://neuralensemble.org/docs/PyNN/releases/0.9.4.html",
            requirements="neo, lazyarray",
            copyright=Organization("The PyNN community"),
            components=None,
            part_of=None,
            funding=[Organization("CNRS"), Organization("Human Brain Project")],
            languages=ProgrammingLanguage("Python"),
            features=None,
            #keywords="simulation, neuroscience",
            is_free=True,
            homepage="https://neuralensemble.org/PyNN/",
            documentation="http://neuralensemble.org/docs/PyNN/",
            help="https://groups.google.com/forum/#!forum/neuralensemble"
        )
        software_release = Software(**input_data)
        kg_data = software_release._build_data(client=None)
        assert kg_data == {
            'name': input_data["name"],
            'version': input_data["version"],
            'headline': input_data["summary"],
            'description': input_data["description"],
            'citation': input_data["citation"],
            'license': {'@id': input_data["license"].iri, 'label': input_data["license"].label},
            'dateCreated': '2019-03-22',
            #'copyrightYear': input_data["release_date"].year,
            'author': {'@id': None, '@type': ['nsg:Person', 'prov:Agent']},
            #'image': {'@id': input_data["image"]},
            #'distribution': {
            #    'downloadURL': {"@id": input_data["download_url"]},
            #    'accessURL': {"@id": input_data["access_url"]}
            #},
            'operatingSystem': [
                {'@id': os.iri, 'label': os.label}
                for os in input_data["operating_system"]
            ],
            'releaseNotes': {'@id': input_data["release_notes"]},
            'softwareRequirements': input_data["requirements"],
            'copyrightHolder': {'@id': None, '@type': ['nsg:Organization']},
            'funder': [{'@id': None, '@type': ['nsg:Organization']}, {'@id': None, '@type': ['nsg:Organization']}],
            #'programmingLanguage': [{'@id': input_data["languages"].iri, 'label': input_data["languages"].label}],
            #'keywords': input_data["keywords"],
            'isAccessibleForFree': input_data["is_free"],
            'url': {'@id': input_data["homepage"]},
            'documentation': {'@id': input_data["documentation"]},
            'softwareHelp': {'@id': input_data["help"]}
        }

    def test_from_instance(self):
        instance_data = json.loads("""{
            "@context": [
                "https://nexus-int.humanbrainproject.org/v0/contexts/neurosciencegraph/core/data/v0.1.0",
                {
                    "dbpedia": "http://dbpedia.org/resource/",
                    "wd": "http://www.wikidata.org/entity/",
                    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
                    "label": "rdfs:label",
                    "schema": "http://schema.org/",
                    "hbpsc": "https://schema.hbp.eu/softwarecatalog/"
                },
                "https://nexus-int.humanbrainproject.org/v0/contexts/nexus/core/resource/v0.3.0"
            ],
            "@id": "https://nexus-int.humanbrainproject.org/v0/data/softwarecatalog/software/software/v0.1.1/beb9546e-c801-4159-ab3f-5678a5f75f33",
            "@type": [
                "hbpsc:Software",
                "nsg:Entity"
            ],
            "providerId": "doi:10.5281/zenodo.1400175",
            "applicationCategory": [
                {
                    "@id": "https://www.wikidata.org/wiki/Q166142",
                    "label": "application"
                }
            ],
            "applicationSubCategory": [
                {
                    "@id": "https://www.wikidata.org/wiki/Q184148",
                    "label": "plug-in"
                }
            ],
            "citation": "Linssen, Charl et al. (2018). NEST 2.16.0. Zenodo. 10.5281/zenodo.1400175",
            "code": {
                "@id": "https://github.com/nest/nest-simulator"
            },
            "copyrightYear": 2018,
            "dateCreated": "2018-08-21",
            "description": "NEST is a highly scalable simulator for networks of point or few-compartment spiking neuron models. It includes multiple synaptic plasticity models, gap junctions, and the capacity to define complex network structure.",
            "device": [
                {
                    "@id": "https://www.wikidata.org/wiki/Q5082128",
                    "label": "mobile device"
                }
            ],
            "documentation": {
                "@id": "http://www.nest-simulator.org/documentation/"
            },
            "encodingFormat": [
                {
                    "@id": "https://www.wikidata.org/wiki/Q28865",
                    "label": "Python"
                }
            ],
            "headline": "NEST is a highly scalable simulator for networks of point or few-compartment spiking neuron models. It includes multiple synaptic plasticity models, gap junctions, and the capacity to define complex network structure.",
            "identifier": [
                {
                    "propertyID": "doi",
                    "value": "10.5281/zenodo.1400175"
                },
                {
                    "@id": "https://doi.org/10.5281/zenodo.1400175"
                }
            ],
            "image": {
                "@id": "http://www.nest-simulator.org/wp-content/uploads/nest-simulated-www-320.png"
            },
            "isAccessibleForFree": true,
            "programmingLanguage": [
                {
                    "@id": "https://www.wikidata.org/wiki/Q28865",
                    "label": "Python"
                }
            ],
            "license": {
                "@id": "https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html",
                "label": "GNU General Public License 2 or later (http://www.nest-simulator.org/license/)"
            },
            "name": "NEST v2.16.0",
            "operatingSystem": [
                {
                    "@id": "http://dbpedia.org/resource/Linux",
                    "label": "Linux"
                }
            ],
            "releaseNotes": {
                "@id": "https://github.com/nest/nest-simulator/releases/tag/v2.16.0"
            },
            "screenshot": {
                "@id": "http://www.nest-simulator.org/wp-content/uploads/nest-simulated-www-320.png"
            },
            "softwareHelp": {
                "@id": "http://www.nest-simulator.org/community/"
            },
            "softwareRequirements": "libreadline, gsl, ...",
            "url": {
                "@id": "http://www.nest-simulator.org/"
            },
            "version": "2.16.0"
        }
        """)
        instance = MockInstance(instance_data)
        software_release = Software.from_kg_instance(instance, client=None, use_cache=False)
        assert software_release.name == instance_data["name"]
        assert software_release.operating_system == OperatingSystem("Linux")
