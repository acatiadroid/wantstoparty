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

def _handle_errorcode(self, code):
        if code == 401:
            raise Unauthorized()
        elif code == 403:
            raise Forbidden("Likely caused by being banned or invalid API key.")
        elif code == 400:
            raise BadRequest("Either caused by max file size being exceeded (100MB), " \
                "no file recieved, or other reason.")
        elif code == 500:
            raise InternalServerError("An internal server error occured. Try again later.")
        else:
            raise UnhandledError(f"An unhandled error occured. Error code: {code}")
            