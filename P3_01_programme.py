import pygame
from pygame.locals import *
from classe import *
''' This module contains all the project classes'''
from constantes import *
''' This module contains all constants : images, audios, values)'''

# -*- coding: utf-8 -*-

pygame.init()
'''Pygame initialization'''

# Window setting
win = pygame.display.set_mode((450, 480), RESIZABLE)
# Hero display
char = pygame.image.load(IMAGE_MACGYVER).convert()

winner = pygame.image.load(IMAGE_WIN).convert()
lose = pygame.image.load(IMAGE_LOSE).convert()
pygame.display.set_caption('ACCUEIL')

pygame.display.flip()
# Maze display
labyrinthe = Labyrinthe('labyrinthe.txt')
''' Display Hero and special objetcs '''
perso = Macgayver(labyrinthe)
ether = SpecialObjects(labyrinthe,IMAGE_ETHER)
tube = SpecialObjects(labyrinthe,IMAGE_TUBE)
needle = SpecialObjects(labyrinthe,IMAGE_NEEDLE)
pygame.display.flip()

game = 1
while game:
    continuer = 1
    ''' Game loop '''
    while continuer:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer = 0
                game = 0
                pygame.quit()
                exit()
        
        ''' Display of the maze '''
        labyrinthe.show(win)
        ether.show_special(win)
        tube.show_special(win)
        needle.show_special(win)
        win.blit(char,(perso.x, perso.y))
        pygame.display.flip()
            
        '''Move fuctions in pygame with keyboard actions '''        
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
            print(perso.compteur)

        '''New position and refresh of the maze structure, hero and objects'''
        labyrinthe.show(win)
        ether.show_special(win)
        tube.show_special(win)
        needle.show_special(win)
        win.blit(char,(perso.x, perso.y))
        pygame.display.flip()

        ''' Put the object catched outside the maze '''
        #ether_new = pygame.image.load(IMAGE_ETHER).convert()
        #win.blit(ether_new, (150, 450))

        '''Death of the Hero Event'''
        if labyrinthe.structure[perso.case_y][perso.case_x] == 'a' and perso.compteur < 3:
            win.blit(lose, (150,200))
            pygame.display.flip()
            continuer = 0
            #pygame.quit()

        ''' Win the game '''
        sound3 = pygame.mixer.Sound(SOUND_WIN)
        if labyrinthe.structure[perso.case_y][perso.case_x] == 'a' and perso.compteur == 3:
            sound3.play()
            win.blit(winner, (150,200))
            pygame.display.flip()
            continuer = 0
            #pygame.quit()
