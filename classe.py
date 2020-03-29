import pygame
import random
from constantes import *


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
                        #print(x,y)
                        
                level_lab.append(level_line)
                y += 1
                pos = []
                #Obtenir la position des cases
                #return
        self.structure = level_lab
        
        
    #afficher labyrinthe
    def show(self, win):
        wall = pygame.image.load(image_wall).convert()
        departure = pygame.image.load(image_departure).convert()
        arrival = pygame.image.load(image_guard).convert()
        path = pygame.image.load(image_path).convert()
        needle = pygame.image.load(image_needle).convert()
        tube = pygame.image.load(image_tube).convert()
        ether = pygame.image.load(image_ether).convert()

        available_pos = []
        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                x = num_case * taille_sprite
                y = num_line * taille_sprite
                self.compteur = 0
                if sprite == 'a':
                    win.blit(arrival, (x,y))
                elif sprite == 'm':
                    win.blit(wall, (x,y))
                elif sprite == '0':
                    win.blit(path, (x,y))
                    available_pos.append((num_case,num_line))
                elif sprite == 'd':
                    win.blit(departure, (x,y))
                elif sprite == 't':
                    win.blit(tube, (x,y))
                elif sprite == 'n':
                    win.blit(needle, (x,y))
                elif sprite == 'e':
                    win.blit(ether, (x,y))
                num_case +=1
            num_line +=1

        
            #print(available_pos)
                    
       
        # PAS DE ELSE PAS UN PROBLEME ?
       
        
    # Liste des positions
    
    #def create_items_list(self):
    #    """Method that adds items in a list"""

     #   for i in range(0, self.item_numbers):
    #      self.items_list.append(Item(self))
    
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
        if direction == 'up':
            if self.case_y > 0:
                if self.structure[self.case_y-1][self.case_x] != 'm':
                    if self.structure[self.case_y-1][self.case_x] == 't' or self.structure[self.case_y-1][self.case_x] == 'n' or self.structure[self.case_y-1][self.case_x] == 'e':
                        
                        self.case_y -= 1
                        self.y = self.case_y * taille_sprite
                        self.compteur += 1
                        self.structure[self.case_y][self.case_x] = '0'
                    else:
                        self.case_y -= 1
                        self.y = self.case_y * taille_sprite
                    
                    
                        #print (str(self.case_x))
                        #print (str(self.case_y))
              
        if direction == 'down':
            if self.case_y < (nombre_sprite_cote - 1):
                if self.structure[self.case_y+1][self.case_x] != 'm':
                    if self.structure[self.case_y+1][self.case_x] == 't' or self.structure[self.case_y+1][self.case_x] == 'n' or self.structure[self.case_y+1][self.case_x] == 'e':
                        self.case_y += 1
                        self.y = self.case_y * taille_sprite
                        self.compteur += 1
                        self.structure[self.case_y][self.case_x] = '0'
                    else:
                        self.case_y +=1
                        self.y = self.case_y * taille_sprite
                    
        if direction == 'right':
            if self.case_x < (nombre_sprite_cote - 1):
                if self.structure[self.case_y][self.case_x+1] != 'm':
                    if self.structure[self.case_y][self.case_x+1] == 't' or self.structure[self.case_y][self.case_x+1] == 'n' or self.structure[self.case_y][self.case_x+1] == 'e':
                        self.case_x += 1
                        self.x = self.case_x * taille_sprite
                        self.structure[self.case_y][self.case_x] = '0'
                        self.compteur += 1
                    else:
                        self.case_x += 1
                        self.x = self.case_x * taille_sprite
                        self.y = self.case_y * taille_sprite
                   
            
        if direction == 'left':
            if self.case_x > 0:
                if self.structure[self.case_y][self.case_x-1] != 'm':
                    if self.structure[self.case_y][self.case_x-1] == 't' or self.structure[self.case_y][self.case_x-1] == 'n' or self.structure[self.case_y][self.case_x-1] == 'e':
                        self.case_x -= 1
                        self.x = self.case_x * taille_sprite
                        self.structure[self.case_y][self.case_x] = '0'
                        self.compteur += 1
                    else:
                        self.case_x -= 1
                        self.x = self.case_x * taille_sprite
                        self.y = self.case_y * taille_sprite
                    
                    
# Attraper objet                    
#    def compteur(self, catch_objects):
#        self.catch_objects = 0
#        if self.structure[self.case_y][self.case_x] == 't':
#            self.catch_objects += 1
#            return catch_objects
#            self.structure[self.case_y][self.case_x] = '0'
            # en ajoutant cette modif il avance de + d'une case ( modifier pour qu'il avance d'une case)
# est-ce que la case est un objet
#si case = objet
#compteur = ajoute 1 à l'inventaire



# Comment matérialiser que la case doit être vide

#https://stackoverflow.com/questions/50859819/pygame-making-things-move-slower-than-1
#si c'est un objet et on met un compteur inventaire avec variable i find_objects = 0


