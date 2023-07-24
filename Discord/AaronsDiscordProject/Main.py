import os
import random
import time

from dotenv import load_dotenv
import sqlite3
from discord.ext import commands
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
bot.db_conn = sqlite3.connect("mymatchmaking.db")
bot.db_curs = bot.db_conn.cursor()


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    bot.db_curs.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, points INTEGER, consecutive_misses INTEGER)")





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
    user = bot.db_curs.fetchone()

    if user is None:
        await ctx.send("User not registered.")
    else:
        await ctx.send(f"{username} has {user[1]} points.")
@bot.command(name= 'newmatchup')
async def newmatchup(ctx):
    bot.db_curs.execute("SELECT username FROM users")
    allusers = [row[0]for row in bot.db_curs.fetchall()]
    if len(allusers)< 2:
        await ctx.send("There aren't enough users for a match.")
        return
    user_1, user_2 = random.sample(allusers, 2)


    print(f'Matchup: {user_1} vs {user_2}')
    await ctx.send(f'Matchup: {user_1} vs {user_2}')


def owner_mediation(ctx, opponent, outcome):
    pass


async def update_points_and_notify(ctx, discord_id, points):
    bot.db_curs.execute('UPDATE users SET points = points + ? WHERE discord_id=?', (points, discord_id))
    bot.db_conn.commit()
    bot.db_curs.execute('SELECT points FROM users WHERE discord_id=?', (discord_id))
    update_points = bot.db_curs.fetchone()[0]
    await ctx.send(f'Your points have been updated. You now have {update_points}.')


def kick_inactive_users(ctx, winner, loser):
    pass


def remind_player_to_submit_report(ctx, winner, loser, winner_consecutive_misses, loser_consecutive_misses):
    pass

def handle_losing_streak(ctx, discord_id, outcome):
    bot.db_curs.execute('SELECT points, consecutive_misses FROM users WHERE discord_id=?', (discord_id))
    user_info = bot.db_curs.fetchone()
    points, consecutive_misses = user_info


@bot.command(name= 'confirm')
async def confirm(ctx, opponent: discord.Member, outcome: str):
    if outcome not in ['win', 'lose']:
        await ctx.send('Invalid response: Please enter win or lose.')
        return

    report = bot.match_reports.get(str(opponent.id))
    if report and report['opponent'] == str(ctx.message.author.id) and report['outcome'] != outcome:
        await owner_mediation(ctx, ctx.message.author, opponent, outcome)
        return

    winner, loser = (str(ctx.message.author.id), str(opponent.id)) if outcome == 'win' else (str(opponent.id), str(ctx.message.author.id))

    bot.db_curs.execute('SELECT consecutive_losses FROM users WHERE discord_id=?', (loser,))
    loser_consecutive_losses = bot.db_curs.fetchone()[0]
    if loser_consecutive_losses >= 5:
        change_points(winner, 40)
    else:
        change_points(winner, 23)
    change_points(loser, -15)

    bot.db_curs.execute('UPDATE users SET consecutive_losses = consecutive_losses + 1 WHERE discord_id=?', (loser,))
    bot.db_curs.execute('UPDATE users SET consecutive_losses = 0 WHERE discord_id=?', (winner,))

@bot.command(name='checkmisseddeadlines')
@commands.is_owner()
async def check_missed_deadlines(ctx):
    current_time = time.time()
    for user_id, report in bot.match_reports.items():
        if current_time - report['created'] >= 2 * 24 * 60 * 60:
            bot.db_curs.execute('SELECT consecutive_misses FROM users WHERE discord_id=?', (user_id,))
            misses = bot.db_curs.fetchone()[0]

            if misses >= 8:
                bot.db_curs.execute('DELETE FROM users WHERE discord_id=?', (user_id,))
                bot.db_conn.commit()
                await ctx.send(f'{bot.get_user(int(user_id))} has been removed from the server due to inactivity.')
                continue

            bot.db_curs.execute('UPDATE users SET consecutive_misses = consecutive_misses + 1 WHERE discord_id=?', (user_id,))
            bot.db_conn.commit()
            change_points(user_id, -5)

def main():
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
