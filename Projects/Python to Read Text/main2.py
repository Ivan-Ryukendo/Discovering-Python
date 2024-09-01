from gtts import gTTS

language = "en"
#file = open('read_text.txt', 'r')
#read = file.read()
#file.close()
read = "It's Xzvan"
speech = gTTS(text=read, lang=language, slow=False, tld="com.au")
speech.save("file_quick_readed.mp3")