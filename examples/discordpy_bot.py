import io
from discord.ext import commands

# Using async so we don't stop the event loop (blocking)
from wantstoparty._async import WantsToParty

bot = commands.Bot(command_prefix="???") # intents, etc not relevant for demo
wtp = WantsToParty(api_key="your api key", subdomain="your subdomain")

@bot.command()
async def upload(ctx: commands.Context):
    """Uploads all files provided when running this command."""
    for attachment in ctx.message.attachments:
        extension = attachment.filename.split(".")
        extension = extension[len(extension)-1]     # the file extension. I.E., "png"

        file_data = io.BytesIO(await attachment.read()) # store bytes in BytesIO
        file = await wtp.upload_from_bytes(file_data, extension)
    
        await ctx.send(f'<{file}>')


bot.run("token")
