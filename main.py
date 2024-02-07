import pygame
import sys
import settings

from game import Game
from game_ui import GameUI

pygame.init()
pygame.display.set_caption(settings.WINDOW_NAME)
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
clock = pygame.time.Clock()

game = Game(screen)
game_ui = GameUI(screen, game)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                game_ui.handle_click(event.pos)

    game.update()
    game.draw()
    game_ui.draw()

    pygame.display.flip()
    clock.tick(100)

pygame.quit()
sys.exit()
