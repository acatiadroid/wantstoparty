class MissingRequiredOauthArguments(Exception):
    """Raised when there are missing Oauth scopes."""
    pass

class NoScopesProvided(Exception):
    """Raised when no scopes are provided."""
    pass

class Unauthorized(Exception):
    """Raised when a 401 error code is returned by wants-to.party."""
    pass

class Forbidden(Exception):
    """Raised when a 403 error code is returned by wants-to.party."""
    pass

class BadRequest(Exception):
    """Raised when a 400 error code is returned by wants-to.party."""
    pass

class InternalServerError(Exception):
    """Raised when a 500 error code is returned by wants-to.party."""
    pass

class UnhandledError(Exception):
    """Raised when a 401 error code is returned by wants-to.party."""
    pass

class MaxFileSizeExceeded(Exception):
    """Raised when a file size is larger than the preset size, set by the `SizeLimit` object."""
    pass

def _handle_errorcode(code, message):
        if code == 401:
            raise Unauthorized(message)
        elif code == 403:
            raise Forbidden(message)
        elif code == 400:
            raise BadRequest(message)
        elif code == 500:
            raise InternalServerError(message)
        else:
            raise UnhandledError(message)
            