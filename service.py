from io import BytesIO

import pygame
from gtts import gTTS


# import os


def say(text: str):
    tts = gTTS(text=text, lang='uk')
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def bytesSpeach(text: str):
    audio = gTTS(text=text, lang="uk")
    fp = BytesIO()
    audio.write_to_fp(fp)
    fp.seek(0)
    return str(fp.getvalue())


def file(text: str):
    file_name = "example.mp3"
    audio = gTTS(text=text, lang="uk")
    audio.save(file_name)

    # Запустити mp3
    # os.system("start example.mp3")

    # витягнути байти
    # data = open(file_name, 'rb').read()

    return file_name
