class User:
    """Represents a wants-to.party user."""
    def __init__(self, data: dict):
        self.__user_id = data.get("user_id", False)
        self.__user_name = data.get("user_name", False)
        self.__email = data.get("email", False)

    @property
    def user_id(self):
        """The users ID.
        
        If you're using an oauth session, this is only accessible with the `user.read` scope.
        If you're using your user API key, the `user.read` scope is not necessary."""
        return self.__user_id
    
    @property
    def userid(self):
        """(An alias for the user_id property) 
        The users ID.
        
        If you're using an oauth session, this is only accessible with the `user.read` scope.
        If you're using your user API key, the `user.read` scope is not necessary."""
        return self.__user_id

    @property
    def user_name(self):
        """The users name.
        
        If you're using an oauth session, this is only accessible with the `user.read` scope.
        If you're using your user API key, the `user.read` scope is not necessary."""
        return self.__user_name

    @property
    def username(self):
        """(An alias for the user_name property)
        The users name.
        
        If you're using an oauth session, this is only accessible with the `user.read` scope.
        If you're using your user API key, the `user.read` scope is not necessary."""
        return self.__user_name

    @property
    def email(self):
        """The users email.
        
        If you're using an oauth session, this is only accessible with the `user.email` scope.
        If you're using your user API key, the `user.email` scope is not necessary."""
        return self.__email
    
class File:
    """Represents a wants-to.party file."""
    def __init__(self, data: dict):
        self.__name: str = data.get("name", None)
        self.__extension: str = data.get("extension", None)
        self.__filename: str = data.get("filename", None)
        self.___uploaded_at: int = data.get("uploaded_at", None)
        self.__url: str = data.get("url", None)

    def __str__(self) -> str:
        return str(self.__url)

    @property
    def name(self) -> str:
        """The filename and filetype."""
        return self.__name

    @property
    def extension(self) -> str:
        """The file extension. (does not include the ".")"""
        return self.__extension

    @property
    def filename(self) -> str:
        """The filename only."""
        return self.__filename

    @property
    def uploaded_at(self) -> int:
        """The Unix timestamp for when the file was created."""
        return self.___uploaded_at

    @property
    def url(self) -> str:
        """The full usable URL of the file."""
        return self.__url