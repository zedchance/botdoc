import sys
import os
import discord

if __name__ == '__main__':
    # Check for argv
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]} /absolute/path/to/main.py')
        exit(1)

    # Get filename from argv[1] for bot to evaluate
    filename = sys.argv[1]
    print("Filename:", filename)

    # Import or run the bot somehow

    # Run bot and do similar commands for embed_help to run thru cogs
    # and get items for docs

    # Compile docs

    # Output to .md files

