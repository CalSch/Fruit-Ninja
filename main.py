import pygame

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])

# Variables
x: float=250
y: float=250
vx: float=0
vy: float=-1

gravity: float=0.002
friction: float=1.005

# Game
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  pressed_keys = pygame.key.get_pressed()

  # Update the game
  if pressed_keys[pygame.K_SPACE]:
    vy=-1


  vy+=gravity

  vx/=friction
  vy/=friction

  x+=vx
  y+=vy

  # Clear the screen
  screen.fill((255, 255, 255))

  # Draw the stuff
  pygame.draw.circle(screen, (0, 0, 255), (x, y), 10)


  # Flip the display

  pygame.display.flip()

pygame.quit()