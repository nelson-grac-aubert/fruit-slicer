import pygame
import random

from game_assets import *

# A game states that handles lives, score, and ice cube freeze effect
class GameState:
    def __init__(self) : 
        self.score = 0 
        self.lives = 3 
        self.freeze_timer = 0 

    def frozen(self):
        return self.freeze_timer > 0


# All objects flying across screens
class FlyingObject:
    def __init__(self, image, letter, position, speed):
        self.image = image
        self.letter = letter
        self.x, self.y = position
        self.x_speed, self.y_speed = speed
        self.gravity = 0.4
        self.rotation = 0
        self.rotation_speed = random.randint(2,4)

        self.font = load_font("assets/fonts/pixelify_sans.ttf", 32)
        self.text_surface = self.font.render(self.letter, True, (255, 255, 255))

    def update(self, game_state):
        if not game_state.frozen():
            self.y_speed += self.gravity
            self.x += self.x_speed
            self.y += self.y_speed
            self.rotation += self.rotation_speed


    def draw(self, screen):
        rotated = pygame.transform.rotate(self.image, self.rotation)
        rect = rotated.get_rect(center=(self.x, self.y))
        screen.blit(rotated, rect)

        pygame.draw.rect(screen, (0, 0, 0), (self.x - 20, self.y - 60, 40, 40))
        screen.blit(self.text_surface, (self.x - 12, self.y - 55))


class Fruit(FlyingObject):
    def __init__(self, image, letter, position, speed, points=1):
        super().__init__(image, letter, position, speed)
        self.points = points

    def on_hit(self, game_state):
        game_state.score += self.points

    def on_miss(self, game_state):
        game_state.lives -= 1


class IceCube(FlyingObject):
    def __init__(self, letter, position, speed) :
        super().__init__(load_image("assets/images/biggest_ice.png"), letter, position, speed)
        
    def on_hit(self, game_state):
        game_state.freeze_timer = 120  # 2 seconds at 60 FPS


class Bomb(FlyingObject):
    def __init__(self, letter, position, speed) :
        super().__init__(load_image("assets/images/big_bomb.png"), letter, position, speed)

    def on_hit(self, game_state):
        game_state.lives -= 3 
