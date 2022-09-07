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