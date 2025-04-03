import pygame


class Movable:
  def __init__(self, rect):
    self.rect = rect

  def draw(self, surface):
    color = (255, 0, 0)
    surface.fill(color, self.rect)

class Game:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((800,800))
    self.movables = []
    for x in range(100, 600, 100):
      self.movables.append(Movable(pygame.Rect(x, 100, 50, 50)))

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
