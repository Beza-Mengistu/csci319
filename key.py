import pygame
from gameObjects import Drawable

class Key(Drawable):
    def __init__(self, position):
        super().__init__(position, "key.png")
        
        
    def update(self, seconds):
        pass

    def draw(self, draw_surface):
        super().draw(draw_surface)