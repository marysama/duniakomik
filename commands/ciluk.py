import hikari
import lightbulb

plugin = lightbulb.Plugin('ciluk')


@plugin.command
@lightbulb.command('ciluk', 'coba dijawab apacik?')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Baaaaaaa!')

def load(bot):
    bot.add_plugin(plugin)