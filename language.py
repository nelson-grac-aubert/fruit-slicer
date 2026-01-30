import pygame
from game_assets import load_image

class ActiveLanguage:
    """Centralize every text in the game for easy language toggle"""

    def __init__(self):
        self.texts = {
            "english": {
                "yes": "YES",
                "no": "NO",
                "new_game": "New Game",
                "leaderboard": "Leaderboard",
                "difficulty": "Difficulty",
                "easy": "Easy",
                "medium": "Medium",
                "hard": "Hard",
                "wish": "Do you wish to exit game?",
                "your_score": "Your score:",
                "save_score": "Save score",
                "play_again": "Play again",
                "main_menu": "Main menu",
            },
            "french": {
                "yes": "OUI",
                "no": "NON",
                "new_game": "Nouvelle Partie",
                "leaderboard": "Meilleurs scores",
                "difficulty": "Difficulté",
                "easy": "Facile",
                "medium": "Moyen",
                "hard": "Difficile",
                "wish": "Souhaitez-vous quitter le jeu?",
                "your_score": "Votre score:",
                "save_score": "Sauver score",
                "play_again": "Rejouer",
                "main_menu": "Menu principal",
            }
        }

        self.language = "english"
        self.load()


    def load(self):
        """Load all text keys into ActiveLanguage attributes."""

        lang_dict = self.texts[self.language]
        for key, value in lang_dict.items():
            setattr(self, key, value)


    def swap_language(self):
        """ Toggle between English and French """

        self.language = "french" if self.language == "english" else "english"
        self.load()


def load_language_button() : 
    """ Gets the variables for the language button """

    french_image = load_image("assets/images/french.png")
    english_image = load_image("assets/images/english.png")
    language_image_size = (65,65)
    french_image = pygame.transform.scale(french_image, (language_image_size))
    english_image = pygame.transform.scale(english_image, (language_image_size))

    language_image_position = (1140,50)
    french_image_rectangle = french_image.get_rect(center=(language_image_position))

    return french_image, english_image, french_image_rectangle

def draw_language_button(screen, current_language, french_image, english_image, rect):
    """ Draw swap language button """
    image = french_image if current_language.language == "english" else english_image
    screen.blit(image, rect)

def language_button_click(event, rect, current_language):
    """ Mute/unmute sound behavior """
    if event.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(event.pos):
        current_language.swap_language()
