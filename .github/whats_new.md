# What's new

## V2 (30 July 2022)
* Added API coverage for `api/user/files` (`GET`, `POST`, `DELETE`) & `api/user` (`GET`) endpoints:
    - `get_user()`
    - `delete_file()`
    - `upload_from_bytes()`
    - `upload_from_file()`
    - `get_files()`
* Ability to specify URL arguments:
    * `extension` - whether to show the file extension
    * `custom_code` - a custom file URL instead of a randomly generated one
    * `code_length` - the number of random characters generated
* Subdomain is no longer required when instantiating the WantsToParty class.