import pygame
from pygame.locals import *



screens=["main","game","paused","result","tutorial"]
gameState = screens[0]

pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Defender")
done = False
clock = pygame.time.Clock()

while True:
    if(gameState=="main"):
        screen.fill(pygame.Color(255,0,0))

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                gameState = "game"

    if(gameState=="game"):
        screen.fill(pygame.Color(0,0,0))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
                
                        
            
    pygame.display.update()
    clock.tick(60)

        
        




#player 
class Player:
    def __init__(self,Username,playerClass,combatLevel):
        self.name = Username
        self.Class = playerClass
        self.combatLevel = combatLevel

    def getName(self):
        return self.name
    def getCombat(self):
        return self.combatLevel
    def setCombat(self,lvl):
        self.combatLevel = lvl
    
