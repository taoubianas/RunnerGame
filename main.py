import sys
 
import pygame
from pygame.locals import *
from Background import Background

from Charachter import Charachter
from Objects import Objects
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
i=0
screen = pygame.display.set_mode((width, height))
Char= Charachter(screen,(0,height*2/3))
Back= Background(screen,(0,height*2/3),0.5)
obj= Objects(screen,(width,height*2/3),0.5)
# Game loop.
while True:
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == KEYDOWN and event.key == pygame.key.key_code("space"):
      Char.jump()
  
  # Update.
  # Draw.

  """for hbox in obj.hitBox:
    if( Char.deadHit(hbox)):
      print("dead" + str(i))
      i+=1"""
  
  Back.animate()
  Char.animate()
  obj.animate()
  obj.deadHit(Char)
  
  """a=Char.deadHit(obj.hitBox)
      print(a)"""

  pygame.display.flip()
  fpsClock.tick(fps)