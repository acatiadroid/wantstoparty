# Getting started

### Prerequisites
For using this package, please ensure you have the following installed:
* Python >=3.8
* Pip (for installation/upgrading)
* A [wants-to.party](https://wants-to.party) account

### Installation
Firstly, to use this package you'll need to install it. The package is hosted on PyPi so installation is very simple.

To install the **stable** wantstoparty release, run:
```pip install wantstoparty```

To install the **development** release, run:
```pip install -U git+https://github.com/acatiadroid/wantstoparty```

Alternately, `git clone` the package.

### Using wantstoparty
1. On your [wants-to.party](https://wants-to.party) dashboard, click "View api key":
    
    ![img](https://user-images.githubusercontent.com/69216256/180094711-f3428246-e369-440f-84d7-d9eba7a9d8bc.png)

2. Import the WantsToParty class:
    ```py
    from wantstoparty import WantsToParty

    # For async use, refer to the examples.
    wtp = WantsToParty("api key from dashboard")
    ```

3. All done. If this executes without errors then you're ready to go!. Check out the examples [here](examples.md).