import pygame
from pygame.locals import *
import engine
import fade
import time


def start():
    pygame.init()

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
    color = 255, 255, 255
    fade.text_in(screen, "Pong", 0.03, (color), 'Calibri', 160)
    time.sleep(0.1)
    fade.text_out(screen, "Pong", 0.01, (color), 'Calibri', 160)
    time.sleep(0.2)
    app = engine.Main(screen)
    app.tick()

if __name__ == "__main__":
    start()

