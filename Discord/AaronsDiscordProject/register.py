from discord.ext import commands
import sqlite3


class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def register(self, ctx, username: str):
        print(f"Trying to register user: {username}")  # Print statement for debugging
        try:
            self.bot.db_curs.execute("INSERT INTO users VALUES (?, 0)", (username,))
            self.bot.db_conn.commit()
            print(f"User {username} registered successfully.")  # Success message
            await ctx.send(f"User {username} registered successfully.")
        except sqlite3.IntegrityError:
            print(f"Failed to register user: {username}. Username already exists.")  # Failure message
            await ctx.send(f"Failed to register user: {username}. Username already exists.")


def setup(bot):
    bot.add_cog(Register(bot))