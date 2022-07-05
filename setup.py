from setuptools import find_packages, setup

VERSION = "0.1.0"
DESCRIPTION = "An API wrapper for the wants-to.party API."

long_desc = ""
with open(".github/README.md", "r") as f:
    long_desc = f.read()

setup(
    name="wantstoparty",
    version=VERSION,
    author="acatiadroid",
    author_email="<acatia@mail.com>",
    url="https://github.com/acatiadroid/wantstoparty",
    description=DESCRIPTION,
    long_description=long_desc,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["docs", "examples", "build", "dist", "*.egg-info"]),
    install_requires=["aiohttp", "requests"],
    keywords=["python", "api wrapper"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)