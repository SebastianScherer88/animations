# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 20:36:10 2019

@author: bettmensch
"""

from pygame.sprite import Sprite as Sprite

class GameSprite(Sprite):
    
    def __init__(self,
                 *groups, # list of spite groups the sprite will be added to when initialized
                 image_sequences, # dictionary of image sequences defining animation sequences
                 x = 0,
                 y = 0,
                 vel_x = 0,
                 vel_y = 0
                 ):
        
        # base class initializer
        Sprite.__init__(self,
                        *groups)
        
        # animation attributes
        self._image_sequences = image_sequences
        
        # positional attributes
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
    