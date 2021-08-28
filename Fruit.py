import pygame

gravity: float=0.02
friction: float=1.0005

class Fruit():
  def __init__(self, x: float, vx: float, vy: float):
    self.x: float=x
    self.y: float=500
    self.vx, self.vy=(vx,vy)
    self.size=20
  def update(self):
    self.vy+=gravity

    self.vx/=friction
    self.vy/=friction

    self.x+=self.vx
    self.y+=self.vy
  def draw(self,screen: pygame.Surface):
    pygame.draw.circle(screen, (0, 255, 50), (self.x,self.y), self.size)