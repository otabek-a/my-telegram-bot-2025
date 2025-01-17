# Get toke from the environment variable
import os
from telegram import Bot
token = os.environ['TOKEN']


CHAT_ID = os.environ['chat_id']
bot = Bot(token,CHAT_ID)


video_url = 'https://www.w3schools.com/html/movie.mp4'
response = bot.send_video(CHAT_ID, video_url, 'hey, it is my own bot!')
print(response)




audio = bot.send_audio(CHAT_ID, "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
print(audio)




dacument=bot.send_document(CHAT_ID,"https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf")
print(dacument)


message=bot.send_message(CHAT_ID,'SAlom')
print(message)


audio = bot.send_audio(CHAT_ID, "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
print(audio)



photo=bot.send_photo(CHAT_ID)
print(photo)




updates = bot.get_updates()
update = updates['result'][-1]
#text = update.message.text
print(update)