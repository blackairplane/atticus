import pygame
import time
import random

from ai import *
from ui import *
from colors import *

pygame.init()
display_width = 1200
display_height = 500
window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('AI test')
clock = pygame.time.Clock()

ai = Ai()

def draw_ui():
  for b in buttons:
    pygame.draw.rect(window, b.color, (b.x,b.y,b.width,b.height))
    b.label(window, b.text)
  
  for i in inputFields:
    pygame.draw.rect(window, i.bg_color, (i.x, i.y, i.width, i.height))
    i.update(window)

buttons = [Button(10,10,green, 'affirmation'), Button(10,60,blue, 'agreement'), Button(10,110,red,'apology'), Button(10,160,yellow,'negation'), Button(10,210,green,'identify')]
#buttons = []
inputFields = [InputBox(10,(display_height-50), (display_width-20))]
def app_loop():
  editingInput = False
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        m = pygame.mouse.get_pos()
        for button in buttons:
          if button.contains(m):
            if button.text == 'identify':
              ai.identify()
            else:
              ai.respond(button.text)
        for i in inputFields:
          if i.contains(m):
            editingInput = True
          else:
            if editingInput == True:
              editingInput = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
          inputFields[0].backspace()
        elif event.key > 31 and event.key < 127:
          inputFields[0].addText(event.unicode)
        elif event.key == pygame.K_RETURN:
          textInput = inputFields[0].content
          inputFields[0].content = ''
          ai.input(textInput)
         

    window.fill(black)
    draw_ui()
    ai.draw(window)
    pygame.display.update()
    clock.tick(50)

app_loop()
