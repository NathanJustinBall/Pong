import pygame
from pygame.locals import *
import check
import startup


pygame.init()
clock = pygame.time.Clock()
pygame.display.init()

screen_data = pygame.display.Info()
SW, SH = screen_data.current_w, screen_data.current_h
new = pygame.display.set_mode((SW,SH))

screen = pygame.display.get_surface()
tmp = screen.convert()
caption = pygame.display.get_caption()
cursor = pygame.mouse.get_cursor()
w, h = screen.get_width(), screen.get_height()
flags = screen.get_flags()
bits = screen.get_bitsize()

screen = pygame.display.set_mode((w, h), flags ^ FULLSCREEN, bits)

pygame.display.set_caption(*caption)

pygame.mouse.set_visible(0)
startup.start(screen)

while True:
    check.for_quit()

