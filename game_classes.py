import pygame
import random

from game_assets import *

# A game states that handles lives, score, and ice cube freeze effect
class GameState:
    def __init__(self) : 
        self.state = "MENU"
        self.score = 0 
        self.lives = 3 
        self.freeze_timer = 0 
        self.active_objects = []
        self.difficulty = "Easy"
        self.combo_count = 0
        self.combo_timer = 0
        self.score_popup = None

    def frozen(self):
        """ True for 3-5 seconds seconds after activating ice cube """
        return self.freeze_timer > 0

    def register_hit(self):
        """Called each time a fruit is hit to update combo logic."""
        now = pygame.time.get_ticks()

        # Reset combo if too slow
        if now - self.combo_timer > 400:  # 0.4 seconds max window
            self.combo_count = 0

        self.combo_count += 1
        self.combo_timer = now

        # Return combo bonus
        if self.combo_count == 2 and now - self.combo_timer <= 200:
            return 2  # +2 points
        if self.combo_count == 3 and now - self.combo_timer <= 400:
            return 3  # +3 points

        return 0
    
    def show_score_popup(self, text):
        self.score_popup = {
            "text": text,
            "timer": 600,   # MS Duration
            "alpha": 255
        }

# All objects flying across screens
class FlyingObject:
    def __init__(self, image, letter, position, speed):
        self.image = image
        self.letter = letter
        self.x, self.y = position
        self.x_speed, self.y_speed = speed
        self.gravity = 0.1
        self.rotation = random.randint(0,360)
        self.rotation_speed = random.randint(-6,6)

        self.font = load_font("assets/fonts/roboto.ttf", 50)
        self.text_surface = self.font.render(self.letter, True, (255, 255, 255))

    def update(self, game_state):
        """ Move the object """
        if not game_state.frozen():
            self.y_speed += self.gravity
            self.x += self.x_speed
            self.y += self.y_speed
            self.rotation += self.rotation_speed


    def draw(self, screen):
        """ Blits the object and its letter on the screen """
        rotated = pygame.transform.rotate(self.image, self.rotation)
        rect = rotated.get_rect(center=(self.x, self.y))
        screen.blit(rotated, rect)

        # LETTER
        box_size = 45
        offset_y = -110  # DISTANCE FROM FRUIT

        rect_surface = pygame.Surface((box_size, box_size), pygame.SRCALPHA)
        rect_surface.fill((0, 0, 0, 120))  # 120 = ALPHA TRANSPARENCE (0-255)
        screen.blit(rect_surface, (self.x - box_size//2, self.y + offset_y))


        # CENTER LETTER ON SQUARE
        text_rect = self.text_surface.get_rect(center=(self.x, self.y + offset_y + box_size//2))
        screen.blit(self.text_surface, text_rect)


class Fruit(FlyingObject):
    def __init__(self, image, letter, position, speed, points=1):
        super().__init__(image, letter, position, speed)
        self.points = points

    def on_hit(self, game_state):
        load_sound("assets/sounds/slice1.mp3").play()
        game_state.score += self.points
        bonus = game_state.register_hit()
        game_state.score += bonus
        if bonus > 0:
            game_state.show_score_popup(f"COMBO +{bonus}!")



    def on_miss(self, game_state):
        game_state.lives -= 1


class IceCube(FlyingObject):
    def __init__(self, letter, position, speed) :
        super().__init__(load_image("assets/images/biggest_ice.png"), letter, position, speed)
        
    def on_hit(self, game_state):
        load_sound("assets/sounds/ice.mp3").play()
        game_state.freeze_timer = random.randint(180,300)  # 3-5 seconds at 60 FPS


class Bomb(FlyingObject):
    def __init__(self, letter, position, speed) :
        super().__init__(load_image("assets/images/big_bomb.png"), letter, position, speed)

    def on_hit(self, game_state):
        game_state.lives -= 3 
