import asyncio
import io

from wantstoparty._async import WantsToParty

wtp = WantsToParty(api_key="your api key", subdomain="your subdomain")

# Upload using binary data
html_file = io.BytesIO(b"<h1>Hello world</h1>")

async def uploadfile1():
    await wtp.upload_from_bytes(html_file, "html")

asyncio.run(uploadfile1())

# Upload using local file
# For this example, we're pretending "cat.png" is stored locally.