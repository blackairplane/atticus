import os
import random
import json
import pygame
pygame.init()

class Ai:
  def __init__(self, name = 'Atticus', width = 40):
    self.color = (0,255,0)
    self.width = width
    self.height = self.width / 2
    self.name = name
    self.speaking_speed = 250
    self.responses = {}
    self.load_responses()
    self.img = pygame.image.load('assets/blue-hal.png')

  def respond(self, response_type, debug = False):
    try:
      response = random.choice(self.responses[response_type])
    except:
        response = random.choice(self.responses['no_response'])
        self.respond('apology')
    self.say(response)

  def say(self, phrase):
    os.system("say \"" + str(phrase) + "\" -r " + str(self.speaking_speed))

  def load_responses(self):
    with open("data/responses.json", "r") as f: 
      self.responses = json.loads(f.readline())

  def identify(self):
    self.say("My name is " + self.name)

  def draw(self, surface):
    surface.blit(self.img, (450, 100))

  def input(self, content):
    receivedInput = TextInput(content)
    if receivedInput.needs_response():
      response = AI_response(receivedInput).output
      self.say(response)

class TextInput:
  def __init__(self, content =''):
    self.content = content
    
  def needs_response(self):
    return True

class AI_response:
  def __init__(self, input):
    self.input = input
    self.output = self.explain()

  def explain(self):
    response = ''
    #response = "Here's what I know so far: "
    response += "You have said " + str(self.input.content)
    # TODO: Decide if question is being asked
    if self.is_question():
      response += "This was a question."
    return response

  def is_question(self):
    questionPct = 0
    if self.input.content[-1:] == '?':
      questionPct = 100
    else:
      statement = self.input.content.split()
      firstWords = ['what', 'why', 'when', 'where', 'how', 'is', 'are', 'were','can', 'did', 'do', 'may', 'will', 'what\'s', 'where\'s', 'why\'s', 'how\'s']
      secondWords = ['are', 'much', 'aren\'t', 'will', 'can', 'is']
      for word in firstWords:
        if word == statement[0].lower():
          questionPct = 51
          break
    
    if questionPct > 50:
      return True
    else:
      return False
    
