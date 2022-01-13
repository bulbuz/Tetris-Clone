import pygame

from config import *

class Figure(object):
    def __init__(self, game, figure_type, x, y, rotation=0):
        self.figs = {
            'L': {
                'color': ORANGE,
                'rotations': [[
                    [0, 0, 0],
                    [0, 0, 1],
                    [1, 1, 1],
                ],
                [
                    [1, 0, 0],
                    [1, 0, 0],
                    [1, 1, 0],
                ],
                [
                    [1, 1, 1],
                    [1, 0, 0],
                    [0, 0, 0],
                ],
                [
                    [0, 1, 1],
                    [0, 0, 1],
                    [0, 0, 1],
                ]]
            },
            'S': {
                'color': GREEN,
                'rotations': [
                [
                    [0, 0, 0],
                    [0, 1, 1],
                    [1, 1, 0],
                ],
                [
                    [1, 0, 0],
                    [1, 1, 0],
                    [0, 1, 0],
                ],
                [
                    [0, 0, 0],
                    [0, 1, 1],
                    [1, 1, 0],
                ],
                [
                    [1, 0, 0],
                    [1, 1, 0],
                    [0, 1, 0],
                ]]

            },
            'I': {
                'color': TURQUOISE,
                'rotations': [
                [
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [1, 1, 1, 1],
                    [0, 0, 0, 0],
                ],
                [
                    [0, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 0, 0],
                ],
                [
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [1, 1, 1, 1],
                    [0, 0, 0, 0],
                ],
                [
                    [0, 0, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 0],
                ]]
            },
            'J': {
                'color': BLUE,
                'rotations' : [
                [
                    [0, 0, 0],
                    [1, 0, 0],
                    [1, 1, 1]
                ],
                [
                    [1, 1, 0], 
                    [1, 0, 0], 
                    [1, 0, 0]
                ],
                [
                    [1, 1, 1],
                    [0, 0, 1],
                    [0, 0, 0]
                ],
                [
                    [0, 0, 1],
                    [0, 0, 1],
                    [0, 1, 1]
                ]]

            },
            'Z': {
                'color': RED,
                'rotations': [
                [
                    [0, 0, 0],
                    [1, 1, 0],
                    [0, 1, 1]
                ],
                [
                    [0, 1, 0],
                    [1, 1, 0],
                    [1, 0, 0]
                ],
                [
                    [0, 0, 0],
                    [1, 1, 0],
                    [0, 1, 1]
                ],
                [
                    [0, 1, 0],
                    [1, 1, 0],
                    [1, 0, 0]
                ]]
            }, 
            'T': {
                'color': PURPLE,
                'rotations': [
                [
                    [0, 0, 0],
                    [0, 1, 0],
                    [1, 1, 1]
                ],
                [
                    [1, 0, 0],
                    [1, 1, 0],
                    [1, 0, 0]
                ],
                [
                    [1, 1, 1],
                    [0, 1, 0],
                    [0, 0, 0]
                ],
                [
                    [0, 0, 1],
                    [0, 1, 1],
                    [0, 0, 1]
                ]]
            }
        }
        self.figure = self.figs.get(figure_type)
        self.game = game
        self.x = x
        self.y = y

    def draw(self):
        for i in range(len(self.figure['rotations'][self.game.rotation])):
            for j in range(len(self.figure['rotations'][self.game.rotation][i])):
                if self.figure['rotations'][self.game.rotation][i][j] == 1:
                    rect = [(self.x+j)*TILE_SIZE, (self.y+i-2)*TILE_SIZE, TILE_SIZE, TILE_SIZE]
                    pygame.draw.rect(self.game.game_display, self.figure['color'], rect)
                    pygame.draw.rect(self.game.game_display, WHITE, rect, 1)

