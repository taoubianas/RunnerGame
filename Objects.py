import pygame
class Objects:
    timeIndex=0
    cactSpeed=3
    cactusArray=[]
    hitBox=[]
    j=0
    def __init__(self,screen,initalPos, scal=1):
        self.objectImag=pygame.image.load("Objects/Cactus (1).png")
        size= self.objectImag.get_size()
        self.objectImag= pygame.transform.scale(self.objectImag,  (int(size[0]*scal), int (size[1]* scal)))
        self.screen=screen
        self.cactuSize= self.objectImag.get_size()
        self.initalPos=(initalPos[0],initalPos[1]-self.cactuSize[1])

    def animate(self):
        #largeurScreen, longeurScreen=self.screen.get_size()
        self.timeIndex += self.cactSpeed
        if(self.timeIndex>200):
            self.timeIndex=0
            self.cactusArray.append(self.initalPos)
            self.hitBox.append(())
        for i in range( len(self.cactusArray)):
            self.screen.blit(self.objectImag,self.cactusArray[i])
            self.cactusArray[i]=(self.cactusArray[i][0]-self.cactSpeed,self.cactusArray[i][1])
            self.hitBox[i] = (self.cactusArray[i][0],self.cactusArray[i][1],self.cactuSize[0],self.cactuSize[1])  #      
            pygame.draw.rect(self.screen,(255,255,255),self.hitBox[i],2)        #

    def right(self,i):
        return self.hitBox[i][0]+self.hitBox[i][2]
    def left(self,i):
        return self.hitBox[i][0] 
    def top(self,i):
        return self.hitBox[i][1]
    def bottom(self,i):
        return self.hitBox[i][1]+self.hitBox[i][3]   

    def deadHit(self,Char):
        
        for i in range(len(self.hitBox)):
            if( Char.deadHit(self,i)):
                print("dead" + str(self.j))
                self.j+=1


        

            
        