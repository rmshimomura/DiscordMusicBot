# DiscordMusicBot
A Discord bot because the others are down, made on https://replit.com/

Some things to notice:

- You should have ```youtube_dl```, ```PyNaCl```, ```Flask``` and ```discord.py``` packages installed on your replit. This can be done my clicking on "Packages" button on the left side of the screen

- You need to create an environment variable called 'token'

![secret](https://user-images.githubusercontent.com/65873681/145472822-a5034083-7205-4362-a026-2871084267f4.png)


![token](https://user-images.githubusercontent.com/65873681/145472959-d8b9acc8-e7c1-4c64-af90-786278096e50.png)

- Searches on Youtube if passed argument is not a link (also, this is age restricted bot because of YoutubeDL)

- The prefix is customizable, just change it on:

```py
bot = commands.Bot(command_prefix='!')
```


## Available commands:
- play (p)
- queue (q)
- skip
- pause
- resume
- disconnect (leave)
