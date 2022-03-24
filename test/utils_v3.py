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


class MockKGClient:
    _private_space = "myspace_1234"


@pytest.fixture
def mock_client():
    return MockKGClient()