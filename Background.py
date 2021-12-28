import pygame
class Background:
    posInit=(0,0)
    movingSpeed=10
    moveIndex=0
    speedOffcet=movingSpeed*0.1
    offcet=0
    def __init__(self,screen,posH, scal=0.7):
            self.backgroundImag=pygame.image.load("Jungle/jungle_pack_05.png")
            self.backgroundim=pygame.image.load("Jungle/bg_jungle.png")
            size= self.backgroundImag.get_size()
            self.backgroundImag= pygame.transform.scale(self.backgroundImag,  (size[0]*scal, size[1]* scal))
            size= self.backgroundim.get_size()
            self.backgroundim= pygame.transform.scale(self.backgroundim,  (size[0]*scal, size[1]* scal))
            self.screen=screen
            self.posInit=posH
    
    def animate(self):
        largeurScreen, longeurScreen=self.screen.get_size()
        
        #background
        largeurImage, longeurImage=self.backgroundim.get_size()
        pos = (self.posInit[0]-self.offcet,0)
        self.screen.blit(self.backgroundim,pos)
        pos1 = (-self.offcet+largeurImage,0)
        self.screen.blit(self.backgroundim,pos1)
        self.offcet=self.offcet+self.speedOffcet
        if(self.offcet>largeurScreen):
            self.offcet = 0
        


        largeurImage, longeurImage=self.backgroundImag.get_size()
        for i in range(int (largeurScreen/largeurImage)+2):
            pos = (self.posInit[0]+i*largeurImage-self.moveIndex,self.posInit[1])
            self.screen.blit(self.backgroundImag,pos)
        self.moveIndex=self.moveIndex+self.movingSpeed
        if(self.moveIndex>largeurImage):
            self.moveIndex = 0

