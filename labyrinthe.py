import pygame
from constantes import IMAGE_WALL, IMAGE_DEPARTURE, IMAGE_GUARD
from constantes import IMAGE_PATH, TAILLE_SPRITE


class Labyrinthe:
    """ This class is the stucture of the maze"""

    def __init__(self, fichier):
        """ maze constructor"""
        self.fichier = fichier
        self.structure = []
        with open(self.fichier, "r") as fichier:
            level_lab = []
            y = 0
            for line in fichier:
                level_line = []
                x = 0
                for sprite in line:
                    if sprite != "\n":
                        level_line.append(sprite)
                        x += 1
                level_lab.append(level_line)
                y += 1
        self.structure = level_lab

    def show(self, win):
        """ This method display the maze"""
        wall = pygame.image.load(IMAGE_WALL).convert()
        departure = pygame.image.load(IMAGE_DEPARTURE).convert()
        arrival = pygame.image.load(IMAGE_GUARD).convert()
        path = pygame.image.load(IMAGE_PATH).convert()

        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                x = num_case * TAILLE_SPRITE
                y = num_line * TAILLE_SPRITE
                if sprite == "a":
                    win.blit(arrival, (x, y))
                elif sprite == "m":
                    win.blit(wall, (x, y))
                elif sprite == "0":
                    win.blit(path, (x, y))
                elif sprite == "d":
                    win.blit(departure, (x, y))
                num_case += 1
            num_line += 1
