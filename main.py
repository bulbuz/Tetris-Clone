import pygame
import sys
import random

from figure import Figure
from config import *

class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)

        self.game_display = pygame.Surface((GAME_SURFACE_WIDTH, GAME_SURFACE_HEIGHT))
        self.run = True
        self.game_grid = [[0] * 10 for i in range(20)]

        self.block_types = ['L', 'S', 'I', 'J', 'Z', 'T']

        self.delay = 900
        self.update_event = pygame.USEREVENT + 0
        self.ok = 1

        self.state = "update"

        self.rotation = 0

        self.current_fig = Figure(self, self.block_types[0], 0, 0)
        self.move_right = False
        self.move_left = False
        self.move_down = False
        self.vel_x = 0
        self.vel_y = 0

        self.rotate = False

    def main(self):
        pygame.time.set_timer(self.update_event, self.delay)
        while self.run:
            self.events()
    
            if self.move_right and self.current_fig.x < 10-len(self.current_fig.figure['rotations'][self.rotation]):
                self.vel_x += 0.12
                self.current_fig.x += round(self.vel_x)
                if round(self.vel_x):
                    self.vel_x = 0

            if self.move_left and self.current_fig.x > 0:
                self.vel_x += 0.12
                self.current_fig.x -= round(self.vel_x)
                if round(self.vel_x):
                    self.vel_x = 0

            if self.move_down:
                self.vel_y += 0.15
                self.current_fig.y += round(self.vel_y)
                if round(self.vel_y):
                    self.vel_y = 0

            if self.ok:
                self.update()
                self.ok = 0
            self.draw()

            self.clock.tick(FPS)
            pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == self.update_event:
                self.ok = 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_left = True

                if event.key == pygame.K_RIGHT:
                    self.move_right = True

                if event.key == pygame.K_DOWN:
                    self.move_down = True

                if event.key == pygame.K_UP:
                    if self.rotation == 3:
                        self.rotation = 0
                    else:
                        self.rotation += 1

                if event.key == pygame.K_SPACE:
                    self.state = 'update'
                    self.ok = 1
                    self.rotation = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.move_left = False

                if event.key == pygame.K_RIGHT:
                    self.move_right = False

                if event.key == pygame.K_DOWN:
                    self.move_down = False

    def update(self):
        if self.state == 'update':
            self.current_fig = Figure(self, random.choice(self.block_types), 4, 0)
            self.state = 'fall'
    
        self.current_fig.y += 1

    def draw(self):
        self.screen.fill(BLACK)
    
        self.game_display.fill(BLACK)

        # Draws the tetris grid
        for i in range(20):
            for j in range(10):
                rect = pygame.Rect(j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.game_display, WHITE, rect, 1)

        self.current_fig.draw()

        # Blits the tetris game surface onto the actual surface
        self.screen.blit(pygame.transform.scale(self.game_display, 
            (GAME_SURFACE_WIDTH, GAME_SURFACE_HEIGHT)), ((SCREEN_WIDTH/2)-GAME_SURFACE_WIDTH//2, 10))

if __name__ == "__main__":
    g = Game()
    g.main()