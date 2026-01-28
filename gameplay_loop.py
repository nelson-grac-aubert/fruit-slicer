import random

from difficulty_settings import DIFFICULTY_SETTINGS
from game_assets import * 
from game_classes import *

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
    """ Access all characters currently on screen to not pick it again """

    in_use_caracters = []
    for element in game_state.active_objects : 
        in_use_caracters.append(element.letter)
    return in_use_caracters


def get_random_character(difficulty, game_state) :
    """ Return a character for a FlyingObject to spawn
    taking consideration of difficulty and characters already on screen """

    easy_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
                'O','P','Q','R','S','T','U','V','W','X','Y','Z']
    medium_list = easy_list + ['1','2','3','4','5','6','7','8','9']
    hard_list = medium_list + ['²','0']

    in_use_characters = get_used_characters(game_state)

    match difficulty :
        case "Easy" : 
            while True:
                character = random.choice(easy_list)
                if not character in in_use_characters:
                    return character
        case "Medium" : 
            while True:
                character = random.choice(medium_list)
                if not character in in_use_characters:
                    return character
        case "Hard":
            while True:
                character = random.choice(hard_list)
                if not character in in_use_characters:
                    return character


def get_random_initial_position():
    """ Get a random but controlled initial position for the FlyingObject """
    SCREEN_HEIGHT = 700
    SCREEN_WIDTH = 1200
    return (
        random.choice([SCREEN_WIDTH + 50, -50]),            # Left or right
        random.randint(SCREEN_HEIGHT//3, SCREEN_HEIGHT//2)  # Between 33% and 50% of the screen
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
    game_state.active_objects.append(fruit) # And add it to the list to be tracked


def spawn_bomb(game_state) : 
    """ Spawns a Bomb FlyingObject with its stats randomized """
    pos = get_random_initial_position()
    speed = get_random_initial_speed(pos[0])
    bomb = Bomb(get_random_character(game_state.difficulty, game_state), pos, speed)
    game_state.active_objects.append(bomb) # And add it to the list to be tracked


def spawn_ice(game_state) : 
    """ Spawns and IceCube FlyingObject with its stats randomized """
    pos = get_random_initial_position()
    speed = get_random_initial_speed(pos[0])
    ice = IceCube(get_random_character(game_state.difficulty, game_state), pos, speed)
    game_state.active_objects.append(ice) # And add it to the list to be tracked


def spawn_item(game_state):
    """ Spawns a fruit, ice cube or bomb depending on difficulty settings """

    settings = DIFFICULTY_SETTINGS[game_state.difficulty]

    # Random allows to add % of chance when chosing, sett difficulty_settings.py to edit
    items = [spawn_fruit, spawn_bomb, spawn_ice]
    weights = settings["weights"]
    chosen = random.choices(items, weights=weights, k=1)[0]
    return chosen(game_state)


def update_all_objects(game_state):
    """ Applies the update method on all objects """

    # Initialize a list of items that are still on screen
    remaining = []
    for obj in game_state.active_objects:
        obj.update(game_state)

        # If objects goes 100 pixel under screen or sideways
        if obj.y >= 800 or obj.x <= -100 or obj.x >= 1400:
            if hasattr(obj, "on_miss"): 
                obj.on_miss(game_state) # Lose a life if it's a fruit
        else:
            remaining.append(obj) # Else keep it in the list

    # Update list
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
    """ Draws a little popup below score to indicate bonus """

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