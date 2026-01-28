import pygame

# Initialize pygame and window
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Pixel Slicer')

from game_classes import GameState
from game_assets import *
from sound_control import * 
from main_menu_display import * 
from game_screen import game_screen
from gameplay_loop import * 

# Music
load_music("assets/sounds/synthwave.mp3")
pygame.mixer.music.play(-1)

# Initialize display and clock
clock = pygame.time.Clock()
width, height = 1200, 700
screen = pygame.display.set_mode((width, height))
background = load_image("assets/images/background.png")

game_state = GameState()

# Sound init
music_img, music_muted_img, music_rect = load_music_images()
sound_img, sound_muted_img, sound_rect = load_sound_images()


def main():

    # Initialize variables
    music_muted = False
    sound_muted = False
    difficulty_levels = ["Easy", "Medium", "Hard"]
    difficulty_index = 0
    current_difficulty = difficulty_levels[difficulty_index]  

    while True:

        # Menu screen
        if game_state.state == "MENU":

            screen.blit(background, (0, 0))

            # UI 
            draw_title(screen)
            draw_music_button(screen, music_muted, music_img, music_muted_img, music_rect)
            draw_sound_button(screen, sound_muted, sound_img, sound_muted_img, sound_rect)
            draw_menu_fruits(screen)
            play_rect = new_game_button(screen)
            difficulty_rect = draw_difficulty_button(screen, current_difficulty)
            score_rect = draw_score_button(screen)

            # Buttons and events
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                music_muted = button_music_click(event, music_rect, music_muted)
                sound_muted = button_sound_click(event, sound_rect, sound_muted)

                if game_button_click(event, play_rect):
                    while True:
                        reset_gameplay_state(game_state)
                        game_state.state = "GAME"
                        decision = game_screen(screen, clock, game_state)

                        if decision == "RESTART":
                            continue   # Start new game
                        break          # Back to main menu

                if difficulty_button_click(event, difficulty_rect):
                    difficulty_index = (difficulty_index + 1) % len(difficulty_levels)
                    current_difficulty = difficulty_levels[difficulty_index] 
                    game_state.difficulty = current_difficulty  

                if score_button_click(event, score_rect):
                    print("Score screen opened !") # Placeholder for menu screen 

            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    main()
