import pygame
from random import randint
from constantes import TAILLE_SPRITE


class SpecialObjects:
    """ This class is dedicated to special objects that Hero must catch """

    def __init__(self, lab, image):
        """ Special objects constructor with the maze structure"""
        self.case_x = randint(0, 14)
        self.case_y = randint(0, 14)
        self.structure = lab.structure
        while self.structure[self.case_y][self.case_x] != "0":

            self.case_x = randint(0, 14)
            self.case_y = randint(0, 14)
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(image).convert()

        self.structure[self.case_y][self.case_x] = "i"

    def show_special(self, win):
        """ Method that displays special objects and activate count """
        self.x = self.case_x * TAILLE_SPRITE
        self.y = self.case_y * TAILLE_SPRITE

        if self.structure[self.case_y][self.case_x] == "i":
            win.blit(self.image, (self.x, self.y))
