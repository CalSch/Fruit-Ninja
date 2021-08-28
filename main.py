import pygame
from collision import dist, CheckPointCircle
from Fruit import Fruit
from random import uniform

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])
clock=pygame.time.Clock()

# Variables
fruitCullingLevel=500
mx: int=0
my: int=0

fruits=[]
melon=Fruit(100,1,-3.75)
fruits.append(melon)

# Game
running = True

while running:
  clock.tick(90)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  pressed_keys = pygame.key.get_pressed()
  mx, my=pygame.mouse.get_pos()

  # Update the game  
  if uniform(0, 1)<=1/(90*5):
    fruits.append(Fruit(100,1,-3.75))

  for fruit in fruits:
    fruit.update()
    # Delete fruit if its too low
    if fruit.y > fruitCullingLevel:
      fruits.remove(fruit)

  # Clear the screen
  screen.fill((255, 255, 255))

  # Draw the stuff
  for fruit in fruits:
    fruit.draw(screen)

  # Flip the display

  pygame.display.flip()

pygame.quit()