import pygame

def createSound(file):
    return pygame.mixer.Sound(file)

def play(sound, volume = 50):
    sound.set_volume(volume)
    sound.play()

def stop(sound):
    sound.stop()
