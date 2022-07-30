<div align="center">
    <h1>wantstoparty</h1>
    <h3>An API wrapper for the <a href="https://wants-to.party">wants-to.party</a> API.</h3>
    <img src="https://img.shields.io/pypi/v/wantstoparty.svg">
    <h3>V2 is out! Check out the changes <a href=".github/whats_new.md">here</a>.</h3>

</div>

## About
`wantstoparty` is a feature rich API wrapper for the wants-to.party API which offers:
* Blocking and non-blocking (async) support. [See blocking example](https://github.com/acatiadroid/wantstoparty/blob/main/examples/nonasync_use.py)/[See non-blocking example](https://github.com/acatiadroid/wantstoparty/blob/main/examples/async_use.py).
* Upload files using raw binary data or a local file stored on disk. Look at the examples above.
* Set a maximum upload file size.
    - This prevents files that exceed your limit being uploaded. [See example](https://github.com/acatiadroid/wantstoparty/blob/main/examples/max_filesize.py).
* Check if file types are supported on wants-to.party.
* User-friendly errors.
* ...and much more.

**Created by acatia#5378**

## Getting started
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
    wtp = WantsToParty(api_key="api key from dashboard")
    ```


Join the Motion Development server for extra help, [here](https://discord.gg/9x566fY47Z).

## Examples
Some examples can be found in the [examples/](https://github.com/acatiadroid/py-wants-to-party/tree/main/examples) folder.

## Contributing
Contributions are welcome! Check out the [contributing guidelines](https://github.com/acatiadroid/py-wants-to-party/blob/main/.github/CONTRIBUTING.md) beforehand.

## License
This is licensed under MIT. Read the license [here](https://github.com/acatiadroid/py-wants-to-party/blob/main/LICENSE.txt).
