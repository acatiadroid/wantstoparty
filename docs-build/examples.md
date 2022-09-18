# Examples

Here are some minimal examples of what wantstoparty is capable of. There are more examples available on the GitHub repository, [here](https://github.com/acatiadroid/wantstoparty/tree/main/examples).

### Async use
Using the async version is preferred in an asynchronous environment as it does not halt the event loop.
If you're using a Discord bot, use this. [See discord.py bot example](https://github.com/acatiadroid/wantstoparty/blob/main/examples/discordpy_bot.py).
```py
import asyncio
import io

from wantstoparty._async import WantsToParty # importing the async version of WantsToParty.

wtp = WantsToParty("your api key")

# Upload using binary data
my_html = io.BytesIO(b"<h1>Hello world</h1>") # a stream of bytes. For this, we'll use text.

async def uploadfile1():
    file = await wtp.upload_from_bytes(my_html, "html") # running this in an async function.

    print(file)

asyncio.run(uploadfile1()) # execute the async function.
```

### Getting a hosted files' size
This gets a hosted files' size that you've uploaded to wants-to.party.

```py
from wantstoparty import WantsToParty

wtp = WantsToParty("your api key")

files = wtp.get_files() # gets all of your files that you've hosted.

filesize = files[0].get_size() # or async_get_size() for async. - Reads the file size.

print(filesize.formatted_bytes) # the file size in MB, KB and B.
```

### Max file size
This is a pre-upload check that let's you specify how many bytes can be uploaded. This is useful in a system where users input their own files but you want to ensure they don't upload a file that's ridiculously big.
I.E., a form that let's a user upload an image and you want it to be a max size of 5MB.
The `Size` object lets you specify the size. Example:
* `Size(mb=5)`
* `Size(mb=4, kb=512, b=50)`

```py
from wantstoparty import WantsToParty, Size, MaxFileSizeExceeded

wtp = WantsToParty("your api key")

try:
    wtp.upload_from_file("somefile.png", max_bytes=Size(mb=5)) # 5 MB max file size.
except MaxFileSizeExceeded: # uh oh file is too big
    print("woah there that file is too big buddy")
```
