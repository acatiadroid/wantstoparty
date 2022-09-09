import os
import requests
from aiohttp import ClientSession, FormData

from .errors import BadRequest, _handle_errorcode
from .utils import _format_arguments
from .objects import File, SizeLimit, User

class URL:
    BASE = "https://wants-to.party"
    def __init__(self, path: str, args: dict = None):
        self.path = path
        self.args = args

    def _assemble_url(self):
        args = _format_arguments(self.args) if self.args else ""

        return self.BASE + self.path + args

class Request:
    def _post_from_file(
        file,
        filetype: str,
        *,
        data: dict,
        url_args: dict = None,
        max_bytes: SizeLimit = None
    ):
        key = data.get("key")
        headers = {"Authorization": f"User {key}"}

        if max_bytes:
            max_bytes._check_bytes(os.path.getsize(file))
        
        file_data = open(file, "rb")

        file = {"file": ("file" + filetype, file_data)}

        resp = requests.post(
            URL("/api/user/files", url_args)._assemble_url(),
            headers=headers,
            files=file
        )
        payload = resp.json()

        if resp.status_code != 200:
            return _handle_errorcode(resp.status_code, payload["message"])
        
        return payload["url"]
    
    def _post_from_bytes(
        file,
        filetype: str,
        *,
        data: dict,
        url_args: dict = None,
        max_bytes: SizeLimit = None
    ):
        key = data.get("key")
        headers = {"Authorization": f"User {key}"}

        if max_bytes:
            max_bytes._check_bytes(file.getbuffer().nbytes)
        
        if not filetype.endswith("."):
            filetype = "." + filetype

        filename = f"file{filetype}"

        file = {"file": (filename, file.getvalue())}

        resp = requests.post(
            URL("/api/user/files", url_args)._assemble_url(),
            headers=headers,
            files=file
        )

        payload = resp.json()

        if resp.status_code != 200:
            return _handle_errorcode(resp.status_code, payload["message"])
        
        return payload["url"]

    def _get_user(data: dict):
        key = data.get("key")
        headers = {"Authorization": f"User {key}"}
        resp = requests.get(
            URL("/api/user")._assemble_url(),
            headers=headers
        )
        
        payload = resp.json()

        if resp.status_code != 200:
            return _handle_errorcode(resp.status_code, payload["message"])
        
        return User(payload)
    
    def _get_files(data: dict):
        key = data.get("key")
        headers = {"Authorization": f"User {key}"}
        resp = requests.get(
            URL("/api/user/files")._assemble_url(),
            headers=headers
        )

        payload = resp.json()

        if resp.status_code != 200:
            return _handle_errorcode(resp.status_code, payload["message"])

        files = payload["files"]

        if not files:
            return None
            
        new_files = []
        for file in files:
            new_files.append(File(file))

        return new_files

    def _delete_file(file_id: str, data: dict):
        key = data.get("key")
        headers = {"Authorization": f"User {key}"}
        resp = requests.delete(
            URL(f"/api/user/files/{file_id}")._assemble_url(),
            headers=headers
        )

        payload = resp.json()

        if payload["message"] == "ok":    # lord forgive me
            return True
        
        raise BadRequest("That file does not exist.") # just gonna raise 400 even though its 404.

class AsyncRequest:
    async def _post_from_file(
        file,
        filetype: str,
        *,
        data: dict,
        url_args: dict = None,
        max_bytes: SizeLimit = None
    ):
        key = data.get("key")
        headers = {"Authorization": f"User {key}"}

        if max_bytes:
            max_bytes._check_bytes(os.path.getsize(file))
        
        form = FormData()
        form.add_field("file", open(file, "rb").read(), filename="file" + filetype)
    
        async with ClientSession(headers=headers) as s:
            async with s.post(URL("/api/user/files", url_args)._assemble_url(), data=form) as resp:
                payload = await resp.json()
                
            if resp.status != 200:
                return _handle_errorcode(resp.status, payload["message"])

            return payload["url"]
    
    async def _post_from_bytes(
        file,
        filetype: str,
        *,
        data: dict,
        url_args: dict = None,
        max_bytes: SizeLimit = None
    ):
        key = data.get("key")
        headers = {"Authorization": f"User {key}"}

        if max_bytes:
            max_bytes._check_bytes(file.getbuffer().nbytes)
        
        form = FormData(quote_fields=False)
        filename = f"file{filetype}"
        form.add_field("file", file.getvalue(), filename=filename)
    
        async with ClientSession(headers=headers) as s:
            async with s.post(URL("/api/user/files", url_args)._assemble_url(), data=form) as resp:
                payload = await resp.json()
                
            if resp.status != 200:
                return _handle_errorcode(resp.status, payload["message"])

            return payload["url"]
        
    
    async def _get_user(data: dict):
        key = data.get("key")
        headers = {"Authorization": f"User {key}"}
        async with ClientSession(headers=headers) as s:
            async with s.get(URL("/api/user")._assemble_url()) as resp:
                payload = await resp.json()
                
            if resp.status != 200:
                return _handle_errorcode(resp.status, payload["message"])
            
            return User(payload)
    
    async def _get_files(data: dict):
        key = data.get("key")
        headers = {"Authorization": f"User {key}"}
        async with ClientSession(headers=headers) as s:
            async with s.get(URL("/api/user/files")._assemble_url()) as resp:
                payload = await resp.json()
                
            if resp.status != 200:
                return _handle_errorcode(resp.status, payload["message"])
        
        files = payload["files"]

        if not files:
            return None

        new_files = []
        for file in files:
            new_files.append(File(file))

        return new_files
    
    async def _delete_file(file_id: str, data: dict):
        key = data.get("key")
        headers = {"Authorization": f"User {key}"}
        async with ClientSession(headers=headers) as s:
            async with s.delete(URL(f"/api/user/files/{file_id}")._assemble_url()) as resp:
                payload = await resp.json()
                
            if resp.status != 200:
                return _handle_errorcode(resp.status, payload["message"])
        
            return True
