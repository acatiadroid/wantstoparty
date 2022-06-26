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