import os
import sys
import pygame

def resource_path(relative_path: str) -> str:
    """
    Returns the absolute path to an asset, PyInstaller compatible
    - Through IDE and Python files : uses normal path.
    - Through Pyinstaller builder for .exe : uses temportary MEIPASS dir. 
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

import os
import sys
import pygame


def resource_path(relative_path: str) -> str:
    """
    Retourne le chemin absolu vers un asset, compatible PyInstaller.
    - En IDE : utilise le chemin normal.
    - En .exe PyInstaller : utilise le dossier temporaire MEIPASS.
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def load_image(path: str) -> pygame.Surface:
    """
    Load an image through resource_path
    convert_alpha for a transparent background .png
    """
    full_path = resource_path(path)
    try:
        image = pygame.image.load(full_path)
        return image.convert_alpha()
    except Exception as e:
        raise FileNotFoundError(f"Impossible de charger l’image : {full_path}\n{e}")


def load_sound(path: str) -> pygame.mixer.Sound:
    """
    Load sound through resource_path
    """
    full_path = resource_path(path)
    try:
        return pygame.mixer.Sound(full_path)
    except Exception as e:
        raise FileNotFoundError(f"Impossible de charger le son : {full_path}\n{e}")


def load_font(path: str, size: int) -> pygame.font.Font:
    """
    Load font through resource_path
    """
    full_path = resource_path(path)
    try:
        return pygame.font.Font(full_path, size)
    except Exception as e:
        raise FileNotFoundError(f"Impossible de charger la police : {full_path}\n{e}")
    

# EXEMPLES
fruits_images = load_image("assets/images/fruits_assets.png")
pixel_font = load_font("assets/fonts/pixelify_sans.tff")
ice_sound = load_sound("assets/sounds/ice.mp3")
