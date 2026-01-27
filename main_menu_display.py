import pygame
from game_assets import *

def draw_title(screen) : 
    """ Draw main title on main screen"""
    title_position = (screen.get_width() //2 , 100)
    title_color = (255, 147,147)
    title_size = 128
    
    title_font = pygame.font.Font(resource_path("assets/fonts/pixelify_sans.ttf"), title_size)
    title_surface = title_font.render("Pixel Slicer", True, title_color)
    
    title_rect = title_surface.get_rect(center = title_position)

    screen.blit(title_surface, title_rect)


def draw_rotating_fruit(screen, image_path, position):
    # --- LOAD IMAGE ON FIRST CALL ---
    if not hasattr(draw_rotating_fruit, "cache"):
        draw_rotating_fruit.cache = {}  # { path: (image, angle) }

    if image_path not in draw_rotating_fruit.cache:
        img = load_image(image_path)
        draw_rotating_fruit.cache[image_path] = [img, 0]  # [surface, angle]

    img, angle = draw_rotating_fruit.cache[image_path]

    # --- UPDATE ANGLE ---
    angle = (angle + 3) % 360
    draw_rotating_fruit.cache[image_path][1] = angle

    # --- ROTATE ---
    rotated = pygame.transform.rotate(img, angle)
    rect = rotated.get_rect(center=position)

    # --- DRAW ---
    screen.blit(rotated, rect)

def draw_all_fruits(screen):
    """ Draws all fruits """
    screen_w = screen.get_width()
    screen_h = screen.get_height()

    fruits = [
        ("assets/images/big_watermelon.png",        (screen_w * 0.10, screen_h * 0.55)),
        ("assets/images/big_strawberry.png",        (screen_w * 0.90, screen_h * 0.70)),
        ("assets/images/biggest_ice.png",           (screen_w * 0.50, screen_h * 0.80)),
        ("assets/images/big_bomb.png",              (screen_w * 0.30, screen_h * 0.35)),
        ("assets/images/big_banana.png",            (screen_w * 0.70, screen_h * 0.30)),

    ]

    for path, pos in fruits:
        draw_rotating_fruit(screen, path, pos)
