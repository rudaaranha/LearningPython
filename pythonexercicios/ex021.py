#Ex021 - Faça um programa de python que abra e reproduza o áudio de um arquivo .mp3.
import pygame
print('Este programa reproduz um áudio de um arquivo .mp3.')
pygame.init()
pygame.mixer.music.load('ex021aceofspades.mp3')
pygame.mixer.music.play()
pygame.event.wait()
