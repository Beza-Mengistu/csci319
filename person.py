from . import Mobile
from FSMs import WalkingFSM, AccelerationFSM, GravityFSM
from utils import vec, RESOLUTION

from pygame.locals import *

import pygame
import numpy as np

from gameObjects import Drawable, MobileGravity


#class Person(Mobile):
class Person(MobileGravity):
   def __init__(self, position):
      super().__init__(position, "person.png")

        
      # Animation variables specific to Person
      self.framesPerSecond = 2 
      self.nFrames = 2
      
      self.nFramesList = {
         "moving"   : 4,
         "standing" : 2
      }
      
      self.rowList = {
         "moving"   : 1,
         "standing" : 0
      }
      
      self.framesPerSecondList = {
         "moving"   : 8,
         "standing" : 2
      }
            
      self.FSManimated = WalkingFSM(self)
      self.LR = AccelerationFSM(self, axis=0)
      #self.UD = AccelerationFSM(self, axis=1)
      self.UD = GravityFSM(self)
      
   def handleEvent(self, event):
      if event.type == KEYDOWN:
         if event.key == K_UP:
            #self.UD.decrease()
            self.UD.jump
             
         elif event.key == K_DOWN:
            #self.UD.increase()
            pass
            
         elif event.key == K_LEFT:
            self.LR.decrease()
            
         elif event.key == K_RIGHT:
            self.LR.increase()
            
      elif event.type == KEYUP:
         if event.key == K_UP:
            # self.UD.stop_decrease()
            if self.UD.canFall:
               self.UD.fall
            else:
               pass
             
         elif event.key == K_DOWN:
            # self.UD.stop_increase()
            pass
            
         elif event.key == K_LEFT:
            self.LR.stop_decrease()
            
         elif event.key == K_RIGHT:
            self.LR.stop_increase()
   
   def update(self, seconds): 
      self.LR.update(seconds)
      self.UD.update(seconds)
      
      super().update(seconds)


   def draw(self, drawSurface):
      super().draw(drawSurface)
  
   
   def updateMovement(self):
      pass

   def getCollisionRect(self):
        # Customize the collision rectangle size for the person
        rect_width = self.getSize()[0] // 1
        rect_height = self.getSize()[1] // 1.1
        new_rect = pygame.Rect(self.position[0], self.position[1], rect_width, rect_height)
        return new_rect


   def handleCollision(self, platform): #function for colliding with platforms
        person_rect = self.getCollisionRect()
        platform_rect = pygame.Rect(platform.position[0], platform.position[1], platform.getSize()[0], platform.getSize()[1])

        
        if person_rect.colliderect(platform_rect):
            print("colliding")
            collisionArea = platform_rect.clip(person_rect) #(x,y,width,height)
            print("overlap:", collisionArea, collisionArea[2])
            if collisionArea[2] > collisionArea[3]: #if the width is greater than the height
               if platform.position[1] > self.position[1]:
                  print("from above, y-coordinate of platform and person:", platform.position[1], self.position[1])
                  if self.velocity[1] > 0:  # Stop vertical movement
                     self.UD.stop_increase()  # Stop upward movement
                     self.velocity[1] = 0
                     self.position[1] -= collisionArea[3]
               else:
                  print("from below, y-coordinate of platform and person:", platform.position[1], self.position[1])
                  if self.velocity[1] < 0:  # Stop vertical movement
                     self.UD.stop_decrease()  # Stop downward movement
                     self.velocity[1] = 0
                     self.position[1] += collisionArea[3]
            else:
               #Checking left and right collisions
               if platform.position[0] > self.position[0]:
                  print("from the left")
                  if self.velocity[0] > 0:  # Stop horizontal movement
                     self.LR.stop_increase()  # Stop rightward movement
                     self.velocity[0] = 0
                     self.position[0] -= collisionArea[2]
               elif platform.position[0] < self.position[0]:
                  if self.velocity[0] < 0:  # Stop horizontal movement
                     self.LR.stop_decrease()  # Stop leftward movement
                     self.position[0] += collisionArea[2]

            

            
      
  
      
   # def handleCollision(self, platform): #function for colliding with platforms
   #    person_rect = self.getCollisionRect()
   #    platform_rect = pygame.Rect(platform.position[0], platform.position[1], platform.getSize()[0], platform.getSize()[1])

   #    if person_rect.colliderect(platform_rect):
   #       # Check if the person is to the right of the platform
   #       if self.position[0] > platform.position[0] + platform.getSize()[0] // 2:
   #             if self.velocity[0] > 0:  # Stop horizontal movement
   #                self.LR.stop_increase()  # Stop rightward movement
   #                self.velocity[0] = 0
   #       # Check if the person is to the left of the platform
   #       elif self.position[0] < platform.position[0] + platform.getSize()[0] // 2:
   #             if self.velocity[0] < 0:  # Stop horizontal movement
   #                self.LR.stop_decrease()  # Stop leftward movement
   #                self.velocity[0] = 0

   #       # Check if the person is below the platform
   #       if self.position[1] > platform.position[1] + platform.getSize()[1] // 2:
   #             if self.velocity[1] > 0:  # Stop vertical movement
   #                self.UD.stop_increase()  # Stop upward movement
   #                self.velocity[1] = 0
   #       # Check if the person is above the platform
   #       elif self.position[1] < platform.position[1] + platform.getSize()[1] // 2:
   #             if self.velocity[1] < 0:  # Stop vertical movement
   #                self.UD.stop_decrease()  # Stop downward movement
   #                self.velocity[1] = 0
   
  