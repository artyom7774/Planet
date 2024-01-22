import pygame


def alpha_rect(screen, width, height, x, y, color):
    surf = pygame.Surface((width, height), pygame.SRCALPHA)
    surf.fill(color)
    screen.blit(surf, (x, y))
