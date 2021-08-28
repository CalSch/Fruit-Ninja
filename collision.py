import math

def dist(x1,y1,x2,y2):
  return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def CheckPointCircle(pos1: tuple, r: float, pos2: tuple):
  return dist(pos1[0], pos1[1], pos2[0], pos2[1]) < r