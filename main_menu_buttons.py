import pygame
from game_assets import *

def draw_title(screen) : 
    title_position = (screen.get_width() //2 , 100)
    title_color = (255, 147,147)
    title_size = 128
    
    title_font = pygame.font.Font(resource_path("assets/fonts/pixelify_sans.ttf"), title_size)
    title_surface = title_font.render("Pixel Cutter", True, title_color)
    
    title_rect = title_surface.get_rect(center = title_position)

    screen.blit(title_surface, title_rect)