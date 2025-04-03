import pygame

class Movable:
  def __init__(self, rect):
    self.rect = rect

class Circle(Movable):
  def draw(self, surface):
    color = (255, 0, 0)
    pygame.draw.circle(surface, color, self.rect.center, self.rect.w / 2)

class Box(Movable):
  def draw(self, surface):
    color = (0, 255, 0)
    pygame.draw.rect(surface, color, self.rect)

class Triangle(Movable):
  def draw(self, surface):
    color = (0, 0, 255)
    pygame.draw.polygon(surface, color, [self.rect.midtop, self.rect.bottomright, self.rect.bottomleft])

class Game:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((800,800))
    self.movables = []
    for x in range(100, 600, 100):
      self.movables.append(Circle(pygame.Rect(x, 100, 50, 50)))
      self.movables.append(Box(pygame.Rect(x, 300, 50, 50)))
      self.movables.append(Triangle(pygame.Rect(x, 500, 50, 50)))

  def mainloop(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit()
    self.screen.fill((0,0,0))
    for m in self.movables:
      m.draw(self.screen)
    pygame.display.update()
    return True

if __name__ == "__main__":
  g = Game()
  while g.mainloop():
    pass
