import pygame
import sys
from pygame.locals import *


def for_quit():
    for event in pygame.event.get():
        if event.type == pygame.quit:
            print("trying quit")
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("trying quit")
                sys.exit()


def for_control():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("up key pressed")
                return "UP"
            elif event.key == pygame.K_DOWN:
                return "DOWN"
            else:
                return"NONE"


def for_reset():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space key pressed")
                return True
