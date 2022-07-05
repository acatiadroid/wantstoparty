def validate_file_extension(extension: str):
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