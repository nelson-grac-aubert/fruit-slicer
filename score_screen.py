import pygame

from score_management import get_best_scores
from sound_control import * 
from game_assets import * 
from main_menu_display import draw_back_button

def draw_title(screen):
    """ Draws Leaderboard on top of the screen """

    # Centered horizontally, on top vertically
    title_position = (screen.get_width() // 2, 100)
    title_color = (255, 147, 147)
    title_size = 128

    title_font = load_font(("assets/fonts/pixelify_sans.ttf"), title_size)
    title_surface = title_font.render("Leaderboard", True, title_color)
    
    title_rect = title_surface.get_rect(center = title_position)
    screen.blit(title_surface, title_rect)

def draw_scores(screen) : 
    """ Draws 10 best score on the screen """

    # Get 10 best scores from .json
    scores = get_best_scores()

    # Centered horizontally, below "Leaderboard"
    score_x = screen.get_width() // 2
    score_start_y = 200 
    spacing = 52
    scores_color = (255, 147, 147)
    scores_size = 48

    # Font
    scores_font = load_font(("assets/fonts/pixelify_sans.ttf"), scores_size)
    
    # Draw scores one by one in format : #. Name - Score
    for i, entry in enumerate(scores):
        text = f"{i+1}. {entry['player']} - {entry['score']}"
        score_surface = scores_font.render(text, True, scores_color)
        score_rect = score_surface.get_rect(center=(score_x, score_start_y + i * spacing))
        screen.blit(score_surface, score_rect)

def score_screen(screen, clock, game_state, background,
                 music_muted, sound_muted,
                 music_img, music_muted_img, music_rect,
                 sound_img, sound_muted_img, sound_rect):

    while True:
        # Background
        screen.blit(background, (0, 0))

        # UI
        draw_title(screen)
        draw_scores(screen)
        draw_music_button(screen, music_muted, music_img, music_muted_img, music_rect)
        draw_sound_button(screen, sound_muted, sound_img, sound_muted_img, sound_rect)
        back_rect = draw_back_button(screen, (1100,640))

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "QUIT", music_muted, sound_muted

            # Mute/Unmute
            music_muted = button_music_click(event, music_rect, music_muted)
            sound_muted = button_sound_click(event, sound_rect, sound_muted)

            # Return to menu
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_rect.collidepoint(event.pos):
                    game_state.state = "MENU"
                    return "MENU", music_muted, sound_muted

        pygame.display.flip()
        clock.tick(60)