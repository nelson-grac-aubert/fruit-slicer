import pygame

pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Pixel Slicer')

from game_assets import *
from sound_control import * 

clock = pygame.time.Clock()

width, height = 1200, 700
screen = pygame.display.set_mode((width, height))

background = load_image("assets/images/background.png")

# SOUND INIT
music_muted = False
sound_muted = False
music_img, music_muted_img, music_rect = load_music_images()
sound_img, sound_muted_img, sound_rect = load_sound_images()

running = True
while running:

    # EVENTS
    for event in pygame.event.get():

        music_muted = button_music_click(event, music_rect, music_muted)
        sound_muted = button_sound_click(event, sound_rect, sound_muted)

        if event.type == pygame.QUIT:
            running = False

    # DRAWING
    screen.blit(background, (0, 0))
    draw_music_button(screen, music_muted, music_img, music_muted_img, music_rect)
    draw_sound_button(screen, sound_muted, sound_img, sound_muted_img, sound_rect)

    # UPDATE
    pygame.display.flip()
    clock.tick(60)

pygame.quit()