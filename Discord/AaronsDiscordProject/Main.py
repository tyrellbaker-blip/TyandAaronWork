import os
from dotenv import load_dotenv
import sqlite3
from discord.ext import commands
import discord

load_dotenv()
TOKEN = os.getenv('TY_TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
bot.db_conn = sqlite3.connect("mymatchmaking.db")
bot.db_curs = bot.db_conn.cursor()


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    bot.db_curs.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, points INTEGER)")




@bot.command(name='register')
async def register(ctx, username: str):
    print(f"Trying to register user: {username}")  # Print statement for debugging
    try:
        bot.db_curs.execute("INSERT INTO users VALUES (?, 0)", (username,))
        bot.db_conn.commit()
        print(f"User {username} registered successfully.")  # Success message
        await ctx.send(f"User {username} registered successfully.")
    except sqlite3.IntegrityError:
        print(f"Failed to register user: {username}. Username already exists.")  # Failure message
        await ctx.send(f"Failed to register user: {username}. Username already exists.")

@bot.command(name='allusers')
async def view_registered(ctx):
    bot.db_curs.execute("SELECT username FROM users")
    users = bot.db_curs.fetchall()

    if not users:
        await ctx.send("No users in database")
        return
    user_names = ', '.join(user[0] for user in users)
    await ctx.send(f"Registered users: {user_names}")

@bot.command(name='points')
async def points(ctx, username: str):
    bot.db_curs.execute("SELECT points FROM users WHERE username=?", (username,))
    user = self.bot.db_curs.fetchone()

    if user is None:
        await ctx.send("User not registered.")
    else:
        await ctx.send(f"{username} has {user[1]} points.")


bot.run(TOKEN)
