# What's new

## V2.0.1 - V2.0.3 (9 September 2022)
* Added `get_size()`/`async_get_size()` (sync & async) methods to `File` object.
* Renamed `Size` class to `SizeLimit` (used in setting max bytes)
* Added `FileSize` class which is returned when calling the get_size methods.
    - These classes act as a blueprint to the filesize and give you more information than just the sum total bytes (I.E., units like MB andKB.)
* Improved README.

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