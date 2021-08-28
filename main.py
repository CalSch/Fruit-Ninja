import pygame
from collision import dist, CheckPointCircle
from Fruit import Fruit

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])
clock=pygame.time.Clock()

# Variables

mx: int=0
my: int=0

melon=Fruit(100,1,-3.75)

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
  melon.update()

  # Clear the screen
  screen.fill((255, 255, 255))

  # Draw the stuff
  melon.draw(screen)

  # Flip the display

  pygame.display.flip()

pygame.quit()