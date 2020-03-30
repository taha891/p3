import pygame
from pygame.locals import *
from classe import *
from constantes import *

# Affichage premier ecran


pygame.init()

win = pygame.display.set_mode((640, 480), RESIZABLE)
# Personnage princpal
char = pygame.image.load(image_macgayver).convert()
# Objets spéciaux
needle = pygame.image.load(image_needle).convert()
tube = pygame.image.load(image_tube).convert()
ether = pygame.image.load(image_ether).convert()

pygame.display.set_caption('accueil')

pygame.display.flip()
#Affichage labyrinthe
labyrinthe = Labyrinthe('labyrinthe.txt')
#Affichage personnage et objets
perso = Macgayver(labyrinthe)
ether = Special_Objects()
tube = Special_Objects()
needle = Special_Objects()



pygame.display.flip()

      

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    # Affichage labyrinthe du jeu
    labyrinthe.show(win)
    
    win.blit(char,(perso.x, perso.y))
    
    pygame.display.flip()
    

    # Lancement du jeu

      
    #Deplacement
        
    if event.type == QUIT:
        continuer = 0
    elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            continuer = 0
        elif event.key == K_DOWN:
            perso.move('down')
            
        elif event.key == K_UP:
            perso.move('up')
            
        elif event.key == K_RIGHT:
            perso.move('right')
            
        elif event.key == K_LEFT:
            perso.move('left')
            
        #print(perso.case_x, perso.case_y)
        #catch_objects(perso)
        print(perso.compteur)
# Nouvelle position
    labyrinthe.show(win)
    win.blit(char,(perso.x, perso.y))
    ether.show_special(win)
    pygame.display.flip()

# Objets spéciaux
    
    '''labyrinthe = Position() Quand je mets ça le perso ne bouge plus
    perso = Position()'''

    # arrivée
    if labyrinthe.structure[perso.case_y][perso.case_x] == 'a' and perso.compteur == 3:
        continuer = 0
        pygame.quit()
