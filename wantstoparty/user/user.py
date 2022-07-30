class UserSession:
    """The base class for all user endpoitns"""
    def __init__(
        self,
        *,
        api_key: str,
        subdomain: str = None
    ):

