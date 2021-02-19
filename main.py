import time
from instabot import Bot
import random

bot = Bot()
totalArchivedPost = 0
PostToArchive = 0

IGUSERNAME = input("insert your Instagram account USERNAME: ")
IGPASSWORD = input("insert your Instagram account PASSWORD: ")

bot.login(username = IGUSERNAME, password = IGPASSWORD)

PostToArchive = input("insert number of post you want to ARCHIVE: ")
PostToArchive = int(PostToArchive)
print("fetching...")
medias = bot.get_total_user_medias(bot.user_id)

for PostToArchive in medias:
    try:
        bot.archive(PostToArchive)
        print("archived")
        totalArchivedPost =+ 1         
        time.sleep(random.randint(5, 15))
    except:
        print("error")
        time.sleep(random.randint(200, 400))

print("total archived post: " + str(totalArchivedPost))