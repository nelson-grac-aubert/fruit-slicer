import random

from game_assets import * 
from game_classes import *

active_objects = []

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


def get_random_initial_position():
    SCREEN_HEIGHT = 700
    SCREEN_WIDTH = 1200
    return (
        random.choice([SCREEN_WIDTH + 100, -100]),   # LEFT OR RIGHT
        random.randint(SCREEN_HEIGHT//2, SCREEN_HEIGHT) # VERTICAL
    )


def get_random_initial_speed() : 
    """ Return an initial speed (x,y) for the FlyingObject"""
    x_speed = random.choice([-1, 1]) * random.randint(4, 8)  # towards the center
    y_speed = -random.randint(10, 17)                         # vers le haut
    return (x_speed, y_speed)


def spawn_fruit() : 
    """ Spawns a Fruit FlyingObject with all its stats randomized """
    fruit = Fruit(get_random_fruit_image(), 
            random.choice(["A","B","C", "D"]), #NOM DE LA FONCTION DE YANNIS POUR LES LETTRES
            get_random_initial_position(),
            get_random_initial_speed())
    active_objects.append(fruit)
    

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
    