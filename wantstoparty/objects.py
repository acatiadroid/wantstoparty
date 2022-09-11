import requests
from typing import Union
from aiohttp import ClientSession

from .errors import MaxFileSizeExceeded

class SizeLimit:
    """A class that defines a maximum file size for a file.
    
    This transforms B, KB & MB units into the no. of bytes specified.
    
    To specify the maximum number of bytes, use the kwargs.
    If the maximum file size is exceeded, the MaxFileSizeExceeded exception is raised.
    
    GB+ units not necessary due to wants-to.party's maximum allowed file size of 100MB."""
    def __init__(
        self,
        *,
        mb: float = None,
        kb: float = None,
        b:  float = None
        ):
        self.mb: Union[float, bool] = mb
        self.kb: Union[float, bool] = kb
        self.b:  Union[float, bool] = b

        self.exceeded: bool = False
    
    def _check_bytes(self, all_bytes: int) -> None:
        nbytes = 1024
        b = 0
        kb = 0
        mb = 0

        if self.mb:
            mb = self.mb * (nbytes ** 2)
        
        if self.kb:
            kb = self.kb * (nbytes ** 1)
        
        if self.b:
            b = self.b
        
        total_allowed_bytes = mb + kb + b

        if all_bytes > total_allowed_bytes: # file exceeded max allowed filesize
            self.exceeded = True
            raise MaxFileSizeExceeded("This file exceeded the maximum file size limit.")

class FileSize:
    KBSIZE = 1024
    MBSIZE = 1048576 # in bytes
    def __init__(self, _total: int):
        self._total = _total
    
    def __str__(self) -> str:
        count = self.formatted_bytes
        fmt = f"{count['mb']}MB, {count['kb']}KB, {count['b']}B"
        return str(fmt)

    @property
    def total_bytes(self) -> int:
        """The number of bytes present in the file."""
        return self._total

    @property
    def total_kb(self) -> int:
        """The number of kilobytes present in the file."""
        return self._total / self.KBSIZE
    
    @property
    def total_mb(self) -> int:
        """The number of megabytes present in the file."""
        return (self._total / self.KBSIZE) / self.KBSIZE
    
    @property
    def formatted_bytes(self) -> dict:
        """The number of MB, KB & B in the file.

        This counts bytes in order of largest unit to smallest. (MB to B)
        If the sum bytes is less than 1 MB, it will calculate number of KB's instead (and so on).

        This method factors in sizes that are on the boundary of the next unit (I.E, 1024 B = 1 KB)

        For example:
        1586230 B -> 1 MB, 525 KB, 54 B"""
        temp = self._total

        mb = 0
        kb = 0
        b = 0

        while temp > 0:
            if temp >= 1048576:
                mb += 1
                temp = temp - 1048576
            elif temp >= 1024:
                kb += 1
                temp = temp - 1024
            else:
                b = temp
                temp = 0
            
        return {"mb": mb, "kb": kb, "b": b}


class User:
    """Represents a wants-to.party user."""
    def __init__(self, data: dict):
        self.data = data

    def __str__(self) -> str:
        return str(self.data.get("user_id"))

    @property
    def user_id(self) -> int:
        """The users ID.
        
        If you're using an oauth session, this is only accessible with the `user.read` scope.
        If you're using your user API key, the `user.read` scope is not necessary."""
        return self.data.get("user_id")
    
    @property
    def userid(self) -> int:
        """(An alias for the user_id property) 
        The users ID.
        
        If you're using an oauth session, this is only accessible with the `user.read` scope.
        If you're using your user API key, the `user.read` scope is not necessary."""
        return self.data.get("user_id")

    @property
    def user_name(self) -> str:
        """The users name.
        
        If you're using an oauth session, this is only accessible with the `user.read` scope.
        If you're using your user API key, the `user.read` scope is not necessary."""
        return self.data.get("user_name")

    @property
    def username(self) -> str:
        """(An alias for the user_name property)
        The users name.
        
        If you're using an oauth session, this is only accessible with the `user.read` scope.
        If you're using your user API key, the `user.read` scope is not necessary."""
        return self.data.get("user_name")

    @property
    def email(self) -> str:
        """The users email.
        
        If you're using an oauth session, this is only accessible with the `user.email` scope.
        If you're using your user API key, the `user.email` scope is not necessary."""
        return self.data.get("email")
    
class File:
    """Represents a wants-to.party file."""
    def __init__(self, data: dict):
        self.data = data

    def __str__(self) -> str:
        return str(self.data.get("url"))

    @property
    def name(self) -> str:
        """The filename and filetype."""
        return self.data.get("name")

    @property
    def extension(self) -> str:
        """The file extension. (does not include the ".")"""
        return self.data.get("extension")

    @property
    def filename(self) -> str:
        """The filename only."""
        return self.data.get("filename")

    @property
    def uploaded_at(self) -> int:
        """The Unix timestamp for when the file was created."""
        return self.data.get("uploaded_at")

    @property
    def url(self) -> str:
        """The full usable URL of the file."""
        return self.data.get("url")

    @classmethod    
    def get_size(self, file_id: str, subdomain: str) -> FileSize:
        """Returns a `FileSize` object  a hosted files' size.
        
        Attributes
        -----------
        file_id - The file ID and filetype of the hosted file.

        subdomain - The the subdomain which the file is hosted with.
        """
        url = f"https://{subdomain}.wants-to.party/{file_id}"

        bcount = requests.get(url, stream=True).headers['Content-Length']

        return FileSize(bcount)
    
    @classmethod
    async def async_get_size(self, file_id: str, subdomain: str) -> FileSize:
        """A non-blocking method that returns a `FileSize` object  a hosted files' size.
        
        Attributes
        -----------
        file_id - The file ID and filetype of the hosted file.

        subdomain - The the subdomain which the file is hosted with.
        """
        url = f"https://{subdomain}.wants-to.party/{file_id}"

        async with ClientSession() as s:
            async with s.get(url) as resp:
                bcount = len(await resp.read())
        
        return FileSize(bcount)