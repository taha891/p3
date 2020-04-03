import pygame
import random
from constantes import *

available_pos = []
available_case = []

class Labyrinthe:

    #générer labyrinthe
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = []


    
        with open(self.fichier, 'r') as fichier:
            level_lab = []
            y = 0
            for line in fichier:
                level_line = []
                x = 0
                
                for sprite in line:
                    if sprite != '\n':
                        level_line.append(sprite)
                        x += 1
                        
                        
                level_lab.append(level_line)
                y += 1
                pos = []
                #Obtenir la position des cases
                #return
        self.structure = level_lab

    
        
    #afficher labyrinthe
    def show(self, win):
        wall = pygame.image.load(IMAGE_WALL).convert()
        departure = pygame.image.load(IMAGE_DEPARTURE).convert()
        arrival = pygame.image.load(IMAGE_GUARD).convert()
        path = pygame.image.load(IMAGE_PATH).convert()
        needle = pygame.image.load(IMAGE_NEEDLE).convert()
        tube = pygame.image.load(IMAGE_TUBE).convert()
        ether = pygame.image.load(IMAGE_ETHER).convert()

        
        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                x = num_case * TAILLE_SPRITE
                y = num_line * TAILLE_SPRITE
                self.compteur = 0
                if sprite == 'a':
                    win.blit(arrival, (x,y))
                elif sprite == 'm':
                    win.blit(wall, (x,y))
                elif sprite == '0':
                    win.blit(path, (x,y))
                    available_case.append((num_case,num_line)) 
                elif sprite == 'd':
                    win.blit(departure, (x,y))

                num_case +=1
            num_line +=1

class Macgayver:
    def __init__(self, lab):
    #Position perso en cases et en pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.structure = lab.structure
        self.compteur = 0
        
    # Methode deplacement perso
    def move(self, direction):
        sound1 = pygame.mixer.Sound(SOUND_MOVE)
        sound2 = pygame.mixer.Sound(SOUND_GOT_ITEM)
        if direction == 'up':
            if self.case_y > 0:
                if self.structure[self.case_y-1][self.case_x] != 'm':
                    if self.structure[self.case_y-1][self.case_x] == 'i':
                        self.case_y -= 1
                        #sound1.play()
                        self.y = self.case_y * TAILLE_SPRITE
                        self.compteur += 1
                        sound2.play()
                        self.structure[self.case_y][self.case_x] = '0'
                    else:
                        self.case_y -= 1
                        #sound1.play()
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
                        self.case_y +=1
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
                        self.y = self.case_y * TAILLE_SPRITE
                   
            
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
                        self.y = self.case_y * TAILLE_SPRITE
                    
                    

class Special_Objects:
    
    def __init__(self, lab, image):
        self.case_x = random.randint(0,14)
        self.case_y = random.randint(0,14)
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(image).convert()
        self.structure = lab.structure
        self.structure[self.case_y][self.case_x] = 'i'
        
    def show_special(self, win):
        self.x = self.case_x * TAILLE_SPRITE
        self.y = self.case_y * TAILLE_SPRITE     

        if self.structure[self.case_y][self.case_x] != 'm' and self.structure[self.case_y][self.case_x] != 'a' and self.structure[self.case_y][self.case_x] != 'd':
            
            if self.structure[self.case_y][self.case_x] == 'i':
            
                win.blit(self.image, (self.x, self.y))
            


