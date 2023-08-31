import pygame
from fastapi import APIRouter

from service import say, bytesSpeach, file

router = APIRouter(tags=["text_to_speach"])


@router.get("/say")
def text_to_speach_say(text: str):
    pygame.init()
    say(text)


@router.get("/bytes")
def text_to_speach_bytes(text: str):
    return bytesSpeach(text)


@router.get("/file")
def text_to_speach_file(text: str):
    return file(text)
