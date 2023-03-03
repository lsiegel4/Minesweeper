"""Attempting to Create Minesweeper using pygame!"""

__author__ = "Lucas Siegel"

import pygame
import sys


pygame.init()

screen = pygame.display.set_mode([650, 800])

clock = pygame.time.Clock()

running = True

rect: pygame.Rect = pygame.Rect(20, 20, 25, 25)

while running:
    clock.tick(60)

    screen.fill((120, 200, 255))

    i: int = 0
    j: int = 0
    while i <= 650:
        pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 650))
        i += 65
    while j <= 650: 
        pygame.draw.line(screen, (0, 0, 0), (0, j), (650, j))
        j += 65

    rect.x = pygame.mouse.get_pos()[0] - 10
    rect.y = pygame.mouse.get_pos()[1] - 10

    pygame.draw.rect(screen, (200, 200, 200), rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pygame.draw.rect(screen, (100, 100, 100), rect)
        
    pygame.display.flip()

pygame.quit()