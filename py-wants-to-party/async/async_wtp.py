import io
import random
import string
from typing import Union
from aiohttp import ClientSession

from ..errors import (
    BadRequest,
    Forbidden,
    InternalServerError,
    Unauthorized,
    UnhandledError
)

class WantsToParty:
    def __init__(
            self,
            *,
            api_key: str,
            subdomain: str
        ):
        self.api_key = api_key
        self.subdomain = subdomain
        self.BASE = f"https://{subdomain}.wants-to.party/upload"
    
    @classmethod
    async def _make_post_req(self, file: Union[str, io.BytesIO], filename):
        headers = {
            "key": self.api_key,
            "Content-Type": "multipart-form-data"
        }

        if isinstance(file, str):
            file = open(file, "rb")
        elif isinstance(file, io.BytesIO):
            pass

        async with ClientSession(headers=headers) as session:
            async with session.post(self.BASE, files={"file": (filename, file)}) as resp:

                if resp.status != 200:
                    return self._handle_errorcode(resp.status)
                    
                return resp.json()
    
    @classmethod
    async def upload_file(self, *, file_name: str=None, file: Union[str, io.BytesIO]):
        """Uploads a file."""
        if not file_name:
            file_name = self._gen_random_filename()
        await self._make_post_req(file, file_name)

    @staticmethod
    def _gen_random_filename():
        return random.choice(string.ascii_lowercase, k=10)

    @classmethod
    def _handle_errorcode(self, code):
        if code == 401:
            raise Unauthorized("Invalid API key provided.")
        elif code == 403:
            raise Forbidden("Likely caused by being banned.")
        elif code == 400:
            raise BadRequest("Either caused by max file size being exceeded (100MB) " \
                "or other reason.")
        elif code == 500:
            raise InternalServerError("An internal server error occured. Try again later.")
        else:
            raise UnhandledError(f"An unhandled error occured. Error code: {code}")