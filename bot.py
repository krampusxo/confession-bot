token = 'tokenhere'
channelid = channelidhere

import discord
bot = discord.Client() 

@bot.event
async def on_message(message):
  if not message.guild:
    await message.author.send(f'Confession posted. <#{channelid}>')
    embed = discord.Embed()
    embed=discord.Embed(description=message.content)
    embed.set_footer(text="dm to confess.")
    await bot.get_channel(channelid).send(embed = embed)
    await bot.change_presence(activity=discord.Streaming(name="DM to confess", url="https://cock.li"))

bot.run(token)