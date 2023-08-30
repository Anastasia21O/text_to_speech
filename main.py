from io import BytesIO

import pygame
import uvicorn
from fastapi import FastAPI
from gtts import gTTS

# import os
# import pyglet

app = FastAPI()


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


def bytesSpeach(text: str):
    audio = gTTS(text=text, lang="uk")
    fp = BytesIO()
    audio.write_to_fp(fp)
    fp.seek(0)

    return str(fp.getvalue()), fp


def file(text: str):
    file_name = "example.mp3"

    audio = gTTS(text=text, lang="uk")
    audio.save(file_name)
    # os.system("start example.mp3")

    data = open(file_name, 'rb').read()
    return file_name, str(data)


@app.get("/text_to_speach/say")
def text_to_speach_say(text: str):
    pygame.init()
    say(text)


@app.get("/text_to_speach/bytes")
def text_to_speach_bytes(text: str):
    return bytesSpeach(text)


@app.get("/text_to_speach/file")
def text_to_speach_file(text: str):
    return file(text)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        log_level="debug",
        reload=True,
        workers=1,
    )

# test = pyglet.media.load(None, file=fp, streaming=False)
# test.play()
# pyglet.app.run()
