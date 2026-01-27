# game_screen.py

import pygame
from gameplay_loop import spawn_fruit, update_all_objects, draw_all_fruits
from game_assets import load_image
from sound_control import *
from main_menu_display import draw_image_button, image_button_click


def game_screen(screen, clock, game_state, difficulty):

    background = load_image("assets/images/background.png")

    # Diffilcuty settings
    if difficulty == "Easy":
        spawn_rate = 60
    elif difficulty == "Medium":
        spawn_rate = 40
    else:  # Hard
        spawn_rate = 25

    spawn_cooldown = 0

    # Sound buttons
    music_muted = False
    sound_muted = False
    music_img, music_muted_img, music_rect = load_music_images()
    sound_img, sound_muted_img, sound_rect = load_sound_images()

    while game_state.state == "GAME":

        # Backround
        screen.blit(background, (0, 0))

        # Sound buttons
        draw_music_button(screen, music_muted, music_img, music_muted_img, music_rect)
        draw_sound_button(screen, sound_muted, sound_img, sound_muted_img, sound_rect)

        # Back button
        back_rect = draw_image_button(
            screen,
            "assets/images/arrow.png",
            position=(80, 80)
        )

        # Update fruits
        update_all_objects(game_state)

        # Draw fruits
        draw_all_fruits(screen)

        # Spawn fruits (depends on difficulty)
        spawn_cooldown += 1
        if spawn_cooldown >= spawn_rate:
            spawn_fruit()
            spawn_cooldown = 0

        # Events
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
