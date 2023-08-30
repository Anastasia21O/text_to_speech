from io import BytesIO

import pygame
from gtts import gTTS

pygame.init()


def say(text):
    tts = gTTS(text=text, lang='uk')
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


mytext = "Привіт, хочу тобі допомогти!"
say(mytext)

# mytext1 = "Звукова доріжка №2!"
# audio = gTTS(text=mytext1, lang="uk")
# audio.save("example.mp3")
# os.system("start example.mp3")

