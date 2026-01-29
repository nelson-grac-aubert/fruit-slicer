# language.py

LANGUAGES = {
    "fr": {
        "play": "Jouer",
        "quit": "Quitter",
        "score":"Score",
        "leave": "Voulez-vous vraiment quittez le jeu ?",
        "difficulty": "Difficulté",

        "easy": "Facile",
        "normal": "Normal",
        "hard": "Difficile"
    },

    "en": {
        "play": "Play",
        "quit": "Quit",
        "score": "Score",
        "leave": "Do you really want to quit the game ?",
        "difficulty": "Difficulty",

        "easy": "Easy",
        "normal": "Normal",
        "hard": "Hard"
    }
}

current_language = "fr"

def set_language(lang):
    global current_language
    current_language = lang

def text(key):
    return LANGUAGES[current_language][key]
