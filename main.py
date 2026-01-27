import pygame

pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Pixel Slicer')

from game_classes import GameState
from gameplay_loop import active_objects, spawn_fruit, update_all_objects, draw_all_fruits
from game_assets import *
from sound_control import * 
from main_menu_display import * 

# Music
load_music("assets/sounds/synthwave.mp3")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

width, height = 1200, 700
screen = pygame.display.set_mode((width, height))

background = load_image("assets/images/background.png")

# Diffilcuty
difficulty_levels = ["Facile", "Normal", "Difficile"]
difficulty_index = 0


game_state = GameState()
spawn_cooldown = 0


# Sound init
music_muted = False
sound_muted = False
music_img, music_muted_img, music_rect = load_music_images()
sound_img, sound_muted_img, sound_rect = load_sound_images()

# Animation
button_clicked = False
click_timer = 0
score_clicked = False
score_click_timer = 0

running = True
while running:

    screen.blit(background, (0, 0))

    draw_title(screen)
    draw_music_button(screen, music_muted, music_img, music_muted_img, music_rect)
    draw_sound_button(screen, sound_muted, sound_img, sound_muted_img, sound_rect)
    draw_menu_fruits(screen)
    draw_all_fruits(screen)
    update_all_objects(game_state)

    spawn_cooldown += 1
    if spawn_cooldown >= 60:
        spawn_fruit()
        spawn_cooldown = 0

    # Draw buttons before events
    button_rect = button(screen, button_clicked)
    difficulty_rect = draw_difficulty_button(screen, difficulty_levels[difficulty_index])
    score_rect = draw_score_button(screen, score_clicked)

    # Events
    for event in pygame.event.get():
        music_muted = button_music_click(event, music_rect, music_muted)
        sound_muted = button_sound_click(event, sound_rect, sound_muted)
        
        if score_button_click(event, score_rect):
            print("Score ouvert !")
            score_clicked = True
            score_click_timer = 10

        if button_click(event, button_rect):
            print("Bouton cliqué !")
            button_clicked = True
            click_timer = 10

        if difficulty_button_click(event, difficulty_rect):
            difficulty_index = (difficulty_index + 1) % len(difficulty_levels)

        if score_button_click(event, score_rect):
            print("Affichage du score !")

        if event.type == pygame.QUIT:
            running = False

    # Timer animation
    if click_timer > 0:
        click_timer -= 1
    else:
        button_clicked = False
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
