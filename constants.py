#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: June 2021
# This module contains the constants for the "Flappy Fish"
#    program on the PyBadge

# PyBadge screen size is 160x128 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
FPS = 60
FLAP_SPEED = 2
FALL_SPEED = 1.5
PIPE_SPEED = 3
TOTAL_NUMBER_OF_PIPES = 6
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_SCREEN_RIGHT = SCREEN_X + SPRITE_SIZE
OFF_SCREEN_LEFT = -1 * SPRITE_SIZE
OFF_TOP_SCREEN = -1 * SPRITE_SIZE

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released"
}

# New pallet for red filled text
BLUE_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
