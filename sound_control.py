import pygame
from game_assets import *

def load_music_images():
    """ Loads music button images and returns their pygame rectangle """
    music_image = load_image("assets/images/music.png")
    music_muted_image = load_image("assets/images/music_off.png")
    music_image_size = (80,80)
    music_image = pygame.transform.scale(music_image, (music_image_size))
    music_muted_image = pygame.transform.scale(music_muted_image, (music_image_size))

    music_image_position = (50,650)
    music_image_rectangle = music_image.get_rect(center=(music_image_position))

    return music_image, music_muted_image, music_image_rectangle

def load_sound_images():
    """ Loads sound button images and returns their pygame rectangle """
    sound_image = load_image("assets/images/sound.png")
    sound_muted_image = load_image("assets/images/sound_off.png")
    sound_image_size = (80,80)
    sound_image = pygame.transform.scale(sound_image, sound_image_size)
    sound_muted_image = pygame.transform.scale(sound_muted_image, sound_image_size)

    sound_image_position = (140,650)
    sound_image_rectangle = sound_image.get_rect(center=(sound_image_position))

    return sound_image, sound_muted_image, sound_image_rectangle

def draw_music_button(screen, music_muted, music_image, music_muted_image, rect):
    """ Draw music on/off button """
    screen.blit(music_muted_image if music_muted else music_image, rect)

def draw_sound_button(screen, sound_muted, sound_mute_icon, sound_unmute_icon, rect):
    """ Draw sound on/off button """
    screen.blit(sound_unmute_icon if sound_muted else sound_mute_icon, rect)

def button_music_click(event, rect, music_muted):
    """ Mute/unmute music behavior """
    if event.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(event.pos):
        music_muted = not music_muted
        if music_muted:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    return music_muted

def button_sound_click(event, rect, sound_muted):
    """ Mute/unmute sound behavior """
    if event.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(event.pos):
        sound_muted = not sound_muted
    return sound_muted