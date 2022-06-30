class MissingRequiredOauthArguments(Exception):
    pass

class NoScopesProvided(Exception):
    pass

class Unauthorized(Exception):
    pass

class Forbidden(Exception):
    pass

class BadRequest(Exception):
    pass

class InternalServerError(Exception):
    pass

class UnhandledError(Exception):
    pass

class MissingFileType(Exception):
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
            