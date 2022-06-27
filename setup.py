from setuptools import find_packages, setup

VERSION = "0.0.1"
DESCRIPTION = "An API wrapper for the wants-to.party API."
LONG_DESC = """An API wrapper for the wants-to.party API which provides 
full API coverage. This wrapper also lets you make API calls asynchronously and
synchronously"""

setup(
    name="wantstoparty",
    version=VERSION,
    author="acatiadroid",
    author_email="<acatia@mail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESC,
    packages=find_packages(),
    requires=["aiohttp", "requests"],
    keywords=["python", "api wrapper"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)