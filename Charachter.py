import pygame
from ressources import ressources

class Charachter:
    runIndex=0
    jumpIndex=0
    etat=0
    res=ressources(0.2)
    jumpRange=0
    jumpDistance=0
    initPos = (0,0)                         #
    size = res.runImages[0].get_size()      #
    hitBox = (initPos[0],initPos[1],size[0],size[1])   #
    pos=() #
    def __init__(self,screen,initPos=(0,0),jumpRange=100):
        self.screen=screen
        self.initPos= (initPos[0],(initPos[1]-self.size[1]))
        self.jumpRange = jumpRange
    def animate(self):
        if (self.etat==0):
            self.running()
        else:
            self.jumping()
        self.hitBox = (self.pos[0]+(50/193)*self.size[0],self.initPos[1]-self.jumpDistance+(22/193)*self.size[1],self.size[0]*80/193,self.size[1]*134/160)     
        self.drawHitBox() ##
            

    def jump(self):
        self.etat=1

    def running(self):
        self.pos=self.initPos
        self.screen.blit(self.res.runImages[int(self.runIndex)],self.initPos)
        self.runIndex+=0.3
        if(self.runIndex>7):
            self.runIndex=0

    def jumping(self):
        self.jumpDistance=self.jumpRange-((self.jumpIndex/5-1)*(self.jumpIndex/5-1))*self.jumpRange
        pos = (self.initPos[0],self.initPos[1]-self.jumpDistance)
        self.screen.blit(self.res.jumpImages[int(self.jumpIndex)],pos)
        #self.hitBox = (self.initPos[0],self.initPos[1]-self.jumpDistance,self.size[0],self.size[1])     #   
        #self.drawHitBox()                                                     #
        self.jumpIndex+=0.2
        if(self.jumpIndex>10):
            self.jumpIndex=0
            self.etat=0

    def drawHitBox(self):
        pygame.draw.rect(self.screen,(255,255,255),self.hitBox,2)
#otherHitbox =objet
    def deadHit(self,objet,i):
        if objet.right(i)< self.left():
            return False
        if objet.bottom(i)< self.top():
            return False
        if objet.left(i)> self.right():
            return False
        if objet.top(i)> self.bottom():
            return False
        return True

    def right(self):
        return self.hitBox[0]+self.hitBox[2]
    def left(self):
        return self.hitBox[0] 
    def top(self):
        return self.hitBox[1]
    def bottom(self):
        return self.hitBox[1]+self.hitBox[3]  

