import random

from game_assets import * 
from game_classes import *

active_objects = []

# def get_difficulty(difficulty_levels, difficulty_index) : 
#     return difficulty_levels[difficulty_index]

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

def get_used_characters(active_objects) : 
    in_use_caracters = []
    for element in active_objects : 
        in_use_caracters.append(element.letter)
    return in_use_caracters

def get_random_character(difficulty) :
    easy_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    medium_list = easy_list + ['0','1','2','3','4','5','6','7','8','9','²']
    hard_list = medium_list + ['&','é','"',"'",'(','-','è','_','ç','à',')','=','^','$','ù','*','<',',',';',':','!']
    in_use_characters = get_used_characters(active_objects)

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
        random.choice([SCREEN_WIDTH + 100, -100]),   # LEFT OR RIGHT
        random.randint(SCREEN_HEIGHT//2, SCREEN_HEIGHT) # VERTICAL
    )


def get_random_initial_speed() : 
    """ Return an initial speed (x,y) for the FlyingObject"""
    x_speed = random.choice([-1, 1]) * random.randint(6, 8)  # TOWARDS THE CENTER
    y_speed = -random.randint(10, 17)                        # UP
    return (x_speed, y_speed)


def spawn_fruit() : 
    """ Spawns a Fruit FlyingObject with all its stats randomized """
    fruit = Fruit(get_random_fruit_image(), 
            get_random_character("Easy"),
            get_random_initial_position(),
            get_random_initial_speed())
    active_objects.append(fruit)

def spawn_bomb() : 
    """ Spawns a Bomb FlyingObject with its stats randomized """
    bomb = Bomb(get_random_character("Easy"),
            get_random_initial_position(),
            get_random_initial_speed())
    active_objects.append(bomb)

def spawn_ice() : 
    """ Spawns and IceCube FlyingObject with its stats randomized """
    ice = IceCube(get_random_character("Easy"),
                  get_random_initial_position(),
                  get_random_initial_speed())
    active_objects.append(ice)

def spawn_item() : 

    difficulty = "Easy"
    if difficulty == "Easy":
        items = [spawn_fruit, spawn_bomb, spawn_ice]
        weights = [85, 5, 10]

    elif difficulty == "Medium":
        items = [spawn_fruit, spawn_bomb, spawn_ice]
        weights = [85, 10, 5]

    else:  # Hard
        items = [spawn_fruit, spawn_bomb, spawn_ice]
        weights = [74, 25, 1]

    chosen = random.choices(items, weights=weights, k=1)[0]
    return chosen()


def update_all_objects(game_state):
    """ Applies the update method on all objects """
    global active_objects

    for obj in active_objects:
        obj.update(game_state)

    # remove objects that fall off screen
    active_objects = [o for o in active_objects if o.y < 800 and -100 < o.x < 1400]

def draw_all_fruits(screen):
    for obj in active_objects:
        obj.draw(screen)
    