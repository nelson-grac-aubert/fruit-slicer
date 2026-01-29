import json 
import os
import pygame
from game_classes import GameState
from game_assets import resource_path
from game_assets import load_font, load_image
from sound_control import *
from main_menu_display import draw_back_button, back_button_click

def get_scores() : 
    """ Get scores from scores.json """

    # Use path function
    path = resource_path('scores.json')

    # Read the scores and return them as a list of dictionnaries
    if os.path.exists(path) :                       # If file exists
        with open(path, 'r', encoding='utf-8') as f:
            try : 
                scores = json.load(f)
            except json.JSONDecodeError :           # Error management
                scores = []
            
    else : 
        scores = []

    return scores


def get_best_scores() :
    """ Get 10 highest scores for display in leaderboard """

    scores = get_scores()
    return scores[:10]


def save_score(game_state, player_name) : 
    """ Save score at the end of the game"""

    path = resource_path('scores.json')     # Use path function
    scores = get_scores()                   # Get scores if they exist

    # Add current entry to scores
    scores.append({"player" : player_name , "score" : game_state.score}) 

    # Sort scores from highest to lowest before writing them in json
    scores.sort(key=lambda x: x["score"], reverse=True)

    # Dump updated scores into scores.json
    with open(path, 'w', encoding="utf-8") as f : 
        json.dump(scores, f, ensure_ascii=False, indent=4)  # Dont convert special characters into unicode

    return scores


def open_player_name_input(screen, game_state) : 
    """ On clicking save score on game over screen, opens an input box for the player to 
    enter his name for the leaderboard """

    # UI
    background = load_image("assets/images/background.png")
    screen.blit(background, (0, 0))
    back_rect = draw_back_button(screen, (1100,640))

    # Initialize font and empty name
    input_font = load_font("assets/fonts/pixelify_sans.ttf", 64)
    name = ""

    # Input rectangle
    input_rect = pygame.Rect(250, 300, 300, 60)

    while True:
        # Background
        screen.blit(background, (0, 0))

        # Text
        text_position = (50,50)
        instructions_label = input_font.render("Enter your name then press Enter:", True, (255, 255, 255))
        screen.blit(instructions_label, text_position)

        # Draw input rectangle
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 2)

        # Display name in rectangle
        name_surf = input_font.render(name, True, (255, 255, 255))
        screen.blit(name_surf, (input_rect.x + 10, input_rect.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Back to main menu button
            if back_button_click(event, back_rect):
                game_state.state = "MENU"
                return

            # Add letter to name
            if event.type == pygame.KEYDOWN:
                # Return name on typing enter
                if event.key == pygame.K_RETURN:
                    return name.strip()
                
                # Remove letter
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]

                # Add letter, max 15
                else:
                    if len(name) < 15:
                        name += event.unicode