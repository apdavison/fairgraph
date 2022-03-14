"""

"""


class ResourceExistsError(Exception):
    """Raised when trying to create a resource that already exists in the Knowledge Graph"""
    pass


class AuthenticationError(Exception):
    """Raised when there is a problem with authentication"""
    pass


class ResolutionFailure(Exception):
    """Raised when unable to resolve a link in the Knowledge Graph"""
    pass
