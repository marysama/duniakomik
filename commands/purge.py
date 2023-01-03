import datetime

import hikari
import lightbulb

purge = lightbulb.Plugin("purge")
purge.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES))


@purge.command()
@lightbulb.add_cooldown(10, 3, lightbulb.UserBucket)
@lightbulb.option(
    "jumlah", "jumlah yang mau di purge", type=int, max_value=100, min_value=1
)
# You may also use pass_options to pass the options directly to the function
@lightbulb.command(
    "purge", "jumlah yang mau di purge", pass_options=True
)
@lightbulb.implements(lightbulb.SlashCommand)
async def _purge(ctx: lightbulb.SlashContext, jumlah: int) -> None:
    if not ctx.guild_id:
        await ctx.respond("Command hanya bisa digunakan di server.")
        return

    # Fetch messages that are not older than 14 days in the channel the command is invoked in
    # Messages older than 14 days cannot be deleted by bots, so this is a necessary precaution
    messages = (
        await ctx.app.rest.fetch_messages(ctx.channel_id)
        .take_until(
            lambda m: datetime.datetime.now(datetime.timezone.utc)
            - datetime.timedelta(days=21)
            > m.created_at
        )
        .limit(jumlah)
    )
    if messages:
        await ctx.app.rest.delete_messages(ctx.channel_id, messages)
        await ctx.respond(f"👍 **{len(messages)}** chat, kehapus!", delete_after=5)
    else:
        await ctx.respond("⚠️ Gabisa dilet lebih dari 21 hari ges!")


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(purge)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(purge)