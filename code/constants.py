# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 21:15:38 2019

@author: bettmensch
"""

import pygame as pg
import os

# sprite constants
LEFT = 'left'
RIGHT = 'right'

# pygame window settings
WINDOW_HEIGHT = 400 # height of pygame window
WINDOW_WIDTH = 400 # width of pygame window

# pygame color settings
WHITE = (255,255,255)

# pygame speed setting
CLOCK_SPEED = 5 # frames per second
VEL_X = 5 # frames per second velocity of animated sprite on x axis
VEL_y = 5 # frames per second velocity of animated sprite on y axis

# animation sequences
NINJA_IMAGE_PATHS = ["../image/ninja/" + image_name for image_name in os.listdir("../image/ninja")]
NINJA_IMAGES_RIGHT = list(map(pg.image.load,NINJA_IMAGE_PATHS))
NINJA_IMAGES_LEFT = [pg.transform.flip(ninja_image,True,False) for ninja_image in NINJA_IMAGES_RIGHT]
NINJA_ANIMATIONS = {True:{LEFT: NINJA_IMAGES_LEFT,
                          RIGHT: NINJA_IMAGES_RIGHT},
                    False:{LEFT: NINJA_IMAGES_LEFT,
                          RIGHT: NINJA_IMAGES_RIGHT}
                    }