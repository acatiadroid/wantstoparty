<div align="center">
    <h1>wantstoparty</h1>
    <h3>An API wrapper for the <a href="https://wants-to.party">wants-to.party</a> API.</h3>
    <img src="https://img.shields.io/pypi/v/wantstoparty.svg">
</div>

## About
**wantstoparty** is a feature-rich API wrapper for the [wants-to.party](https://wants-to.party) API which provides full API coverage, supporting blocking/non-blocking HTTP methods and much more.

Notable features:
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

## Installation & Setup
1. Install the package:
    ```
    pip install wantstoparty
    ```
2. Create a [wants-to.party](https://wants-to.party) account.
3. On your dashboard, click the "View api key" button:

    ![image](https://user-images.githubusercontent.com/69216256/180094711-f3428246-e369-440f-84d7-d9eba7a9d8bc.png)

4. Import the `WantsToParty` class:
    ```py
    from wantstoparty import WantsToParty

    # For async use, refer to the examples.
    wtp = WantsToParty("api key from dashboard")
    ```


Join the Motion Development server for extra help, [here](https://discord.gg/9x566fY47Z).

## Examples
Some examples can be found in the [examples/](https://github.com/acatiadroid/py-wants-to-party/tree/main/examples) folder.

## Contributing
Contributions are welcome! Check out the [contributing guidelines](https://github.com/acatiadroid/py-wants-to-party/blob/main/.github/CONTRIBUTING.md) beforehand.

## License
This is licensed under MIT. Read the license [here](https://github.com/acatiadroid/py-wants-to-party/blob/main/LICENSE.txt).
