import re

from discord import Embed, Role, utils
from discord.ext import commands

from utility import get_message_embed

class baseCog(commands.Cog, name="baseCog"):

    def __init__(self, bot, helpcommand):
        self.bot = bot
        self.__original_help_command = bot.help_command
        bot.help_command = helpcommand
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self.__original_help_command()

    # =============== USER COMMANDS

    @staticmethod
    def has_role(ctx, role):
        coordinator_role = utils.find(lambda r: r.name == role, ctx.guild.roles)
        return coordinator_role in ctx.author.roles

    @staticmethod
    def is_team_member(ctx):
        coordinator_role = utils.find(lambda r: r.name == 'Team', ctx.guild.roles)
        return coordinator_role in ctx.author.roles

    @commands.command('template',
                        aliases = [ 't' , 'tmp' ],
                        help = "Template for bot command",
                        usage = '')
    async def template(self, ctx, *, args):

        user_id = ctx.author.id
        user_name = ctx.author.display_name

        emb = get_message_embed(ctx, f"Called by {user_name}")

        await ctx.send(embed = emb)

    

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        self.bot.write_error(f"{repr(error)}", ctx.message)

        print(error)

        if isinstance(error, commands.errors.CheckFailure):
            await ctx.send("You don't have the permissions to do this")
        elif "ValueError" in repr(error):
            await ctx.send("Arguments incorrectly formatted, check m_help for info")
        elif "BadArgument" in repr(error):
            await ctx.send("Incorrect argument format, check m_help for info")
        else:
            await ctx.send(error)
