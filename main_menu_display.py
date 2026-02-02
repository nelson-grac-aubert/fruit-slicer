import pygame
from game_assets import load_font, load_image, resource_path
from language import current_language

def draw_title(screen):
    """ Draws Title on Main Screen """

    # Centered horizontally, on top vertically
    title_position = (screen.get_width() // 2, 100)
    title_color = (255, 147, 147)
    title_size = 128

    title_font = load_font(("assets/fonts/pixelify_sans.ttf"), title_size)
    title_surface = title_font.render("Pixel Slicer", True, title_color)
    
    title_rect = title_surface.get_rect(center = title_position)
    screen.blit(title_surface, title_rect)

def new_game_button(screen, current_language):
    """ Draws New Game button on Main Screen """

    # Centered horizontally, below title
    button_width, button_height = 350, 100
    screen_width, screen_height = screen.get_size()
    x = (screen_width - button_width) // 2
    y = screen_height // 2 - 100

    # Hover effect
    mouse_pos = pygame.mouse.get_pos()
    hovered = pygame.Rect(x, y, button_width, button_height).collidepoint(mouse_pos)
    color = (143, 0, 118) if not hovered else (199, 0, 131)

    # Rectangle behind text
    button_rect = pygame.Rect(x, y, button_width, button_height)
    pygame.draw.rect(screen, color, button_rect, border_radius=12)

    # Text
    font = pygame.font.Font(resource_path("assets/fonts/pixelify_sans.ttf"), 48)
    text_surface = font.render(f"{current_language.new_game}", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    return button_rect

def draw_exit_button(screen):
    """ Draws a small 'X' button in top-left corner """
    
    # X sign
    font = pygame.font.Font(resource_path("assets/fonts/pixelify_sans.ttf"), 36)
    text_surface = font.render("X", True, (255, 255, 255))
    button_rect = pygame.Rect(20, 20, 40, 40)

    # Hover effect
    mouse_pos = pygame.mouse.get_pos()
    hovered = button_rect.collidepoint(mouse_pos)
    color = (200, 50, 50) if not hovered else (255, 80, 80)

    # Draw rectangle
    pygame.draw.rect(screen, color, button_rect, border_radius=8)
    screen.blit(text_surface, text_surface.get_rect(center=button_rect.center))

    return button_rect

def exit_button_click(event, button_rect):
    """ Handle exit button click behavior """
    return event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos)

def draw_exit_confirmation(screen):
    """ Draws confirmation window with YES/NO buttons """

    # Greys out screen with a transparent overlay
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180)) 

    # Draw rectangle around buttons
    pygame.draw.rect(overlay, (50, 50, 50), (400, 250, 400, 200), border_radius=12)
    font = pygame.font.Font(resource_path("assets/fonts/pixelify_sans.ttf"), 28)
    text = font.render("Do you wish to exit game", True, (255, 255, 255))
    overlay.blit(text, text.get_rect(center=(600, 290)))

    # Buttons rectangle
    yes_rect = pygame.Rect(450, 350, 100, 50)
    no_rect = pygame.Rect(650, 350, 100, 50)
    pygame.draw.rect(overlay, (200, 50, 50), yes_rect, border_radius=8)
    pygame.draw.rect(overlay, (50, 200, 100), no_rect, border_radius=8)

    # Buttons Text
    font_btn = pygame.font.Font(resource_path("assets/fonts/pixelify_sans.ttf"), 28)
    overlay.blit(font_btn.render("YES", True, (255, 255, 255)), yes_rect.move(25, 10))
    overlay.blit(font_btn.render("NO", True, (255, 255, 255)), no_rect.move(34, 10))

    screen.blit(overlay, (0, 0))
    return yes_rect, no_rect


def draw_difficulty_button(screen, current_level):
    """ Draw difficulty button on main screen """

    # Centered horizontally, below new game button
    button_width, button_height = 350, 100
    screen_width, screen_height = screen.get_size()
    x = (screen_width - button_width) // 2
    y = screen_height // 2 + 50

    # Hover
    mouse_pos = pygame.mouse.get_pos()
    hovered = pygame.Rect(x, y, button_width, button_height).collidepoint(mouse_pos)

    # Color depends on current difficulty
    base_colors = {
        "Easy": (50, 200, 100),
        "Medium": (255, 165, 0),
        "Hard": (200, 50, 50)
    }
    hover_colors = {
        "Easy": (80, 255, 130),
        "Medium": (255, 190, 60),
        "Hard": (255, 80, 80)
    }
    color = hover_colors[current_level] if hovered else base_colors[current_level]

    # Rectangle behind text
    button_rect = pygame.Rect(x, y, button_width, button_height)
    pygame.draw.rect(screen, color, button_rect, border_radius=12)

    # Text depends on difficulty
    font = pygame.font.Font(resource_path("assets/fonts/pixelify_sans.ttf"), 36)
    text_surface = font.render(f"Difficulty : {current_level}", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    return button_rect

def draw_score_button(screen):
    """ Draw score screen button under difficulty button """

    # Position
    button_width, button_height = 350, 100
    screen_width, screen_height = screen.get_size()
    x = (screen_width - button_width) // 2
    y = screen_height // 2 + 200

    # Hover effect
    mouse_pos = pygame.mouse.get_pos()
    hovered = pygame.Rect(x, y, button_width, button_height).collidepoint(mouse_pos)
    color = (0, 139, 245) if not hovered else (147, 255, 248)

    # Rectangle behind text
    button_rect = pygame.Rect(x, y, button_width, button_height)
    pygame.draw.rect(screen, color, button_rect, border_radius=12)

    # Text
    font = pygame.font.Font(resource_path("assets/fonts/pixelify_sans.ttf"), 36)
    text_surface = font.render("Leaderboard", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    return button_rect

def draw_back_button(screen, hover_scale=1.15):
    """ Draws the back to main menu button with hover zoom effect."""
    
    img = load_image("assets/images/arrow.png")
    rect = img.get_rect(center=(1120,640))

    mouse_pos = pygame.mouse.get_pos()
    hovered = rect.collidepoint(mouse_pos)

    # Zoom on hover
    if hovered:
        img = pygame.transform.scale(
            img,
            (int(rect.width * hover_scale), int(rect.height * hover_scale))
        )
        rect = img.get_rect(center=(1120,640))

    screen.blit(img, rect)
    return rect


# Buttons click event
def game_button_click(event, button_rect):
    return event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos)

def difficulty_button_click(event, button_rect):
    return event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos)

def score_button_click(event, button_rect):
    return event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos)

def back_button_click(event, rect):
    return event.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(event.pos)


def draw_rotating_fruit(screen, image_path, position):
    """ Draw a decorative fruit on main screen """
    # Load image on first call
    if not hasattr(draw_rotating_fruit, "cache"):
        draw_rotating_fruit.cache = {}

    if image_path not in draw_rotating_fruit.cache:
        img = load_image(image_path)
        draw_rotating_fruit.cache[image_path] = [img, 0]

    img, angle = draw_rotating_fruit.cache[image_path]
    
    # Update angle
    angle = (angle + 3) % 360
    draw_rotating_fruit.cache[image_path][1] = angle

    # Rotate
    rotated = pygame.transform.rotate(img, angle)
    rect = rotated.get_rect(center=position)

    # Draw
    screen.blit(rotated, rect)

def draw_menu_fruits(screen):
    """ Draws menu rotating fruits on main screen """

    # Screen size
    screen_w = screen.get_width()
    screen_h = screen.get_height()

    # Image, position
    fruits = [                  
        ("assets/images/big_watermelon.png", (screen_w * 0.10, screen_h * 0.55)), 
        ("assets/images/big_strawberry.png", (screen_w * 0.90, screen_h * 0.70)),
    ]

    for path, pos in fruits:
        draw_rotating_fruit(screen, path, pos)
