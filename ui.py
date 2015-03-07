import pygame
pygame.init()
btnFont = pygame.font.SysFont("Gotham", 15, True)
inputFont = pygame.font.SysFont("Gotham", 15)

class Button:
  def __init__(self, x, y, color = (0,0,0), text = 'None', width = 100, height = 40):
    self.x = x
    self.y = y
    if (10 * len(text) > width):
      self.width = len(text) * 10 + 10
    else:
      self.width = width
    self.height = height
    self.color = color
    self.text = text
  
  def contains(self, (x, y)):
    if x > self.x and x < (self.x + self.width) and y > self.y and y < (self.y + self.height):
      return True
    else:
      return False

  def label(self, surface, text):
    label = btnFont.render(text, 1, (255,255,255))
    surface.blit(label, ((self.x + 10), (self.y + 10)))

class InputBox:
  def __init__(self, x, y, width = 100, height = 40, content = ''):
    self.x = x
    self.y = y
    self.content = content
    self.width = width
    self.height = height
    self.bg_color = (245,245,245)
    self.show_cursor = True
    self.cursor_blink_speed = 10

  def update(self, surface):
    value = inputFont.render(self.content, 1, (0,0,0))
    surface.blit(value, ((self.x + 10), (self.y + 10)))

  def addText(self, text):
    self.content += str(text)

  def contains(self, (x, y)):
    if x > self.x and x < (self.x + self.width) and y > self.y and y < (self.y + self.height):
      return True
    else:
      return False

  def backspace(self):
    self.content = self.content[:-1]
