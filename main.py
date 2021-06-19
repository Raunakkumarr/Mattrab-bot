import os
import discord
import random
from PIL import Image, ImageDraw, ImageFont
from keep_alive import keep_alive

my_secret = os.environ['BOT_Token']    #This is your secret bot token.
bgImage = Image.open("welcome-bg.jpg")
title_font = ImageFont.truetype('playfair/playfair-font.ttf', 150)
welcome_font = ImageFont.truetype('playfair/playfair-font.ttf', 75)

intents = discord.Intents().default()
intents.members = True

botCmd = discord.Client(intents=intents)

statusList = [
    "with Mattrab", "with Mattrab Notes", "with Mattrab Chapters", "with Mattrab Questions", "with Mattrab Profiles", "with Mattrab on Facebook", "with Mattrab on Instagram", "with Mattrab on Linkedin", "with Mattrab on YouTube"]

greetingsList = ["hi all", "hello all", "hey all", "hello everyone", "hi everyone", "hey eveyone", "hey there"]

welcomeList = ["Welcome to Mattrab Community's Server.", 'Hope you brought Pizza!', 'Best wishes for your journey at Mattrab!', 'Glad to see you!', 'Yay you made it!', 'Everyone Welcome', "Let's Welcome", "Glad you're here"]

sadWords = ["i'm sad" , "i'm dismal","i'm heartbroken" , "i'm mournful","i'm somber","i'm sorrowful", "i'm cheerless","i'm dejected","i'm hurt" ,"i'm grieved", "i'm down","i'm distressed", "i'm gloomy", "i'm low", "i'm depressed", "i'm angsty","i'm awful","i'm melancholy","i'm dejected","i'm agony","i'm broken","i'm pathetic","i'm hopeless","i'm bummer","i'm moody","i'm sorrow","i'm stressed","i'm torn", "i am sad" ,"i am dismal","i am heartbroken", "i am mournful", "i am somber","i am sorrowful", "i am cheerless","i am dejected","i am hurt" ,"i am grieved", "i am down","i am distressed", "i am gloomy", "i am low", "i am depressed", "i am angsty","i am awful","i am melancholy","i am dejected","i am agony","i am broken","i am pathetic","i am hopeless","i am bummer","i am moody","i am in sorrow","i am stressed","i am torn", "i'm in stress", "i am in stress", "i'm tired", "i am tired", "i'm disregarded", "i am disregarded", "i'm frustrated", "i am frustrated", "i'm a loser", "i am a loser", "im loser", "i m loser", "i'm loser", "i am loser"]

inspirationalQoutes = ['Cheer Up!', 'You are the best!!', "I guess you're confident, so cheer up!", "You got this!, Chin up!!!", "Hey, Cherish yourself!", "Forget of others, I know you're amazing so just cheer up!", "Hey, you have all that it takes to rule yourself", "You're intellectual.", "You're a explorer, just explore yourself.", "You're imaginative, impressive and enthusiastic, we all know!", "Your hardwork and devotion makes us proud, just keep going.","If you fear diving, you'll never get to the precious pearl that you're seeking for.... So Come on lets explore together to that depth so as to seek the precious pearl of wisdom."]

@botCmd.event
async def on_ready():
  print("Mattrab's Bot has logged in. Bot Name is {0.user}".format(botCmd))

@botCmd.event
async def on_member_join(member):
    guild = botCmd.get_guild(852558834253692956)
    channel = guild.get_channel(852558834735513672)
    member_name = member.name
    memberAvatar = member.avatar_url
    member_num = str(guild.member_count)
    title_text = member_name
    imgEditable = ImageDraw.Draw(bgImage)
    imgEditable.text((50,400), "Welcome to Mattrab Community's Server", (0, 0, 255), font=welcome_font)
    imgEditable.text((150,650), title_text, (0, 255, 0), font=title_font)
    imgEditable.text((525,850), "Member #"+member_num, (255,0,0), font=welcome_font)
    fileName = "new-"+member_name+member_num+".jpg"
    bgImage.save(fileName)
    file = discord.File(fileName)
    welcome_msg = random.choice(welcomeList)+" "+f"{member.mention}"
    await channel.send(welcome_msg, file=file)
    print(member_name)
    print(memberAvatar)

@botCmd.event
async def on_message(message):
    if message.author == botCmd.user:
        return
    msg = message.content
    if msg.startswith('&changeActivity'):
        customActivity = random.choice(statusList)
        await botCmd.change_presence(activity=discord.Streaming(
            name=customActivity, url="https://www.askmattrab.com/"))
        await message.channel.send('Activity Changed!')

    if any(word in msg.lower() for word in greetingsList):
        await message.channel.send("Hello!, Hope you're enjoying at Mattrab!!")

    if any(word in msg.lower() for word in sadWords):
        await message.channel.send(random.choice(inspirationalQoutes))

    if msg.startswith('&sad'):
        await message.channel.send(random.choice(inspirationalQoutes))
    
    if msg.startswith('&help'):
        help_msg = discord.Embed(title="Mattrab's Bot User Guide", description="In order to use the bot, please go through the user manual first.", color=0x00ff00)
        help_msg.add_field(name="Link to User Manual",value="https://www.raunakmishra.com.np/mattrab-bot/docs.html", inline=False)
        help_msg.set_author(name="Raunak Kumar", url="https://www.raunakmishra.com.np/#Contact", icon_url="https://www.raunakmishra.com.np/signature.png")
        help_msg.set_thumbnail(url="https://www.raunakmishra.com.np/mattrab-bot/Stay%20%40%20Home.png")
        help_msg.set_footer(text="Information requested by: {}".format(message.author.display_name))
        await message.channel.send(embed=help_msg)

keep_alive()
botCmd.run(my_secret)
