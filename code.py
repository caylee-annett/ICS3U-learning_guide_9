#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: June 2021
# This is the "Flappy Fish" program on the PyBadge

import ugame
import stage
import random
import time

import constants


#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: June 2021
# This is the "Flappy Fish" program on the PyBadge

import ugame
import stage
import random
import time

import constants


def game_scene():
    # This function is the main game game_scene
   
    def show_pipe():
        # this function takes an pipe from off screen and moves it on screen
        for pipe_number in range(len(pipes)):
            if pipes[pipe_number].x < 0:
                pipes[pipe_number].move(constants.OFF_SCREEN_RIGHT, pipes[pipe_number].y)
                break

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("ocean_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("ocean_sprites.bmp")

    # buttons to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    swoosh_sound = open("swoosh.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # set the background to image 0 in the image bank and the size
    #   to (10x8 tiles of 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)

    # a sprite that will be updated every frame
    fish = stage.Sprite(image_bank_sprites, 1, 20, int(
                        constants.SCREEN_Y / 2 - constants.SPRITE_SIZE / 2))

    # create list of pipes to show up
    pipes = []
    position = random.randint(0, constants.SCREEN_GRID_Y)
    for pipe_number in range(constants.SCREEN_GRID_Y):
        if position < 1:
            if pipe_number > position + 2:
                straight_section = stage.Sprite(image_bank_sprites, 2, constants.SCREEN_X,
                                                pipe_number *
                                                constants.SPRITE_SIZE)
                pipes.append(straight_section)
            elif pipe_number == position + 2:
                bottom_opening = stage.Sprite(image_bank_sprites, 4, constants.SCREEN_X,
                                                pipe_number * constants.SPRITE_SIZE)
                pipes.append(bottom_opening)
        elif position > 7:
            if pipe_number < position - 2:
                straight_section = stage.Sprite(image_bank_sprites, 2, constants.SCREEN_X,
                                                pipe_number *
                                                constants.SPRITE_SIZE)
                pipes.append(straight_section)
            elif pipe_number == position - 2:
                top_opening = stage.Sprite(image_bank_sprites, 3, constants.SCREEN_X,
                                            pipe_number * constants.SPRITE_SIZE)
                pipes.append(top_opening)
        else:
            if pipe_number < position or pipe_number > position + 3:
                straight_section = stage.Sprite(image_bank_sprites, 2, constants.SCREEN_X,
                                                pipe_number *
                                                constants.SPRITE_SIZE)
                pipes.append(straight_section)
            elif pipe_number == position:
                top_opening = stage.Sprite(image_bank_sprites, 3, constants.SCREEN_X,
                                            pipe_number * constants.SPRITE_SIZE)
                pipes.append(top_opening)
            elif pipe_number == position + 3:
                bottom_opening = stage.Sprite(image_bank_sprites, 4, constants.SCREEN_X,
                                                pipe_number * constants.SPRITE_SIZE)
                pipes.append(bottom_opening)
        # place one pipe on the screen
        show_pipe()
    
    # create a stage for the background to show up on and set the frame
    #   rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites
    game.layers = pipes + [fish] + [background]
    # render all sprites
    game.render_block()

    # Repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # A button to flap
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
            # move fish up
            if fish.y >= 0:
                fish.move(fish.x, fish.y - constants.FLAP_SPEED)
            else:
                fish.move(fish.x, 0)
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
            # make fish fall
            if fish.y <= constants.SCREEN_Y - constants.SPRITE_SIZE:
                fish.move(fish.x, fish.y + constants.FALL_SPEED)
            else:
                fish.move(fish.x, constants.SCREEN_Y - constants.SPRITE_SIZE)
        # B button
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            pass
        if keys & ugame.K_LEFT:
            pass
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
        
        # update game logic
        # play sound if A was button_just_pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(swoosh_sound)

        # each frame move the pipes left that are on the screen
        for pipe_number in range(len(pipes)):
            if pipes[pipe_number].y >= 0:
                pipes[pipe_number].move(pipes[pipe_number].x -
                                        constants.PIPE_SPEED, pipes[pipe_number].y)
                if pipes[pipe_number].x < 0 - constants.SPRITE_SIZE:
                    pipes[pipe_number].move(constants.OFF_SCREEN_X,
                                            constants.OFF_SCREEN_Y)
                show_pipe()

        # redraw Sprites
        game.render_sprites([fish] + pipes)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    game_scene()



if __name__ == "__main__":
    game_scene()
