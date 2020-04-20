import pygame
from constantes import NOMBRE_SPRITE_COTE, TAILLE_SPRITE, SOUND_GOT_ITEM


class Macgayver:
    ''' This class represents the Hero Macgayver and his actions'''

    def __init__(self, lab):
        ''' The Hero constructor with positions'''
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.structure = lab.structure
        self.compteur = 0

    def move(self, direction):
        ''' This method allow the Hero to move '''
        sound2 = pygame.mixer.Sound(SOUND_GOT_ITEM)
        if direction == 'up':
            if self.case_y > 0:
                if self.structure[self.case_y-1][self.case_x] != 'm':
                    if self.structure[self.case_y-1][self.case_x] == 'i':
                        self.case_y -= 1
                        self.y = self.case_y * TAILLE_SPRITE
                        self.compteur += 1
                        sound2.play()
                        self.structure[self.case_y][self.case_x] = '0'
                    else:
                        self.case_y -= 1
                        self.y = self.case_y * TAILLE_SPRITE
        if direction == 'down':
            if self.case_y < (NOMBRE_SPRITE_COTE - 1):
                if self.structure[self.case_y+1][self.case_x] != 'm':
                    if self.structure[self.case_y+1][self.case_x] == 'i':
                        self.case_y += 1
                        self.y = self.case_y * TAILLE_SPRITE
                        self.compteur += 1
                        sound2.play()
                        self.structure[self.case_y][self.case_x] = '0'
                    else:
                        self.case_y += 1
                        self.y = self.case_y * TAILLE_SPRITE

        if direction == 'right':
            if self.case_x < (NOMBRE_SPRITE_COTE - 1):
                if self.structure[self.case_y][self.case_x+1] != 'm':
                    if self.structure[self.case_y][self.case_x+1] == 'i':
                        self.case_x += 1
                        self.x = self.case_x * TAILLE_SPRITE
                        self.structure[self.case_y][self.case_x] = '0'
                        self.compteur += 1
                        sound2.play()
                    else:
                        self.case_x += 1
                        self.x = self.case_x * TAILLE_SPRITE
        if direction == 'left':
            if self.case_x > 0:
                if self.structure[self.case_y][self.case_x-1] != 'm':
                    if self.structure[self.case_y][self.case_x-1] == 'i':
                        self.case_x -= 1
                        self.x = self.case_x * TAILLE_SPRITE
                        self.structure[self.case_y][self.case_x] = '0'
                        self.compteur += 1
                        sound2.play()
                    else:
                        self.case_x -= 1
                        self.x = self.case_x * TAILLE_SPRITE
