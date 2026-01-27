import pygame
from game_assets import *

pygame.init()

# Title
def draw_title(screen):
    title_position = (screen.get_width() // 2, 100)
    title_color = (255, 147, 147)
    title_size = 128

    title_font = pygame.font.Font(resource_path("assets/fonts/pixelify_sans.ttf"), title_size)
    title_surface = title_font.render("Pixel Slicer", True, title_color)
    
    title_rect = title_surface.get_rect(center = title_position)

    screen.blit(title_surface, title_rect)


# New game button
def button(screen):
    button_width, button_height = 300, 100
    screen_width, screen_height = screen.get_size()
    x = (screen_width - button_width) // 2
    y = screen_height // 2 - 100

    mouse_pos = pygame.mouse.get_pos()
    hovered = pygame.Rect(x, y, button_width, button_height).collidepoint(mouse_pos)

    color = (143, 0, 118) if not hovered else (199, 0, 131)

    button_rect = pygame.Rect(x, y, button_width, button_height)
    pygame.draw.rect(screen, color, button_rect, border_radius=12)

    font = pygame.font.Font(resource_path("assets/fonts/pixelify_sans.ttf"), 48)
    text_surface = font.render("New Game", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    return button_rect


# Diffilculty button 
def draw_difficulty_button(screen, current_level):
    button_width, button_height = 250, 80
    screen_width, screen_height = screen.get_size()
    x = (screen_width - button_width) // 2
    y = screen_height // 2 + 50

    mouse_pos = pygame.mouse.get_pos()
    hovered = pygame.Rect(x, y, button_width, button_height).collidepoint(mouse_pos)

    # Color
    base_colors = {
        "Facile": (50, 200, 100),
        "Normal": (255, 165, 0),
        "Difficile": (200, 50, 50)
    }
    hover_colors = {
        "Facile": (80, 255, 130),
        "Normal": (255, 190, 60),
        "Difficile": (255, 80, 80)
    }

    color = hover_colors[current_level] if hovered else base_colors[current_level]

    button_rect = pygame.Rect(x, y, button_width, button_height)
    pygame.draw.rect(screen, color, button_rect, border_radius=12)

    font = pygame.font.Font(resource_path("assets/fonts/pixelify_sans.ttf"), 36)
    text_surface = font.render(current_level, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    return button_rect


# Score button 
def draw_score_button(screen):
    button_width, button_height = 250, 80
    screen_width, screen_height = screen.get_size()
    x = (screen_width - button_width) // 2
    y = screen_height // 2 + 160

    mouse_pos = pygame.mouse.get_pos()
    hovered = pygame.Rect(x, y, button_width, button_height).collidepoint(mouse_pos)

    color = (0, 139, 245) if not hovered else (147, 255, 248)

    button_rect = pygame.Rect(x, y, button_width, button_height)
    pygame.draw.rect(screen, color, button_rect, border_radius=12)

    font = pygame.font.Font(resource_path("assets/fonts/pixelify_sans.ttf"), 40)
    text_surface = font.render("Score", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    return button_rect


# Buttons click event
def button_click(event, button_rect):
    return event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos)

def difficulty_button_click(event, button_rect):
    return event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos)

def score_button_click(event, button_rect):
    return event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos)


# Fruits
def draw_rotating_fruit(screen, image_path, position):
    # LOAD IMAGE ON FIRST CALL
    if not hasattr(draw_rotating_fruit, "cache"):
        draw_rotating_fruit.cache = {}

    if image_path not in draw_rotating_fruit.cache:
        img = load_image(image_path)
        draw_rotating_fruit.cache[image_path] = [img, 0]

    img, angle = draw_rotating_fruit.cache[image_path]
    
    # UPDATE ANGLE
    angle = (angle + 3) % 360
    draw_rotating_fruit.cache[image_path][1] = angle

    # ROTATE
    rotated = pygame.transform.rotate(img, angle)
    rect = rotated.get_rect(center=position)

    # DRAW
    screen.blit(rotated, rect)

def draw_menu_fruits(screen):
    """ Draws all fruits """
    screen_w = screen.get_width()
    screen_h = screen.get_height()

    fruits = [
        ("assets/images/big_watermelon.png",        (screen_w * 0.10, screen_h * 0.55)),
        ("assets/images/big_strawberry.png",        (screen_w * 0.90, screen_h * 0.70)),
    ]

    for path, pos in fruits:
        draw_rotating_fruit(screen, path, pos)
