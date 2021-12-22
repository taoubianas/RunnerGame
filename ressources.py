import pygame
class ressources:
    runImages = []
    jampImages=[]
    def __init__(self, scal=1):
        for i in range(8):
            self.runImages.append(pygame.image.load("Run ("+ str(i+1) + ").png"))
            size= self.runImages[i].get_size()
            self.runImages[i]= pygame.transform.scale(self.runImages[i],  (size[0]*scal, size[1]* scal))

        for i in range(8):
            self.jampImages.append(pygame.image.load("Jump ("+ str(i+1) + ").png"))
            size= self.jampImages[i].get_size()
            self.jampImages[i]= pygame.transform.scale(self.jampImages[i],  (size[0]*scal, size[1]* scal))



