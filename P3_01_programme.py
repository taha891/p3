import pygame
from pygame.locals import *
from classe import *
from constantes import *

# Affichage premier ecran


pygame.init()

win = pygame.display.set_mode((640, 480), RESIZABLE)
# Personnage princpal
char = pygame.image.load(IMAGE_MACGYVER).convert()
# Objets spéciaux
winner = pygame.image.load(IMAGE_WIN).convert()
lose = pygame.image.load(IMAGE_LOSE).convert()


pygame.display.set_caption('ACCUEIL')

pygame.display.flip()
#Affichage labyrinthe
labyrinthe = Labyrinthe('labyrinthe.txt')
#Affichage personnage et objets
perso = Macgayver(labyrinthe)
ether = Special_Objects(labyrinthe,IMAGE_ETHER)
tube = Special_Objects(labyrinthe,IMAGE_TUBE)
needle = Special_Objects(labyrinthe,IMAGE_NEEDLE)



pygame.display.flip()

      

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    # Affichage labyrinthe du jeu
    labyrinthe.show(win)
    ether.show_special(win)
    tube.show_special(win)
    needle.show_special(win)
    
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
    ether.show_special(win)
    tube.show_special(win)
    needle.show_special(win)
    win.blit(char,(perso.x, perso.y))
    pygame.display.flip()

    # test
    
    
        #pygame.display.flip()
        
# Objets spéciaux
    


# Mort du perso
    if labyrinthe.structure[perso.case_y][perso.case_x] == 'a' and perso.compteur < 3:
        win.blit(lose, (100,100))
        pygame.display.flip()
        continuer = 0
        
        pygame.quit()
        
# arrivée
    
    if labyrinthe.structure[perso.case_y][perso.case_x] == 'a' and perso.compteur == 3:
        sound3 = pygame.mixer.Sound(SOUND_WIN)
        sound3.play()
        win.blit(winner, (150,200))
        pygame.display.flip()
        continuer = 0
        pygame.quit()
