import sys
import time
import pygame
import check
from pygame.locals import *


def text_in(screen, text, realtime, COLOR, txt_font, txt_size):
    w, h = screen.get_width(), screen.get_height()
    FADE_EASING = lambda x: x  # Linear
    pygame.key.set_mods(0)  # HACK: work-a-round for a SDL bug??
    font = pygame.font.SysFont(txt_font, txt_size, True)
    bg = 10, 10, 10
    text = font.render(text, True, (COLOR), bg)
    text_rect = text.get_rect(center=(w / 2, h / 2))

    for i in range(0, 255):
        rendered_text = text
        surf2 = pygame.surface.Surface((text_rect.width, text_rect.height))
        alpha = FADE_EASING(i)
        surf2.set_alpha(alpha)
        screen.fill(bg)
        surf2.blit(rendered_text, (0, 0))
        screen.blit(surf2, text_rect)
        pygame.display.flip()
        check.for_quit()
        time.sleep(realtime/256)


def text_out(screen, text, realtime, COLOR, txt_font, txt_size):
    w, h = screen.get_width(), screen.get_height()
    FADE_EASING = lambda x: x  # Linear
    pygame.key.set_mods(0)  # HACK: work-a-round for a SDL bug??
    font = pygame.font.SysFont(txt_font, txt_size, True)
    bg = 10, 10, 10
    text = font.render(text, True, (COLOR), bg)
    text_rect = text.get_rect(center=(w / 2, h / 2))

    for i in range(0, 255):
        rendered_text = text
        surf2 = pygame.surface.Surface((text_rect.width, text_rect.height))
        alpha = FADE_EASING(255-i)
        surf2.set_alpha(alpha)
        screen.fill(bg)
        surf2.blit(rendered_text, (0, 0))
        screen.blit(surf2, text_rect)
        pygame.display.flip()
        check.for_quit()
        time.sleep(realtime/256)


def background_in(screen, realtime, COLOR):
    w, h = screen.get_width(), screen.get_height()
    FADE_EASING = lambda x: x  # Linear
    pygame.key.set_mods(0)  # HACK: work-a-round for a SDL bug??
    bg = 10, 10, 10

    for i in range(0, 255):
        surf2 = pygame.surface.Surface((w, h))
        alpha = FADE_EASING(i)
        surf2.set_alpha(alpha)
        screen.fill(bg)
        surf2.fill(COLOR)
        screen.blit(surf2, (0, 0))
        pygame.display.flip()
        check.for_quit()
        time.sleep(realtime/256)


def logo(screen, COLOR, realtime):
    w, h = screen.get_width(), screen.get_height()
    FADE_EASING = lambda x: x  # Linear
    pygame.key.set_mods(0)  # HACK: work-a-round for a SDL bug??
    bg = 10, 10, 10

    for i in range(0, 255):
        surf2 = pygame.surface.Surface((w, h))
        alpha = FADE_EASING(i)
        surf2.set_alpha(alpha)
        screen.fill(COLOR)
        surf2.fill(bg)
        logo = pygame.image.load("images/logo.png")
        logo_loc = logo.get_rect(center=(w / 2, h / 2))
        screen.blit(logo, logo_loc)
        screen.blit(surf2, (0, 0))


        pygame.display.flip()
        check.for_quit()
        time.sleep(realtime / 256)


def logo_text(screen, text, realtime, COLOR, txt_font, txt_size):
    w, h = screen.get_width(), screen.get_height()
    FADE_EASING = lambda x: x  # Linear
    pygame.key.set_mods(0)  # HACK: work-a-round for a SDL bug??
    font = pygame.font.SysFont(txt_font, txt_size, True)
    bg = 10, 10, 10
    text = font.render(text, True, (COLOR), bg)
    text_rect = text.get_rect(center=(w / 2, h / 1.5))

    for i in range(0, 255):
        rendered_text = text
        surf2 = pygame.surface.Surface((text_rect.width, text_rect.height))
        alpha = FADE_EASING(i)
        surf2.set_alpha(alpha)
        screen.fill(bg)
        surf2.blit(rendered_text, (0, 0))
        screen.blit(surf2, text_rect)
        logo = pygame.image.load("images/logo.png")
        logo_loc = logo.get_rect(center=(w / 2, h / 2))
        screen.blit(logo, logo_loc)
        pygame.display.flip()
        check.for_quit()
        time.sleep(realtime/256)