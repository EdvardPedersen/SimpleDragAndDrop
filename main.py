import pygame

class EventHandler:
  def __init__(self):
    self.handlers = {}

  def subscribe(self, event_type, method):
    if event_type not in self.handlers:
      self.handlers[event_type] = []
    self.handlers[event_type].append(method)

  def unsubscribe(self, event_type, method):
    if event_type not in self.handlers:
      return
    self.handlers[event_type].remove(method)

  def check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return False
      if not event.type in self.handlers:
        continue
      for handler in self.handlers[event.type]:
        handler(event)
    return True

class Movable:
  def __init__(self, rect, eventhandler):
    self.rect = rect
    self.dragging = False
    self.event_handler = eventhandler
    self.event_handler.subscribe(pygame.MOUSEBUTTONDOWN, self.on_mouse_down)

  def on_mouse_down(self, event):
    if self.rect.collidepoint(event.pos):
      self.dragging = True
      self.event_handler.subscribe(pygame.MOUSEMOTION, self.mousemove)
      self.event_handler.subscribe(pygame.MOUSEBUTTONUP, self.on_mouse_up)
      self.event_handler.unsubscribe(pygame.MOUSEBUTTONDOWN, self.on_mouse_down)

  def mousemove(self, event):
    if not self.dragging:
      return
    self.rect.x += event.rel[0]
    self.rect.y += event.rel[1]

  def on_mouse_up(self, event):
    self.dragging = False
    self.event_handler.subscribe(pygame.MOUSEBUTTONDOWN, self.on_mouse_down)
    self.event_handler.unsubscribe(pygame.MOUSEMOTION, self.mousemove)
    self.event_handler.unsubscribe(pygame.MOUSEBUTTONUP, self.on_mouse_up)

  def draw(self, surface):
    color = (255, 0, 0)
    if self.dragging:
      color = (0, 255, 255)
    surface.fill(color, self.rect)

class Game:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((800,800))
    self.ev = EventHandler()
    self.movables = []
    for x in range(100, 600, 100):
      self.movables.append(Movable(pygame.Rect(x, 100, 50, 50), self.ev))

  def mainloop(self):
    if not self.ev.check_events():
      return False
    self.screen.fill((0,0,0))
    for m in self.movables:
      m.draw(self.screen)
    pygame.display.update()
    return True

if __name__ == "__main__":
  g = Game()
  while g.mainloop():
    pass
