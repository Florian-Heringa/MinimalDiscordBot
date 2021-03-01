# Standard Libraries
import os, sys
import click
import operator
import shutil
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands
from discord import User, Intents

# Custom Libraries
from baseCog import baseCog
from baseHelp import baseHelp

class baseBot(commands.Bot):

    def __init__(self, intents, command_prefix="val_", maintenance_mode=False, *args, **kwargs):
        super().__init__(command_prefix=command_prefix, intents=intents, *args, **kwargs)

        self.maintenance_mode = maintenance_mode
        self.lastBackup = datetime.now()
        
    def write_error(self, log, message):
        with open("err.log", "a") as f:
            f.write(f"{datetime.now()} -- {log}\n")
            f.write(f"\tOriginal message : {message}\n")
            f.write(f"\tMessage Content  : {message.content}\n")

    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')

    async def on_command(self, ctx):
        if self.lastBackup + datetime.timedelta(hours=24) < datetime.now():
            return


##=======================================================

@click.command()
@click.option("--debug", is_flag=True)
@click.option("--maintenance", is_flag=True)
def main(debug, maintenance):
    
    DEBUG = debug
    MAINTENANCE = maintenance        

    # Load environment variables like connection tokens
    # Other environment variables are loaded in utility/constants.py
    load_dotenv()

    if (DEBUG):
        pass
    if (MAINTENANCE):
        pass

    # Enable member intents
    intents = Intents.default()
    intents.members = True

    PREFIX = os.getenv("PREFIX")
    TOKEN = os.getenv("DISCORD_TOKEN")

    # Create bot object
    descr = "Bot desription" 
    bot = baseBot(intents=intents, command_prefix=PREFIX, debug=DEBUG, maintenance_mode=MAINTENANCE, description=descr)

    bot.add_cog(baseCog(bot, baseHelp()))

    # Start bot
    bot.run(TOKEN)


if __name__ == "__main__":
    main()