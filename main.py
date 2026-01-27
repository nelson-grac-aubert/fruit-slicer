import pygame

pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Pixel Slicer')

from game_classes import GameState
from gameplay_loop import active_objects, spawn_fruit, update_all_objects, draw_all_fruits
from game_assets import *
from sound_control import * 
from main_menu_display import * 

# MUSIC 
load_music("assets/sounds/synthwave.mp3")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

width, height = 1200, 700
screen = pygame.display.set_mode((width, height))

background = load_image("assets/images/background.png")

def main() : 

    # SOUND INIT
    music_muted = False
    sound_muted = False
    music_img, music_muted_img, music_rect = load_music_images()
    sound_img, sound_muted_img, sound_rect = load_sound_images()

    game_state = GameState()
    spawn_cooldown = 0

    while True:

        # EVENTS
        for event in pygame.event.get():

            music_muted = button_music_click(event, music_rect, music_muted)
            sound_muted = button_sound_click(event, sound_rect, sound_muted)

            if event.type == pygame.QUIT:
                pygame.quit()

        update_all_objects(game_state)

        # DRAWING
        screen.blit(background, (0, 0))
        draw_title(screen)
        draw_music_button(screen, music_muted, music_img, music_muted_img, music_rect)
        draw_sound_button(screen, sound_muted, sound_img, sound_muted_img, sound_rect)
        draw_menu_fruits(screen)
        draw_all_fruits(screen)

        # SPAWN
        spawn_cooldown += 1
        if spawn_cooldown >= 30:   # toutes les 0.5 seconde
            spawn_fruit()
            spawn_cooldown = 0
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__" : 

    main()