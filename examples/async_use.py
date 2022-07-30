import asyncio
import io

from wantstoparty._async import WantsToParty

wtp = WantsToParty("your api key")

# Upload using binary data
my_html = io.BytesIO(b"<h1>Hello world</h1>")

async def uploadfile1():
    file = await wtp.upload_from_bytes(my_html, "html")

    print(file)

asyncio.run(uploadfile1())

# Upload using local file
# For this example, we're pretending "cat.png" is stored locally.
async def uploadfile2():
    file = await wtp.upload_from_file("cat.png")

    print(file)

asyncio.run(uploadfile2())
