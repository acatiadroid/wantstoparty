from wantstoparty import WantsToParty
import io

wtp = WantsToParty(api_key="your api key", subdomain="your subdomain")

# upload from local file on disk using path to file.
file = wtp.upload_from_file("cat.png")

# upload from binary data
my_html = io.BytesIO(b"<h1>Hello world</h1>")
file = wtp.upload_from_bytes(my_html, "html") # filetype must be specified as such data isn't
                                       # provided using BytesIO.

# print the usable URL
print(file)