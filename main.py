import pygame
import sys

from config import *

class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)


        self.game_display = pygame.Surface((640, 1280))
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
        self.screen.fill((255, 255, 255))

        self.screen.blit(pygame.transform.scale(self.game_display, (320, 640)), (0, 0))

if __name__ == "__main__":
    g = Game()
    g.main()
