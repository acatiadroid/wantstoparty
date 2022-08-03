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
        