import sys
 
import pygame
from pygame.locals import *
from ressources import ressources
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
res = ressources(0.3)
i=0
print(res.runImages)
# Game loop.
while True:
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  # Update.
  Image = res.runImages[1]
  # Draw.

  screen.blit(res.runImages[int(i)],(0,0))
  i+=0.2
  if(i>7):
    i=0

  pygame.display.flip()
  fpsClock.tick(fps)