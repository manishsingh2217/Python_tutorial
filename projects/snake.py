import pygame
import random 
import time

pygame.init()
red=(255,0,0)
blue=(51,153,255)
grey=(192,192,192)
green=(51,102,0)

win_width= 600
win_height = 400

window=pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Snake game")

snake=10  #snake size
snake_speed=15

font_style = pygame.font.SysFont("calibri",26)
score_font = pygame.font.SysFont("comicsansms",30)


# def user_score():
    
# fonts = pygame.font.get_fonts()
# print(fonts)