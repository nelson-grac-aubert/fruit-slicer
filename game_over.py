import pygame
from game_assets import * 

def draw_game_over_title(screen):
    """ Blits Game Over Title on game loss """

    # Game Over text
    font = load_font("assets/fonts/pixelify_sans.ttf", 80)
    text = font.render("GAME OVER", True, (255, 80, 80))
    rect = text.get_rect(center=(600, 150))

    # Make a black rectangle bigger than the text rectangle 
    pygame.draw.rect(screen, (0, 0, 0), rect.inflate(60, 30))
    screen.blit(text, rect)


def save_final_score(game_state) : 
    """ Save final score before resetting it for display and leaderboard """

    return game_state.score


def display_final_score(screen, final_score) : 
    """ Blits score on Game Over Screen """

    # Final score
    font = load_font("assets/fonts/pixelify_sans.ttf", 48)
    text = font.render(f"YOUR SCORE : {final_score}", True, (255, 255, 255))
    rect = text.get_rect(center=(600, 275))

    # Make a black rectangle bigger than the text rectangle  
    pygame.draw.rect(screen, (40, 40, 40), rect.inflate(40, 20), border_radius=8)
    screen.blit(text, rect)

    return rect


def draw_save_score_button(screen) : 
    """ Draws save score button on game loss """

    # Final score
    font = load_font("assets/fonts/pixelify_sans.ttf", 48)
    text = font.render(f"SAVE SCORE", True, (255, 255, 255))
    rect = text.get_rect(center=(600, 375))

    # Make a black rectangle bigger than the text rectangle  
    pygame.draw.rect(screen, (40, 40, 40), rect.inflate(40, 20), border_radius=8)
    screen.blit(text, rect)

    return rect

def draw_play_again_button(screen):
    """ Blits play again button on game loss """

    # Text
    font = load_font("assets/fonts/pixelify_sans.ttf", 48)
    text = font.render("PLAY AGAIN", True, (255, 255, 255))
    rect = text.get_rect(center=(600, 475))

    # Make a black rectangle bigger than the text rectangle 
    pygame.draw.rect(screen, (40, 40, 40), rect.inflate(40, 20), border_radius=8)
    screen.blit(text, rect)

    return rect


def draw_main_menu_button(screen):
    """ Blits back to main menu button on game loss """

    # Text
    font = load_font("assets/fonts/pixelify_sans.ttf", 48)
    text = font.render("MAIN MENU", True, (255, 255, 255))
    rect = text.get_rect(center=(600, 575))

    # Make a black rectangle bigger than the text rectangle 
    pygame.draw.rect(screen, (40, 40, 40), rect.inflate(40, 20), border_radius=8)
    screen.blit(text, rect)

    return rect


def game_over_screen(screen, final_score):
    """ Displays end of game screen with play again and main menu button """

    while True:
        screen.fill((20, 20, 20))

        # Title
        draw_game_over_title(screen)
        display_final_score(screen, final_score)

        # Buttons
        save_rect = draw_save_score_button(screen)
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
                if save_rect.collidepoint(event.pos):
                    return "SAVE"

        pygame.display.flip()