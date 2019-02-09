# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 21:35:48 2019

@author: bettmensch
"""

import sys
from constants import *
from sprite_class import AnimatedSprite
import pygame as pg
from pygame.sprite import Group

def main():
    # start up pygame
    pg.init()
    
    # create clock for time keeping
    clock = pg.time.Clock()
    
    # create pygame window
    screen = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pg.display.set_caption("animated sprite demo")
    
    # initialize animated sprite
    animated_sprites = Group()
    animated_sprite = AnimatedSprite(animated_sprites,
                                     #image_sequences = NINJA_ANIMATIONS,
                                     #image_sequences = WALK_ANIMATIONS,
                                     image_sequences = STICK_ANIMATIONS,
                                     pos = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2) # put sprite in center of window
                                     )
    
    # initialize quit event
    quit_event = False
    
    # main game loop
    while True:
        # handle events
        events = pg.event.get()
        
        for event in events:
            if event.type == pg.QUIT:                    
                quit_event = True
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                animated_sprite.set_status(PUNCHING) # start punching animation in controlled way
                animated_sprite.vel.x = 0 # set positioning attribute - pnching makes you stop

        if quit_event == True:
            break                    
        
        # if sprite is not punching (has highest priority), check for other keyobard input
        if animated_sprite.status != PUNCHING:
            # handle keys pressed
            keys_pressed = pg.key.get_pressed()
            
            if keys_pressed[pg.K_RIGHT] and not keys_pressed[pg.K_LEFT]:
                animated_sprite.set_status(WALKING) # start walking right animation in controlled way
                animated_sprite.direction = RIGHT # set animation attribute 
                animated_sprite.vel.x = VEL_X # set positioning attribute
            elif keys_pressed[pg.K_LEFT] and not keys_pressed[pg.K_RIGHT]:
                # move left
                if animated_sprite.status != WALKING:
                    animated_sprite.set_status(WALKING) # start walking left animation in controlled way
                animated_sprite.direction = LEFT # set animation attribute
                animated_sprite.vel.x = -VEL_X # set positioning attribute
            elif (keys_pressed[pg.K_LEFT] and keys_pressed[pg.K_RIGHT]) or (not keys_pressed[pg.K_LEFT] and not keys_pressed[pg.K_RIGHT]):
                animated_sprite.set_status(STANDING) # set standing animation in a controlled way
                animated_sprite.vel.x = 0 # set positioning attribute
            
        # update sprite
        animated_sprites.update()
        
        # draw sprite
        screen.fill(WHITE)
        animated_sprites.draw(screen)
        
        # flip canvas
        pg.display.flip()
        
        # control speed
        clock.tick(CLOCK_SPEED)
            
    # quit animation demo
    pg.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()