import pygame
from constantes import *


class Labyrinthe:

    #générer labyrinthe
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = []


    
        with open(self.fichier, 'r') as fichier:
            level_lab = []
            for line in fichier:
                level_line = []

                for sprite in line:
                    if sprite != '\n':
                        level_line.append(sprite)

                level_lab.append(level_line)
        self.structure = level_lab
        
        
    #afficher labyrinthe
    def show(self, win):
        wall = pygame.image.load(image_wall).convert()
        departure = pygame.image.load(image_departure).convert()
        arrival = pygame.image.load(image_guard).convert()
        path = pygame.image.load(image_path).convert()
        
        
        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                x = num_case * taille_sprite
                y = num_line * taille_sprite
                
                if sprite == 'a':
                    win.blit(arrival, (x,y))
                elif sprite == 'm':
                    win.blit(wall, (x,y))
                elif sprite == '0':
                    win.blit(path, (x,y))
                elif sprite == 'd':
                    win.blit(departure, (x,y))
                num_case +=1
            num_line +=1
            # Objets spéciaux: Aiguile, Tube, Ether    
    # Liste des positions
    '''def create_items_list(self):
        """Method that adds items in a list"""

        for i in range(0, self.item_numbers):
            self.items_list.append(Item(self))'''
    
class Macgayver:
    def __init__(self, lab):
        #Position perso en cases et en pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.structure = lab.structure
        min_case = 0
        max_case = 14
       

# Methode deplacement perso
    def move(self, direction):
        if direction == 'up':
            if self.case_y > 0:
                if self.structure[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * taille_sprite
                    print (str(self.case_x))
                    print (str(self.case_y))
                else:
                    pass
        if direction == 'down':
            if self.case_y < (nombre_sprite_cote - 1):
                if self.structure[self.case_x][self.case_y+1] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * taille_sprite
                    
                else:
                    pass
        if direction == 'right':
            if self.case_x < (nombre_sprite_cote - 1):
                if self.structure[self.case_y][self.case_x+1] != 'm':
                    self.case_x += 1
                    self.x = self.case_x * taille_sprite
                    self.y = self.case_y * taille_sprite
                    print (str(self.case_x))
                    print (str(self.case_y))
                else:
                    pass
            
        if direction == 'left':
            if self.case_x > 0:
                if self.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * taille_sprite
                    print (str(self.case_x))
                    print (str(self.case_y))
                else:
                    pass
            # en ajoutant cette modif il avance de + d'une case ( modifier pour qu'il avance d'une case)

# Recuperer position

# Attraper objet


class Special_Objects:
    # Création objet
    def __init__(self, lab):
        # Aiguille
        '''self.name = 'aiguille'
        self.position_x = random.randint(0, 14)
        self.position_y = random.randint(0, 14)'''
# Comment matérialiser que la case doit être vide


# si c'est un objet et on met un compteur
#inventaire avec variable i 
