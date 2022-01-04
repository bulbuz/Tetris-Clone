import pygame
import sys

from config import *

class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)


        self.game_display = pygame.Surface((GAME_SURFACE_WIDTH, GAME_SURFACE_HEIGHT))
        self.run = True

    def main(self):
        while self.run:
            self.events()
            self.update()
            self.draw()

            self.clock.tick(FPS)
            pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BLACK)
    
        self.game_display.fill(BLACK)
        # Draws the tetris grid
        for i in range(GAME_DISPLAY_WIDTH):
            for j in range(GAME_DISPLAY_HEIGHT):
                rect = pygame.Rect(i*TILE_SIZE, j*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.game_display, WHITE, rect, 1)

        # Blits the tetris game surface onto the actual surface
        self.screen.blit(pygame.transform.scale(self.game_display, (GAME_SURFACE_WIDTH, GAME_SURFACE_HEIGHT)), ((SCREEN_WIDTH/2)-GAME_SURFACE_WIDTH//2, 10))

if __name__ == "__main__":
    g = Game()
    g.main()
