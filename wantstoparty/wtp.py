import io
import os
import pathlib
from typing import Union

import requests

from .errors import _handle_errorcode

class WantsToParty:
    """The base class used for all wants-to.party API interactions.
    
    Keyword arguments
    -----------
    api_key - Your API key. This can be found on your dashboard.

    subdomain - Your unique subdomain. This can also be found on your dashboard.
    """
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
    
    def _post_file(
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

            filename = f"file{filetype}"
            
            file = {"file": (filename, file.getvalue())}
        else:
            file_data = open(file, "rb")
            
            file = {"file": (filename + filetype, file_data)}

        resp = requests.post(
            self._BASE,
            headers=headers,
            files=file
        )
        
        payload = resp.json()

        if resp.status_code != 200:
            return _handle_errorcode(resp.status_code, payload["error"])
        
        return payload["url"]
    
    def upload_from_bytes(
            self, 
            file: io.BufferedIOBase,
            filetype: str
        ) -> str:
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
        return self._post_file(file, filetype, from_bytes=True)
    
    def upload_from_file(
            self,
            file: Union[os.PathLike[str], str]
        ) -> str:
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
        return self._post_file(path, filetype, filename=filename, from_bytes=False)
        