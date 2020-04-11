# botdoc
# Documentation generating cog for discord.py

import sys
import os
import discord
from discord.ext import commands


def _h(num, text):
    """ Returns a h1-h6 string """
    header = ''
    for i in range(num):
        header += '#'
    return f'{header} {text}\n\n'


def _text(text):
    """ Returns normal text string """
    return f'{text}\n\n'


def _code_block(text):
    """ Returns a code block string """
    return f'```\n{text}\n```\n\n'


def _inline_code(text):
    """ Returns an inline code string """
    return f'`{text}`'


def _generate_usage(bot, command_name):
    """ Generates a string of how to use a command """
    if command_name is None:
        return "command_name is None"
    temp = f'!b'  # TODO
    command = bot.get_command(command_name)
    # Aliases
    if len(command.aliases) == 0:
        temp += f'{command_name}'
    elif len(command.aliases) == 1:
        temp += f'[{command.name}|{command.aliases[0]}]'
    else:
        t = '|'.join(command.aliases)
        temp += f'[{command.name}|{t}]'
    # Parameters
    params = f' '
    for param in command.clean_params:
        params += f'<{command.clean_params[param]}> '
    temp += f'{params}'
    return temp


def _generate_cog_docs(bot):
    """ Generates a file of documentation for a cog """
    # Make docs dir
    cwd = os.path.abspath(os.getcwd())
    out_dir = f'{cwd}/docs'
    os.makedirs(out_dir, exist_ok=True)
    print("Created", out_dir, "directory")

    # Run thru the cogs
    for cog in bot.cogs:
        # Make cog doc file
        out_filename = f'{out_dir}/{cog}.md'
        out = open(out_filename, "w")
        ret = _h(1, cog)
        for command in bot.get_cog(cog).get_commands():
            # Compile docs
            ret += _h(2, _inline_code(command))
            ret += _text(command.help)
            ret += _h(3, "Syntax")
            ret += _text(_inline_code("This is todo"))
            ret += _text("---")
        # Output to file
        out.write(ret)
        ret = ''
        out.close()
        print("Outputted to", out_filename)


class Docs(commands.Cog):
    """ botdoc auto generates documentation for cogs/commands """

    def __init__(self, bot):
        self.bot = bot
        _generate_cog_docs(bot)


# Cog setup
def setup(bot):
    bot.add_cog(Docs(bot))


if __name__ == '__main__':
    print(f'Add cogs.botdoc.botdoc to your cogs list')
    exit(1)
