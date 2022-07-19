import io
import os
import pathlib
from typing import Union

import requests

from .checks import Size
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
    
    def _post_file(
            self,
            file,
            filetype: str,
            *,
            from_bytes: bool,
            filename: str = None,
            max_bytes: Size = None
        ):
        headers = {"key": self.api_key}
        
        if from_bytes:
            if max_bytes:
                max_bytes._check_bytes(file.getbuffer().nbytes)

            if not filetype.endswith("."):
                filetype = "." + filetype

            filename = f"file{filetype}"
            
            file = {"file": (filename, file.getvalue())}
        else:
            if max_bytes:
                max_bytes._check_bytes(os.path.getsize(file))

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
            filetype: str,
            *,
            max_bytes: Size = None
        ) -> str:
        """Uploads a file-like object using the raw binary data
        provided.

        Returns the URL of the uploaded file.

        Attributes
        -----------
        file - The raw binary data associated with the file.
               Using `io.BytesIO` is recommended.
            
        filetype - The file type associated with the file
                   you're uploading. I.E., ".png".

        max_bytes - A maximum number of bytes uploadable. Use
        the Size class to specify the number of bytes. 
        """
        return self._post_file(file, filetype, from_bytes=True, max_bytes=max_bytes)
    
    def upload_from_file(
            self,
            file: str,
            *,
            max_bytes: Size = None
        ) -> str:
        """Uploads a local file using the file path provided.
        
        Returns the URL of the uploaded file.
        
        Attributes
        -----------
        file - The path to the file stored on your local disk.

        max_bytes - A maximum number of bytes uploadable. Use
        the Size class to specify the number of bytes. 
        """
        fpath = pathlib.Path(file)
        
        filename = fpath.stem
        filetype = fpath.suffix
        path = os.path.abspath(file)
        return self._post_file(path, filetype, filename=filename, from_bytes=False, max_bytes=max_bytes)
        