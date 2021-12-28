import pygame
class ressources:
    runImages = []
    jumpImages=[]
    def __init__(self, scal=0.7):
        for i in range(8):
            self.runImages.append(pygame.image.load("images/Run ("+ str(i+1) + ").png"))
            size= self.runImages[i].get_size()
            self.runImages[i]= pygame.transform.scale(self.runImages[i],  (size[0]*scal, size[1]* scal))

        for i in range(10):
            self.jumpImages.append(pygame.image.load("images/Jump ("+ str(i+1) + ").png"))
            size= self.jumpImages[i].get_size()
            self.jumpImages[i]= pygame.transform.scale(self.jumpImages[i],  (size[0]*scal, size[1]* scal))



