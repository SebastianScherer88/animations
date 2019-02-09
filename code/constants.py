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
WALKING = 'walking'
STANDING = 'standing'
PUNCHING = 'punching'

# pygame window settings
WINDOW_HEIGHT = 400 # height of pygame window
WINDOW_WIDTH = 400 # width of pygame window

# pygame color settings
WHITE = (255,255,255)

# pygame speed setting
CLOCK_SPEED = 10 # frames per second
VEL_X = 5 # frames per second velocity of animated sprite on x axis
VEL_y = 5 # frames per second velocity of animated sprite on y axis

# animation sequences
NINJA_IMAGE_PATHS = ["../image/ninja/" + image_name for image_name in os.listdir("../image/ninja")]
NINJA_IMAGES_RIGHT = list(map(pg.image.load,NINJA_IMAGE_PATHS))
NINJA_IMAGES_LEFT = [pg.transform.flip(ninja_image,True,False) for ninja_image in NINJA_IMAGES_RIGHT]
NINJA_ANIMATIONS = {WALKING:{LEFT: NINJA_IMAGES_LEFT,
                          RIGHT: NINJA_IMAGES_RIGHT},
                    STANDING:{LEFT: NINJA_IMAGES_LEFT,
                          RIGHT: NINJA_IMAGES_RIGHT}
                    }
                    
WALK_IMAGE_PATHS = ["../image/the_walk/" + image_name for image_name in os.listdir("../image/the_walk") if image_name[-4:] == ".png"]
WALK_IMAGES_RIGHT = list(map(pg.image.load,WALK_IMAGE_PATHS))
WALK_IMAGES_LEFT = [pg.transform.flip(walk_image,True,False) for walk_image in WALK_IMAGES_RIGHT]

PUNCH_IMAGE_PATHS = ["../image/the_punch/" + image_name for image_name in os.listdir("../image/the_punch") if image_name[-4:] == ".png"]
PUNCH_IMAGES_RIGHT = list(map(pg.image.load,PUNCH_IMAGE_PATHS))
PUNCH_IMAGES_LEFT = [pg.transform.flip(punch_image,True,False) for punch_image in PUNCH_IMAGES_RIGHT]

STICK_ANIMATIONS = {WALKING:{LEFT: WALK_IMAGES_LEFT[:8],
                            RIGHT: WALK_IMAGES_RIGHT[:8]},
                    STANDING:{LEFT: [WALK_IMAGES_LEFT[8]],
                              RIGHT: [WALK_IMAGES_RIGHT[8]]},
                    PUNCHING:{LEFT: PUNCH_IMAGES_LEFT,
                              RIGHT: PUNCH_IMAGES_RIGHT}
                    }