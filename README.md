# botdoc

A cog for discord.py that automatically generates markdown documentation for your bot's cogs and commands.

## How to use

### If your bot has cogs

Clone the repo into your cogs folder

```
git clone
```

Add `cogs.botdoc.botdoc` to your cogs array:
```py
cogs = [ ..., 'cogs.embed_help.help']
```

### If your bot doesn't have cogs

Create a directory called `cogs` in your project and clone
```
git clone
```

Create a list called `cogs` like this:
```py
cogs = ['cogs.embed_help.help']
```

Then in your `on_ready` method load the cogs:
```py
@bot.event
async def on_ready():
    # Your existing stuff
    for cog in cogs:
        bot.load_extension(cog)
```

### Once its setup

Each time your bot is loaded and the cogs are loaded, the documentation is automatically generated in a directory called `docs`.