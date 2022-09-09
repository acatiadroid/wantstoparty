import io
import os
import pathlib

from ..objects import User, FileSize
from ..http import AsyncRequest

class WantsToParty:
    """The base class for all wants-to.party API interactions."""
    def __init__(
        self,
        api_key: str
    ):
        self.data = {"key": api_key}

    async def upload_from_bytes(
        self,
        file: io.BufferedIOBase,
        filetype: str,
        *,
        max_bytes: FileSize = None,
        code_length: int = None,
        extension: bool = None,
        custom_code: str = None
    ) -> str:
        """Uploads a file-like object using the raw binary data
        provided.
        Returns the URL of the uploaded file.
        
        Attributes
        -----------
        filepath - The raw binary data associated with the file.
               Using `io.BytesIO` is recommended.
            
        filetype - The file type associated with the file
                   you're uploading. I.E., ".png".

        max_bytes - A maximum number of bytes uploadable. Use
                    the Size class to specify the number of bytes. 
        
        code_length - The length of the unique code to generate.
                      Must be between 5 and 50 characters.

        extension - If `False`, this will not append the file type
                    at the end of the file.
        
        custom_code - The custom file name which will be displayed on
                      wants-to.party.
        """ 
        return await AsyncRequest._post_from_bytes(
            file,
            filetype,
            data=self.data,
            url_args={"max_bytes": max_bytes, "code_length": code_length, "custom_code": custom_code, "extension": extension},
            max_bytes=max_bytes
        )
    
    async def upload_from_file(
        self,
        filepath: str,
        *,
        max_bytes: FileSize = None,
        code_length: int = None,
        extension: bool = None,
        custom_code: str = None
    ) -> str:
        """Uploads a local file using the file path provided.
        
        Returns the URL of the uploaded file.
        
        Attributes
        -----------
        file - The path to the file stored on your local disk.
        
        max_bytes - A maximum number of bytes uploadable. Use
        the Size class to specify the number of bytes. 
        
        code_length - The length of the unique code to generate.
                      Must be between 5 and 50 characters.

        extension - If `False`, this will not append the file type
                    at the end of the file.
        
        custom_code - The custom file name which will be displayed on
                      wants-to.party.
        """
        filedata = pathlib.Path(filepath)
        
        filetype = filedata.suffix
        path = os.path.abspath(filepath)
        
        return await AsyncRequest._post_from_file(
            path,
            filetype,
            data=self.data,
            url_args={"max_bytes": max_bytes, "code_length": code_length, "custom_code": custom_code, "extension": extension},
            max_bytes=max_bytes
        )
    
    async def delete_file(self, file_id: str) -> bool:
        """Deletes a file on wants-to.party with the given ID and filetype.
        
        NOTE: you MUST include the filetype! (I.E., ".mp3")"""
        return await AsyncRequest._delete_file(file_id, data=self.data)

    async def get_files(self) -> list:
        """Returns a list of file objects relating to your files on wants-to.party
        or `None` if there's no files.
        
        As per a wants-to.party limitation, this only shows the first 1000 files."""
        return await AsyncRequest._get_files(data=self.data)
    
    async def get_user(self) -> User:
        """Returns a user object of the user associated with the given API key."""
        return await AsyncRequest._get_user(data=self.data)