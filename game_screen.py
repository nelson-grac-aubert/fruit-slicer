import pygame
from game_classes import GameState
from gameplay_loop import *
from game_assets import load_image
from sound_control import *
from main_menu_display import draw_image_button, back_button_click
from difficulty_settings import DIFFICULTY_SETTINGS

def game_screen(screen, clock, game_state):

    background = load_image("assets/images/background.png")
    frozen_overlay = load_image("assets/images/frozen_state.png")

    spawn_cooldown = 0

    # Sound buttons
    music_muted = False
    sound_muted = False
    music_img, music_muted_img, music_rect = load_music_images()
    sound_img, sound_muted_img, sound_rect = load_sound_images()

    while game_state.state == "GAME":

        # Difficulty 
        settings = DIFFICULTY_SETTINGS[game_state.difficulty]
        spawn_rate = settings["spawn_rate"]

        # Draw UI
        screen.blit(background, (0, 0))
        draw_lives(screen, game_state)
        draw_score(screen, game_state)
        draw_score_popup(screen, game_state)
        draw_music_button(screen, music_muted, music_img, music_muted_img, music_rect)
        draw_sound_button(screen, sound_muted, sound_img, sound_muted_img, sound_rect)
        back_rect = draw_image_button(screen,"assets/images/arrow.png",position=(80, 80))

        # Draw all FlyingObjects
        draw_all_fruits(screen, game_state)

        # Update on each frame
        game_state.freeze_timer -= 1
        if game_state.freeze_timer > 0 : screen.blit(frozen_overlay, (0,0))
        update_all_objects(game_state)

        # Handle game over screen
        if game_state.lives <= 0:
            result = game_over_screen(screen, game_state)

            if result == "RESTART":
                return "RESTART"

            if result == "MENU":
                game_state.state = "MENU"
                return
            
        # Spawn fruits depending on difficulty
        if game_state.freeze_timer < 0 : 
            spawn_cooldown += 1
        if spawn_cooldown >= spawn_rate :
            spawn_item(game_state)
            spawn_cooldown = 0

        # Events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Back button
            if back_button_click(event, back_rect):
                game_state.state = "MENU"
                return

            # Sound buttons
            music_muted = button_music_click(event, music_rect, music_muted)
            sound_muted = button_sound_click(event, sound_rect, sound_muted)
            
            if event.type == pygame.KEYDOWN:
                handle_key_press(event.key, game_state)

        pygame.display.flip()
        clock.tick(60)


