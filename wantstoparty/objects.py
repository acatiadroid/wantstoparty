from typing import Optional, Union

from .errors import MaxFileSizeExceeded

class Size:
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
        b:  float = None,
        _total: int = None
        ):
        self.mb: Union[float, bool] = mb
        self.kb: Union[float, bool] = kb
        self.b:  Union[float, bool] = b

        self.total: Optional[int] = None
        self.exceeded: bool = False
    
    def _get_bytes_size(self):
        """Internal method for calculating total number of bytes."""
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
        
        self.total = mb + kb + b
    
    @staticmethod
    def _get_hosted_size(file):
        

    def _check_bytes(self, all_bytes: int) -> None:
        """Internal method for validation of file size."""
        self._get_bytes_size()
        
        if all_bytes > self.total: # file exceeded max allowed filesize
            self.exceeded = True
            raise MaxFileSizeExceeded("This file exceeded the maximum file size limit.")


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
    def get_size(self):
        pass

        