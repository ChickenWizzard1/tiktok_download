import argparse
import asyncio
import subprocess
from TikTokLive import TikTokLiveClient

async def check_live(username):
    client = TikTokLiveClient(f"@{username}")

    while True:
        if await client.is_live():
            print(f"{username} ist live! Führe Befehl aus...")
            subprocess.run(f"python main.py -user {username}", shell=True)  # <--- Hier anpassen!
            break

        print(f"{username} ist nicht live - erneute Prüfung in 30 Sekunden.")
        await asyncio.sleep(30)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prüft, ob ein TikTok-User live ist und führt dann einen Shell-Befehl aus.")
    parser.add_argument("-user", "--user", required=True, help="TikTok Username (ohne @)")
    args = parser.parse_args()

    asyncio.run(check_live(args.user))

