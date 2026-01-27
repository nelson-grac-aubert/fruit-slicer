# game_screen.py

import pygame
from game_classes import GameState
from gameplay_loop import spawn_fruit, update_all_objects, draw_all_fruits
from game_assets import load_image
from sound_control import button_music_click, button_sound_click, load_music_images, load_sound_images

# Tu peux importer ton background ici aussi


def game_screen(screen, clock):
    """ Game Screen """

    background = load_image("assets/images/background.png")

    game_state = GameState()
    spawn_cooldown = 0

    # Sound buttons
    music_muted = False
    sound_muted = False
    music_img, music_muted_img, music_rect = load_music_images()
    sound_img, sound_muted_img, sound_rect = load_sound_images()

    while True:

        # DRAW BACKGROUND
        screen.blit(background, (0, 0))

        # UPDATE FRUITS
        update_all_objects(game_state)

        # DRAW FRUITS
        draw_all_fruits(screen)

        # SPAWN FRUITS
        spawn_cooldown += 1
        if spawn_cooldown >= 60:
            spawn_fruit()
            spawn_cooldown = 0

        # EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Sound buttons
            music_muted = button_music_click(event, music_rect, music_muted)
            sound_muted = button_sound_click(event, sound_rect, sound_muted)

        # DRAW SOUND BUTTONS
        screen.blit(music_muted_img if music_muted else music_img, music_rect)
        screen.blit(sound_muted_img if sound_muted else sound_img, sound_rect)

        pygame.display.flip()
        clock.tick(60)