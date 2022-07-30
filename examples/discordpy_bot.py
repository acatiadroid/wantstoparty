import io
from discord.ext import commands

# Using async so we don't stop the event loop (blocking)
from wantstoparty._async import WantsToParty, Size, MaxFileSizeExceeded

bot = commands.Bot(command_prefix="???") # intents, etc not relevant for demo
wtp = WantsToParty("your api key")

@bot.command()
async def upload(ctx: commands.Context):
    """Uploads all files provided when running this command."""
    for attachment in ctx.message.attachments:
        extension = attachment.filename.split(".")
        extension = extension[len(extension)-1]     # the file extension. I.E., "png"

        file_data = io.BytesIO(await attachment.read()) # store bytes in BytesIO
        
        try:                                                                      # VVVVVVVVVVVVV basically 6MB.
            file = await wtp.upload_from_bytes(file_data, extension, max_bytes=Size(mb=5, kb=1024))
        except MaxFileSizeExceeded:
            return await ctx.send("That file is bigger than 6MB. Too big!")

        await ctx.send(f'<{file}>')


bot.run("token")
