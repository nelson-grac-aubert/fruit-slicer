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
from score_screen import score_screen
from score_management import open_player_name_input, save_score

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

    # Initialize main menu variables
    show_exit_confirm = False
    yes_rect = None
    no_rect = None
    music_muted = False
    sound_muted = False
    difficulty_levels = ["Easy", "Medium", "Hard"]
    difficulty_index = 0
    current_difficulty = difficulty_levels[difficulty_index]  

    while True:

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
            exit_rect = draw_exit_button(screen)

            # EVENTS
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                # Music / sound
                music_muted = button_music_click(event, music_rect, music_muted)
                sound_muted = button_sound_click(event, sound_rect, sound_muted)

                # Exit button
                if exit_button_click(event, exit_rect):
                    show_exit_confirm = True

                # If confirmation window is open
                if show_exit_confirm:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if yes_rect and yes_rect.collidepoint(event.pos):
                            pygame.quit()
                            return
                        if no_rect and no_rect.collidepoint(event.pos):
                            show_exit_confirm = False
                    continue  # ignore other buttons while popup is open

                # New game
                if game_button_click(event, play_rect):
                    while True:
                        reset_gameplay_state(game_state)
                        game_state.state = "GAME"
                        decision = game_screen(screen, clock, game_state)
                        if decision == "RESTART":
                            continue                    # Start new game

                        elif decision == "SAVE" :       # Save player score
                            name = open_player_name_input(screen, game_state)
                            save_score(game_state, name)
                            game_state.state = "MENU"

                        break                            # Back to main menu
                        
                if difficulty_button_click(event, difficulty_rect):
                    difficulty_index = (difficulty_index + 1) % len(difficulty_levels)
                    current_difficulty = difficulty_levels[difficulty_index]
                    game_state.difficulty = current_difficulty

                # Score
                if score_button_click(event, score_rect):
                    decision, music_muted, sound_muted = score_screen(
                        screen, clock, game_state, background,
                        music_muted, sound_muted,
                        music_img, music_muted_img, music_rect,
                        sound_img, sound_muted_img, sound_rect
                    )
                    if decision == "QUIT":
                        return

            # Draw confirmation popup if needed
            if show_exit_confirm:
                yes_rect, no_rect = draw_exit_confirmation(screen)

            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    main()
