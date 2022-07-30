from typing import Union

from .errors import MaxFileSizeExceeded

def validate_file_extension(extension: str) -> bool:
    """Returns `True` if the file extension provided is allowed 
    on wants-to.party.
    
    Allowed file extensions are:
    png, jpg, gif, mp4, mp3, json, txt, js, html, css, py

    Note that different variations of the same filetype don't work.
    E.G., "jpeg" won't work."""
    if extension.startswith("."):
        extension = extension.replace(".", "")

    allowed = [
        "png",
        "jpg",
        "gif",
        "mp4",
        "mp3",
        "json",
        "txt",
        "js",
        "html",
        "css",
        "py"
    ]
    
    if extension in allowed:
        return True
    
    return False

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

def _format_arguments(data: dict):
    final = []

    if data.get("max_length"):
        final.append("max_length=" + data["max_length"])
    
    if data.get("custom_code"):
        final.append("custom_code=" + data["custom_code"])
    
    if data.get("code_length"):
        final.append("code_length=" + data["code_length"])
    
    if data.get("extension") != None:
        final.append("extension=" + str(data["extension"]))
    
    arguments = "&".join(final)

    return f"?{arguments}"