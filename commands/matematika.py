import hikari
import lightbulb

plugin = lightbulb.Plugin('matematika')

@plugin.command
@lightbulb.command('matematika', 'ini grup matematika')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def matematika(ctx):
    pass


#penjumlahan
@matematika.child
@lightbulb.option('no2', 'pilih nomor keduamu', type=int)
@lightbulb.option('no1', 'pilih nomor pertamamu', type=int)
@lightbulb.command('penjumlahan', 'Tambahkan nomer sesukamu')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def penjumlahan(ctx):
    await ctx.respond(ctx.options.no1 + ctx.options.no2)

#pengurangan
@matematika.child
@lightbulb.option('no2', 'pilih nomor keduamu', type=int)
@lightbulb.option('no1', 'pilih nomor pertamamu', type=int)
@lightbulb.command('pengurangan', 'Kurangi nomer sesukamu')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def pengurangan(ctx):
    await ctx.respond(ctx.options.no1 - ctx.options.no2)

#perkalian
@matematika.child
@lightbulb.option('no2', 'pilih nomor keduamu', type=int)
@lightbulb.option('no1', 'pilih nomor pertamamu', type=int)
@lightbulb.command('perkalian', 'Kalikan nomer sesukamu')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def perkalian(ctx):
    await ctx.respond(ctx.options.no1 * ctx.options.no2)

#pembagian
@matematika.child
@lightbulb.option('no2', 'pilih nomor keduamu', type=int)
@lightbulb.option('no1', 'pilih nomor pertamamu', type=int)
@lightbulb.command('pembagian', 'Bagi nomer sesukamu')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def pembagian(ctx):
    await ctx.respond(ctx.options.no1 / ctx.options.no2)

def load(bot):
    bot.add_plugin(plugin)