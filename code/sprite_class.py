# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 20:36:10 2019

@author: bettmensch
"""

from pygame.sprite import Sprite as Sprite
from pygame.math import Vector2 as Vector
from constants import *

class AnimatedSprite(Sprite):
    
    def __init__(self,
                 *groups, # list of spite groups the sprite will be added to when initialized
                 image_sequences, # dictionary of image sequences defining animation sequences
                 pos = (0,0), # 2-dim position vector in pixels
                 vel = (0,0), # 2-dim velocity  vector in pixels/frame
                 direction = LEFT, # sprite faces right unless specified differently
                 status = STANDING # sprite not moving unless specified differently
                 ):
        
        # base class initializer
        Sprite.__init__(self,
                        *groups)
        
        # --- animation attributes
        
        # orientation
        assert(direction in [LEFT,RIGHT])
        self.direction = direction
        
        # state of movement
        assert(status in [STANDING,WALKING,PUNCHING])
        self.status = status
        
        # animations
        self.image_sequences = image_sequences
        self.current_image_sequence = image_sequences[status][direction]
        self.image_index = 0
        self.image = self.current_image_sequence[self.image_index]
        self.rect = self.image.get_rect()
        
        # positional attributes
        self.pos = Vector(int(pos[0]),int(pos[1])) # position needs to be integers because of pixels
        self.vel = Vector(vel[0],vel[1]) # velocity can be decimals
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        
        print([self.image_sequences[key].keys() for key in self.image_sequences.keys()])
                
    def update(self):
        # moves the sprite around
        self.pos.x = int(self.pos.x + self.vel.x) # x coordinate update
        self.pos.y = int(self.pos.y + self.vel.y) # y coordinate update
        
        # update animation image sequence based on current attributes
        self.current_image_sequence = self.image_sequences[self.status][self.direction]
        
        # move on to next image in current animation sequence
        sequence_length = len(self.current_image_sequence)
        
        if self.status in [STANDING,WALKING]:
            # for looping animations, just increase the image index modulo animation sequence length
            self.image_index = (self.image_index + 1) % sequence_length
        elif self.status == PUNCHING:
            # for non-looping animation: if end is reached, set index to 0 and reset to default status
            if self.image_index == (sequence_length - 1):
                self.set_status(STANDING)
            elif self.image_index < (sequence_length - 1):
                self.image_index += 1
            
        self.image = self.current_image_sequence[self.image_index]
        
        # update position attributes for new image
        self.rect = self.image.get_rect()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        
        return
    
    def set_status(self,
                   new_status,
                   reset = True):
        '''Method to be called when the sprite's animation sequence needs to be changed/updated.
        In particular, when game events / keyboard input affects the animation sequence, this method
        allows for better control.'''
        
        # only change and reset if the new status is different to the current one
        if reset and (new_status != self.status):
            self.image_index = 0
            self.status = new_status
            
        return
        
    