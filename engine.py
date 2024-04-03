import pygame

from . import Drawable, Person
from gameObjects import Ghost

from utils import vec, RESOLUTION

class GameEngine(object):

    def __init__(self):       
        self.person = Person((100,100))
        self.ghost = Ghost((50,50), self) #self passes the game object to the ghost in order to access Person's position
        self.size = vec(*RESOLUTION)
        self.background = Drawable((0,0), "backg2.png")
    
    def draw(self, drawSurface):        
        self.background.draw(drawSurface)
        
        self.person.draw(drawSurface)
        self.ghost.draw(drawSurface)
            
    def handleEvent(self, event):
        self.person.handleEvent(event)
        #self.ghost.handleEvent(event)
    
    def update(self, seconds):
        self.person.update(seconds)
        self.ghost.update(seconds)
        
        Drawable.updateOffset(self.person, self.size)
        Drawable.updateOffset(self.ghost, self.size)

    def getPersonPosition(self): #returns the person's position so the ghost can follow
        return self.person.position
    

