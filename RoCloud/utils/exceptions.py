from typing import Type

from . import VERSION_ONE, VERSION_TWO


class RobloxCloudException(Exception):
    pass    

class InvalidKey(RobloxCloudException):
    pass

class InvalidArgument(RobloxCloudException):
    pass

class PermissionDenied(RobloxCloudException):
    pass

class NotFound(RobloxCloudException):
    pass

class Aborted(RobloxCloudException):
    pass

class ResourceExhausted(RobloxCloudException):
    pass

class Cancelled(RobloxCloudException):
    pass

class Internal(RobloxCloudException):
    pass

class NotImplemented(RobloxCloudException):
    pass

class Unavailable(RobloxCloudException):
    pass

LOOKUP = {
    VERSION_ONE: {
        1: 'TODO'
    },
    VERSION_TWO: {
        400: InvalidArgument,
        401: InvalidKey,
        403: PermissionDenied,
        404: NotFound,
        409: Aborted,
        429: ResourceExhausted,
        499: Cancelled,
        500: Internal,
        501: NotImplemented,
        503: Unavailable
    }
}

def _error_code_to_exception(endpoint_version: str, status_code: int) -> Type[RobloxCloudException]:
    return LOOKUP[endpoint_version].get(status_code) or RobloxCloudException