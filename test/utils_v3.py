from copy import deepcopy
from uuid import uuid4
from fairgraph.client_v3 import KGv3Client as KGClient
from fairgraph.errors import AuthenticationError

import pytest



have_kg_connection = False
try:
    client = KGClient(host="core.kg-ppd.ebrains.eu")  # don't use production for testing
except AuthenticationError:
    pass
else:
    if client.user_info():
        have_kg_connection = True

no_kg_err_msg = "No KG connection - have you set the environment variable KG_AUTH_TOKEN?"


def skip_if_no_connection(f):
    return pytest.mark.skipif(not have_kg_connection, reason=no_kg_err_msg)(f)


@pytest.fixture(scope="session")
def kg_client():
    return client


class MockKGResponse:

    def __init__(self, data):
        self.data = data


class MockKGClient:
    _private_space = "myspace_1234"

    def __init__(self):
        self.instances = {}

    def retrieve_query(self, query_label):
        return {
            "@id": f"mock-query-{query_label}"
        }

    def query(self, filters, query_id, space=None, size=100, from_index=0, scope="released"):
        if "name" in filters:
            if "Dummy new model" in filters["name"]:
                return MockKGResponse(None)
            elif "protein structure" in filters["name"]:
                return MockKGResponse([{
                    "vocab:name": filters["name"],
                    "@id": "fake_uuid",
                    "https://core.kg.ebrains.eu/vocab/meta/space": "controlled",
                    "@type": ['https://openminds.ebrains.eu/controlledTerms/ModelAbstractionLevel']
                }])
            elif "subcellular" in filters["name"]:
                return MockKGResponse([{
                    "vocab:name": filters["name"],
                    "@id": "fake_uuid",
                    "https://core.kg.ebrains.eu/vocab/meta/space": "controlled",
                    "@type": ['https://openminds.ebrains.eu/controlledTerms/ModelScope']
                }])
            elif "Mus musculus" in filters["name"]:
                return MockKGResponse([{
                    "vocab:name": filters["name"],
                    "@id": "fake_uuid",
                    "https://core.kg.ebrains.eu/vocab/meta/space": "controlled",
                    "@type": ['https://openminds.ebrains.eu/controlledTerms/Species']
                }])
            elif "astrocyte" in filters["name"]:
                return MockKGResponse([{
                    "vocab:name": filters["name"],
                    "@id": "fake_uuid",
                    "https://core.kg.ebrains.eu/vocab/meta/space": "controlled",
                    "@type": ['https://openminds.ebrains.eu/controlledTerms/CellType']
                }])
            elif "amygdala" in filters["name"]:
                return MockKGResponse([{
                    "vocab:name": filters["name"],
                    "@id": "fake_uuid",
                    "https://core.kg.ebrains.eu/vocab/meta/space": "controlled",
                    "@type": ['https://openminds.ebrains.eu/controlledTerms/UBERONParcellation']
                }])
            elif "The Lonely Mountain" in filters["name"]:
                return MockKGResponse([])
        elif "given_name" in filters:
            if filters["given_name"] == "Thorin":
                return MockKGResponse([])
        raise NotImplementedError("case not yet handled by mock client")

    def create_new_instance(self, data, space, instance_id=None):
        assert space is not None
        assert data is not None
        instance = deepcopy(data)
        instance["@id"] = instance_id or str(uuid4())
        instance["https://core.kg.ebrains.eu/vocab/meta/space"] = space
        self.instances[instance["@id"]] = instance
        return instance


@pytest.fixture
def mock_client():
    return MockKGClient()