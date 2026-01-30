# Pixel Cutter

## Introduction
Pixel Cutter is a lightweight, keyboard‑controlled slicing game made with Python and Pygame.  
No mouse input — all gameplay is driven by the keyboard.

## Features
- Flying fruits to slice  
- Bombs that reduce score  
- Ice power‑up that freezes the game state  
- Secret bonus item  
- Simple score system and UI

## Dependencies
Install Pygame:
```bash
pip install pygame
```
Standard libraries used : random, time

## Build with pyinstaller : 
```bash
pyinstaller --noconfirm --windowed --name "Pixel Cutter" --icon "assets/images/logo.ico" --add-data "assets;assets" --add-data "scores.json" main.py
```

## Dev difficulties : 
- First time using Classes, OOP
- Adding language support late in development was challenging

## Possible improvements : 
- Different game modes
- Mouse support
- Harder difficulty options
- Alternate sprite themes instead of fruits


## Authors : 
Yannis Sandoval, Angelina Pellat, Nelson Grac-Aubert
