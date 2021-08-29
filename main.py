import pygame
from collision import dist, CheckPointCircle
from Fruit import Fruit
from random import uniform, randint

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])
clock=pygame.time.Clock()

# Variables
rate=5  # Seconds between fruit toss (approximately)
fruitCullingLimit=500  # y-limit for fruit (they get deleted if there lower than it)
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
  if uniform(0, 1)<=1/(90*rate):
    fruits.append(Fruit(100, 1, -3.75))
  for fruit in fruits:
    fruit.update()
    if fruit.y>fruitCullingLimit:
      fruits.remove(fruit)

  # Clear the screen
  screen.fill((255, 255, 255))

  # Draw the stuff
  for fruit in fruits:
    fruit.draw(screen)

  # Flip the display

  pygame.display.flip()

pygame.quit()