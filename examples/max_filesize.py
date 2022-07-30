# This is a pre-upload check that let's you specify a limit to how
# many bytes can be uploaded.
#
# This is useful if you have a system which let's uploads user-inputted files.
# I.E., a form which lets a user upload an image.

from wantstoparty import WantsToParty, Size, MaxFileSizeExceeded

wtp = WantsToParty("your api key")

try:
    wtp.upload_from_file("cat.png", max_bytes=Size(mb=3)) # Alternately use the kb or b kwargs.
except MaxFileSizeExceeded:
    print("woah there that file is too big buddy")