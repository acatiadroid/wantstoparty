# wantstoparty

**wantstoparty** is a feature-rich API wrapper for the [wants-to.party](https://wants-to.party) API which provides full API coverage, supporting blocking/non-blocking HTTP methods and much more.

## Index
* [API reference](wantstoparty.rst)
* [Getting started/Installation](gettingstarted.md)
* [Examples](examples.md)

### Notable features
* Blocking (sync) and non-blocking (async) support. [`blocking example`](https://github.com/acatiadroid/wantstoparty/blob/main/examples/nonasync_use.py) [`non-blocking example`](https://github.com/acatiadroid/wantstoparty/blob/main/examples/async_use.py)
* Upload files by providing a local file path. (I.E, file stored on disk) or bytes-like file object. (see examples above)
* Get all files hosted on your wants-to.party account.
* Get account information associated with the given API key.
* Delete files by their given file ID.
* Set a maximum uploadable file size limit.
    - Prevents files that exceed your specified limit being uploaded. [`see example`](https://github.com/acatiadroid/wantstoparty/blob/main/examples/max_filesize.py)
* Validation for unsupported file types.
* User-friendly errors for handling status codes of failed HTTP requests.

**Created by acatia#5378**

### License
This project is licensed under MIT. Read the license [here](https://github.com/acatiadroid/py-wants-to-party/blob/main/LICENSE.txt).
