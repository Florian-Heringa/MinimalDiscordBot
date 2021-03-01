from discord import Embed
from discord.ext import commands

from constants import HELP_EMBED_COLOR

class baseHelp(commands.MinimalHelpCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Takes care of rendering the help message as a Discord embed instead of a code block
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = Embed(description=page, color=HELP_EMBED_COLOR)
            await destination.send(embed=emby)

    # Change command signature in help message to take custom usage message instead of default function signature.
    def get_command_signature(self, command):
        return f'**{self.clean_prefix}{command.qualified_name}** *{command.usage}*'
        # equivalent to f"{self.clean_prefix}{command.qualified_name} {command.signature}"

    async def send_cog_help(self, cog):
        bot = self.context.bot
        if bot.description:
            self.paginator.add_line(bot.description, empty=True)

        note = self.get_opening_note()
        if note:
            self.paginator.add_line(note, empty=True)

        if cog.description:
            self.paginator.add_line(note, empty=True)

        filtered = await self.filter_commands(cog.get_commands(), sort=self.sort_commands)
        if filtered:
            self.paginator.add_line(f'**{cog.qualified_name} {self.commands_heading}**')
            for command in filtered:
                self.add_subcommand_formatting(command)

            note = self.get_ending_note()
            if note:
                self.paginator.add_line()
                self.paginator.add_line(note)

        await self.send_pages()

    def get_ending_note(self):
        return ""

    def add_subcommand_formatting(self, command):
        fmt = '**{0}{1}** \N{EN DASH} {2}' if command.short_doc else '{0}{1}'
        self.paginator.add_line(fmt.format(self.clean_prefix, command.qualified_name, command.short_doc))
        