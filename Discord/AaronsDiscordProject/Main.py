import os
from dotenv import load_dotenv
import sqlite3
from discord.ext import commands
import discord


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_conn = sqlite3.connect('users.db')
        self.db_curs = self.db_conn.cursor()

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        print(f"Received message: {message.content} from {message.author}")
        await self.process_commands(message)


load_dotenv()
intents = discord.Intents.default()
bot = MyBot(command_prefix='!', intents=intents)
bot.load_extension('register')
bot.load_extension('points')
bot.run(os.getenv('TY_TOKEN'))
