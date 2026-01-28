import random

from difficulty_settings import DIFFICULTY_SETTINGS
from game_assets import * 
from game_classes import *

# def get_difficulty(difficulty_levels, difficulty_index) : 
# return difficulty_levels[difficulty_index]

def get_random_fruit_image() : 
    """ Return a fruit sprite chosen at random """
    return load_image(random.choice([
        "assets/images/big_watermelon.png",        
        "assets/images/big_strawberry.png",                             
        "assets/images/big_banana.png",           
        "assets/images/cherry.png",
        "assets/images/apple.png",
        "assets/images/pineapple.png",
        "assets/images/orange.png"
        ]))

def get_used_characters(game_state) : 
    in_use_caracters = []
    for element in game_state.active_objects : 
        in_use_caracters.append(element.letter)
    return in_use_caracters

def get_random_character(difficulty, game_state) :
    easy_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    medium_list = easy_list + ['0','1','2','3','4','5','6','7','8','9']
    hard_list = medium_list + ['²']

    in_use_characters = get_used_characters(game_state)

    if difficulty == "Easy":
        while True:
            character = random.choice(easy_list)
            if not character in in_use_characters:
                return character
    if difficulty == "Medium":
        while True:
            character = random.choice(medium_list)
            if not character in in_use_characters:
                return character
    if difficulty == "Hard":
        while True:
            character = random.choice(hard_list)
            if not character in in_use_characters:
                return character

def get_random_initial_position():
    SCREEN_HEIGHT = 700
    SCREEN_WIDTH = 1200
    return (
        random.choice([SCREEN_WIDTH + 50, -50]),   # LEFT OR RIGHT
        random.randint(SCREEN_HEIGHT//3, SCREEN_HEIGHT//2) # VERTICAL
    )


def get_random_initial_speed(initial_x):
    """Return an initial speed (x, y) based on spawn side."""
    
    # If item spawns on the right : moves left
    if initial_x > 1200:  
        x_speed = -random.randint(6, 8)

    # If item spawns on left : moves right
    else:
        x_speed = random.randint(6, 8)

    y_speed = -random.randint(3, 6)  # Always upwards

    return (x_speed, y_speed)


def spawn_fruit(game_state) : 
    """ Spawns a Fruit FlyingObject with all its stats randomized """
    pos = get_random_initial_position()
    speed = get_random_initial_speed(pos[0])
    fruit = Fruit(get_random_fruit_image(),
                  get_random_character(game_state.difficulty, game_state),
                  pos,
                  speed)
    game_state.active_objects.append(fruit)



def spawn_bomb(game_state) : 
    """ Spawns a Bomb FlyingObject with its stats randomized """
    pos = get_random_initial_position()
    speed = get_random_initial_speed(pos[0])
    bomb = Bomb(get_random_character(game_state.difficulty, game_state), pos, speed)
    game_state.active_objects.append(bomb)


def spawn_ice(game_state) : 
    """ Spawns and IceCube FlyingObject with its stats randomized """
    pos = get_random_initial_position()
    speed = get_random_initial_speed(pos[0])
    ice = IceCube(get_random_character(game_state.difficulty, game_state), pos, speed)
    game_state.active_objects.append(ice)


def spawn_item(game_state):
    settings = DIFFICULTY_SETTINGS[game_state.difficulty]

    items = [spawn_fruit, spawn_bomb, spawn_ice]
    weights = settings["weights"]

    chosen = random.choices(items, weights=weights, k=1)[0]
    return chosen(game_state)


def update_all_objects(game_state):
    """ Applies the update method on all objects """

    remaining = []
    for obj in game_state.active_objects:
        obj.update(game_state)

        # S'il sort de l'écran → MISS
        if obj.y >= 800 or obj.x <= -100 or obj.x >= 1400:
            if hasattr(obj, "on_miss"):
                obj.on_miss(game_state)
        else:
            remaining.append(obj)

    game_state.active_objects = remaining


def draw_all_fruits(screen, game_state):
    """ Draws all fruits in active_object on the game screen """
    for obj in game_state.active_objects:
        obj.draw(screen)


def handle_key_press(key, game_state):
    """ Handles item destruction depending on their letter """

    try:
        pressed = chr(key).lower()
    except:
        return

    # Looks for an item that has this letter
    for obj in game_state.active_objects:
        if obj.letter.lower() == pressed:
            obj.on_hit(game_state)
            game_state.active_objects.remove(obj)
            break

def draw_lives(screen, game_state):
    """ Displays lives on top right of screen """
    life_full = load_image("assets/images/life_remaing.png")
    life_empty = load_image("assets/images/life_lost.png")

    total_lives = 3
    x_start = 1200 - 150    # First life position
    y = 20                  # Fixed height
    spacing = 100           # Spacing between lives

    for i in range(total_lives):
        x = x_start - i * spacing

        if i < game_state.lives:
            screen.blit(life_full, (x, y))
        else:
            screen.blit(life_empty, (x, y))

def get_pixel_font(size):
    """ Loads font once for Game Over screen """
    return load_font("assets/fonts/pixelify_sans.ttf", size)

def draw_play_again_button(screen):
    """ Blits play again button on game loss """
    font = get_pixel_font(48)
    text = font.render("PLAY AGAIN", True, (255, 255, 255))
    rect = text.get_rect(center=(600, 450))

    pygame.draw.rect(screen, (40, 40, 40), rect.inflate(40, 20), border_radius=8)
    screen.blit(text, rect)

    return rect

def draw_main_menu_button(screen):
    """ Blits back to main menu button on game loss """
    font = get_pixel_font(48)
    text = font.render("MAIN MENU", True, (255, 255, 255))
    rect = text.get_rect(center=(600, 550))

    pygame.draw.rect(screen, (40, 40, 40), rect.inflate(40, 20), border_radius=8)
    screen.blit(text, rect)

    return rect

def draw_game_over_title(screen):
    """ Blits Game Over Title on game loss """
    font = get_pixel_font(80)
    text = font.render("GAME OVER", True, (255, 80, 80))
    rect = text.get_rect(center=(600, 250))

    pygame.draw.rect(screen, (0, 0, 0), rect.inflate(60, 30))
    screen.blit(text, rect)

def game_over_screen(screen, game_state):
    """ Displays end of game screen with play again and main menu button """

    while True:
        screen.fill((20, 20, 20))

        # Title
        draw_game_over_title(screen)

        # Buttons
        play_rect = draw_play_again_button(screen)
        menu_rect = draw_main_menu_button(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    return "RESTART"
                if menu_rect.collidepoint(event.pos):
                    return "MENU"

        pygame.display.flip()

def reset_gameplay_state(game_state):
    """Resets game state at the end of the game"""
    game_state.lives = 3
    game_state.score = 0
    game_state.freeze_timer = 0
    game_state.active_objects.clear()

def draw_score(screen, game_state):
    """ Draws current score on top middle of screen """
    font = load_font("assets/fonts/pixelify_sans.ttf", 120)
    text = font.render(str(game_state.score), True, (255, 255, 255))
    rect = text.get_rect(center=(600, 70))  
    screen.blit(text, rect)

def draw_score_popup(screen, game_state):
    if not game_state.score_popup:
        return

    popup = game_state.score_popup
    font = load_font("assets/fonts/pixelify_sans.ttf", 36)

    # Update
    popup["timer"] -= 16
    popup["alpha"] -= 4

    if popup["timer"] <= 0 or popup["alpha"] <= 0:
        game_state.score_popup = None
        return

    # Position under the game score
    text_surface = font.render(popup["text"], True, (255, 255, 0))
    text_surface.set_alpha(popup["alpha"])
    rect = text_surface.get_rect(center=(600, 135))
    screen.blit(text_surface, rect)