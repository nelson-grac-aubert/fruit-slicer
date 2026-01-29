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
        self._load()