from discord.ext import commands


class Points(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def points(self, ctx, username: str):
        self.bot.db_curs.execute("SELECT points FROM users WHERE username=?", (username,))
        user = self.bot.db_curs.fetchone()

        if user is None:
            await ctx.send("User not registered.")
        else:
            await ctx.send(f"{username} has {user[1]} points.")


def setup(bot):
    bot.add_cog(Points(bot))
