import hikari
import lightbulb

plugin = lightbulb.Plugin('ping')


@plugin.command
@lightbulb.command('ping', 'ini buat liat pingmu!')
@lightbulb.implements(lightbulb.SlashCommand)
async def _ping(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"PING CHILLING 🥶🍦 \n" f"Pingmu: **{ctx.bot.heartbeat_latency * 1000:.0f}ms**")

def load(bot):
    bot.add_plugin(plugin)