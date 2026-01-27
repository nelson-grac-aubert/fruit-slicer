import pygame
from game_assets import *


pygame.init()

# Title
def draw_title(screen) : 
    """ Draw main title on main screen"""
    title_position = (screen.get_width() //2 , 100)
    title_color = (255, 147,147)
    title_size = 128
    
    title_font = pygame.font.Font(resource_path("assets/fonts/pixelify_sans.ttf"), title_size)
    title_surface = title_font.render("Pixel Cutter", True, title_color)
    
    title_rect = title_surface.get_rect(center = title_position)

    screen.blit(title_surface, title_rect)

# New game
def button(screen, clicked=False):
    button_width, button_height = 300, 100
    screen_width, screen_height = screen.get_size()
    button_x = (screen_width - button_width) // 2
    button_y = screen_height // 2 - 100

    color = (199, 0, 131) if not clicked else (0, 139, 245)

    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    pygame.draw.rect(screen, color, button_rect, border_radius=12)

    font = pygame.font.Font(resource_path("assets/fonts/pixelify_sans.ttf"), 48)
    text_surface = font.render("New Game", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    return button_rect

# Diffilcuty
def draw_difficulty_button(screen, current_level):
    button_width, button_height = 250, 80
    screen_width, screen_height = screen.get_size()

    # Position
    x = (screen_width - button_width) // 2
    y = screen_height // 2 + 50  

    # Color
    colors = {
        "Facile": (50, 200, 100),     # green
        "Normal": (255, 165, 0),      # orange
        "Difficile": (200, 50, 50)    # red
    }
    color = colors.get(current_level, (100, 100, 100))  

    button_rect = pygame.Rect(x, y, button_width, button_height)
    pygame.draw.rect(screen, color, button_rect, border_radius=12)

    font = pygame.font.Font(resource_path("assets/fonts/pixelify_sans.ttf"), 36)
    text_surface = font.render(current_level, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    return button_rect

# Score
def draw_score_button(screen, clicked=False):
    button_width, button_height = 250, 80
    screen_width, screen_height = screen.get_size()

    x = (screen_width - button_width) // 2
    y = screen_height // 2 + 160

    color = (0, 139, 245) if not clicked else (147, 255, 248)

    button_rect = pygame.Rect(x, y, button_width, button_height)
    pygame.draw.rect(screen, color, button_rect, border_radius=12)

    font = pygame.font.Font(resource_path("assets/fonts/pixelify_sans.ttf"), 40)
    text_surface = font.render("Score", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    return button_rect

# Event button 
def score_button_click(event, button_rect):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_rect.collidepoint(event.pos):
            print("Score!")
            return True
    return False


def difficulty_button_click(event, button_rect):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_rect.collidepoint(event.pos):
            return True
    return False

#Button press
def button_click(event, button_rect):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_rect.collidepoint(event.pos):
            print("New Game lancé!")
            return True
    return False



def draw_rotating_fruit(screen, image_path, position):
    
    if not hasattr(draw_rotating_fruit, "cache"):
        draw_rotating_fruit.cache = {}  # { path: (image, angle) }

    if image_path not in draw_rotating_fruit.cache:
        img = load_image(image_path)
        draw_rotating_fruit.cache[image_path] = [img, 0]  # [surface, angle]

    img, angle = draw_rotating_fruit.cache[image_path]

    # Update angle
    angle = (angle + 3) % 360
    draw_rotating_fruit.cache[image_path][1] = angle

    # Rotate
    rotated = pygame.transform.rotate(img, angle)
    rect = rotated.get_rect(center=position)

    # Draw
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



