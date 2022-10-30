# from inspect import getframeinfo
# import googletrans
# from googletrans import Translator

# print(googletrans.LANGUAGES)

# text1 = "Hello welcome to my website!"

# translator = Translator()

# print(translator.detect(text1))
# trans1 = translator.translate(text1, src='en', dest='af')
# print("English to Japanese: ", trans1.text)

# print('german/english/japanese/korean/vietnamese')

from gtts import gTTS
tts = gTTS('hello', lang='kr')
tts.save('media/hello.mp3')