import io
import os
import pathlib
from typing import Union
from aiohttp import ClientSession, FormData

from ..errors import _handle_errorcode

class WantsToParty:
    """The base class used for all asynchronous wants-to.party API interactions."""
    def __init__(
            self,
            *,
            api_key: str,
            subdomain: str
        ):
        super().__init__()
        self.api_key: str = api_key
        self.subdomain: str = subdomain
        
        self._BASE: str = f"https://{subdomain}.wants-to.party/upload"
        self._BASE_FILE_URL: str = f"https://{subdomain}.wants-to.party/"
    
    async def _post_file(
            self,
            file: Union[os.PathLike[str], io.BufferedIOBase],
            filetype: str,
            *,
            from_bytes: bool,
            filename: str = None
        ):
        headers = {"key": self.api_key}
        
        if from_bytes:
            if not filetype.endswith("."):
                filetype = "." + filetype

            form = FormData(quote_fields=False)
            filename = f"file{filetype}"
            form.add_field("file", file.getvalue(), filename=filename)
        else:
            form = FormData()
            form.add_field("file", open(file, "rb"), filename=filename + filetype)
        
        async with ClientSession(headers=headers) as session:
            async with session.post(self._BASE, data=form) as resp:
                if resp.status != 200:
                    return _handle_errorcode(resp.status)
                
                return await resp.json()
    
    async def upload_from_bytes(
            self, 
            file: io.BufferedIOBase,
            filetype: str
        ) -> dict:
        """Uploads a file-like object using the raw binary data
        provided.

        Returns the JSON-formatted response.

        Attributes
        -----------
        file - The raw binary data associated with the file.
               Using `io.BytesIO` is recommended.
            
        filetype - The file type associated with the file
                   you're uploading. I.E., ".png".
        """
        return await self._post_file(file, filetype, from_bytes=True)
    
    async def upload_from_file(
            self,
            file: os.PathLike[str]
        ):
        """Uploads a local file using the file path provided.
        
        Returns the JSON-formatted response.
        
        Attributes
        -----------
        file - The path to the file stored on your local disk.
        """
        filedata = pathlib.Path(file)
        
        filename = filedata.stem
        filetype = filedata.suffix
        path = os.path.abspath(file)
        return await self._post_file(path, filetype, filename=filename, from_bytes=False)
