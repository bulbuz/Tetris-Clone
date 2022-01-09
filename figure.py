import pygame

from config import *

class Figure(object):

    figures = {
        'L': {
            'color': ORANGE,
            'rotations': [[
                [0, 0, 0],
                [0, 0, 1],
                [1, 1, 1],
            ],
            [
                [0, 1, 1],
                [0, 0, 1],
                [0, 0, 1],
            ],
            [
                [1, 1, 1],
                [1, 0, 0],
                [0, 0, 0],
            ],
            [
                [1, 0, 0],
                [1, 0, 0],
                [1, 1, 0],
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
            ]]

        },
        'I': {
            'color': TURQUOISE,
            'rotations': [
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 1, 1, 1],
            ],
            [
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
            ],
            [
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
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
            'color': GREEN,
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
            ]]
        }, 
        'T': {
            'color': GREEN,
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


    def __init__(self, figure_type, x, y):
        self.figure = figures.get(figure_type)

    def draw(self):
        pass

