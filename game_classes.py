import pygame
import random

from game_assets import *

class GameState:
    def __init__(self) : 
        self.state = "MENU"         # Or "GAME" or "SCOREBOARD"
        self.score = 0              # Starting score
        self.lives = 3              # Starting lives
        self.freeze_timer = 0       # Freeze timer
        self.active_objects = []    # All items currently on screen
        self.active_particles = []  # All animations currently on screen
        self.difficulty = "Easy"    # Or "Medium" or "Hard"
        self.combo_count = 0        # Amount of fruits cut in a short time
        self.combo_timer = 0        # To evaluate the short time
        self.score_popup = None     # Popup to display combo bonus score
        self.sound_muted = False    # Sound control


    def frozen(self):
        """ True for 3-5 seconds seconds after activating ice cube """
        return self.freeze_timer > 0

    def register_hit(self):
        """ Called each time a fruit is hit to update combo logic """
        # Calculate miliseconds using pygame
        now = pygame.time.get_ticks()

        # Reset combo if too slow
        if now - self.combo_timer > 600:  # 0.6 seconds max window
            self.combo_count = 0

        self.combo_count += 1
        self.combo_timer = now

        # Return combo bonus
        if self.combo_count == 2 and now - self.combo_timer <= 200:
            return 2  # +2 points for 2 fruits cut in 200ms
        if self.combo_count == 3 and now - self.combo_timer <= 400:
            return 3  # +3 points for 3 fruits cut in 400ms
        if self.combo_count == 4 and now - self.combo_timer <= 600:
            return 4  # +6 points for 2 fruits cut in 600ms

        return 0
    
    def show_score_popup(self, text):
        """ Gives the combo text, its miliseconds duration, its transparency (255 = 1)"""
        self.score_popup = {
            "text": text,
            "timer": 600,   
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
        """ Move the object on each frame """
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

        # Letter black square
        box_size = 45
        offset_y = -110  # Distance from fruit

        rect_surface = pygame.Surface((box_size, box_size), pygame.SRCALPHA)
        rect_surface.fill((0, 0, 0, 120))  # 120 = Alpha transparency (0-255)
        screen.blit(rect_surface, (self.x - box_size//2, self.y + offset_y))


        # Center letter on the black square
        text_rect = self.text_surface.get_rect(center=(self.x, self.y + offset_y + box_size//2))
        screen.blit(self.text_surface, text_rect)


class Fruit(FlyingObject):
    def __init__(self, image, letter, position, speed, points=1):
        super().__init__(image, letter, position, speed)
        self.points = points
        # Get one of three slice sound at random for variety
        self.sound = random.choice((load_sound("assets/sounds/slice1.wav"),
                                    load_sound("assets/sounds/slice2.wav"),
                                    load_sound("assets/sounds/slice3.wav")))

    def on_hit(self, game_state):
        """ When the object letter is input by the player """
        if not game_state.sound_muted:
            self.sound.play()
        game_state.score += self.points
        bonus = game_state.register_hit()
        game_state.score += bonus
        if bonus > 0:
            game_state.show_score_popup(f"COMBO +{bonus}!")
        # Add particle effect 
        game_state.active_particles.append(Slice((self.x, self.y)))

    def on_miss(self, game_state):
        """ When the object disappears from bottom of the screen """
        game_state.lives -= 1


class IceCube(FlyingObject):
    def __init__(self, letter, position, speed) :
        super().__init__(load_image("assets/images/biggest_ice.png"), letter, position, speed)
        
    def on_hit(self, game_state):
        """ When the object letter is input by the player """
        if not game_state.sound_muted:
            load_sound("assets/sounds/ice.mp3").play()
        game_state.freeze_timer = random.randint(180,300)  # 3-5 seconds at 60 FPS
        # Add particle effect 
        game_state.active_particles.append(IceWind((self.x, self.y)))


class Bomb(FlyingObject):
    def __init__(self, letter, position, speed) :
        super().__init__(load_image("assets/images/big_bomb.png"), letter, position, speed)

    def on_hit(self, game_state):
        """ When the object letter is input by the player """

        # Play explosion sound
        if not game_state.sound_muted:
            load_sound("assets/sounds/bomb.wav").play()
        # Lose game
        game_state.lives = 0
        # Add particle effect 
        game_state.active_particles.append(Explosion((self.x, self.y)))


class ParticleEffect:
    def __init__(self, position):
        """ Initialize a slice particle effect at given position """
        
        self.position = position                # Center position of the effect
        self.frame_index = 0                    # Current frame index
        self.tick = 0                           # Counter to slow down animation
        self.finished = False                   # True when animation is over
        self.rotation = random.randint(-20, 20)    # Rotation for variations

    def update(self):
        """ Update the animation state each frame """
        # Increase tick counter
        self.tick += 1

        # Advance to next frame every 3 ticks
        if self.tick >= 2:
            self.frame_index += 1
            self.tick = 0

        # Mark as finished if all frames are shown
        if self.frame_index >= len(self.frames):
            self.finished = True

    def draw(self, screen):
        """ Draw the current frame of the effect """
        if not self.finished:
            frame = self.frames[self.frame_index]
            frame = pygame.transform.rotate(frame, self.rotation)
            rect = frame.get_rect(center=self.position)
            screen.blit(frame, rect)

class Slice(ParticleEffect) : 
    def __init__(self, position) : 
        super().__init__(position)
        # Load all slice frames once
        self.frames = [load_image(f"assets/images/animations/slice{i}.png") for i in range(1,9)]

class IceWind(ParticleEffect) : 
    def __init__(self, position) : 
        super().__init__(position)
        # Load all slice frames once
        self.frames = [load_image(f"assets/images/animations/icewind{i}.png") for i in range(1,9)]

class Explosion(ParticleEffect) : 
    def __init__(self, position) : 
        super().__init__(position)
        # Load all slice frames once
        self.frames = [load_image(f"assets/images/animations/explosion{i}.png") for i in range(1,9)]