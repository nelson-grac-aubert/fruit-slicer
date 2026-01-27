# game_screen.py

import pygame
from gameplay_loop import spawn_fruit, update_all_objects, draw_all_fruits
from game_assets import load_image
from sound_control import *
from main_menu_display import draw_image_button, image_button_click


def game_screen(screen, clock, game_state):

    background = load_image("assets/images/background.png")

    spawn_cooldown = 0

    # Sound buttons
    music_muted = False
    sound_muted = False
    music_img, music_muted_img, music_rect = load_music_images()
    sound_img, sound_muted_img, sound_rect = load_sound_images()

    while game_state.state == "GAME":

        # BACKGROUND
        screen.blit(background, (0, 0))

        # SOUND BUTTONS
        draw_music_button(screen, music_muted, music_img, music_muted_img, music_rect)
        draw_sound_button(screen, sound_muted, sound_img, sound_muted_img, sound_rect)

        # BACK BUTTON (PNG)
        back_rect = draw_image_button(
            screen,
            "assets/images/arrow.png",
            position=(80, 80)
        )

        # UPDATE FRUITS
        update_all_objects(game_state)

        # DRAW FRUITS
        draw_all_fruits(screen)

        # SPAWN FRUITS
        spawn_cooldown += 1
        if spawn_cooldown >= 50:
            spawn_fruit()
            spawn_cooldown = 0

        # EVENTS
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Back button
            if image_button_click(event, back_rect):
                game_state.state = "MENU"
                return

            # Sound buttons
            music_muted = button_music_click(event, music_rect, music_muted)
            sound_muted = button_sound_click(event, sound_rect, sound_muted)

        pygame.display.flip()
        clock.tick(60)
