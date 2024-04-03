from . import Mobile
from FSMs.gravity import GravityFSM
from FSMs.movement import AccelerationFSM
from utils.vector import vec


class MobileGravity(Mobile):
    def __init__(self, position, fileName=""):
        super().__init__(position, fileName)
        self.UD = GravityFSM(self)
        self.LR = AccelerationFSM(self)
        
    def update(self, seconds):        
        self.UD.updateState()
        self.LR.updateState()   
 
        # Handle Collision with each item in colliders

        # for collideRect in collideRects:
        #     if self.doesCollide(collideRect):
        #         self.handleCollision(collideRect)

        # Update position based on velocity after handling collision
        self.position += self.velocity * seconds

    # def handleCollision(self, collideRect):
    #     dx = collideRect.centerx - self.position[0]
    #     dy = collideRect.centery - self.position[1]

    #     if abs(dx) > abs(dy):
    #         if dx > 0:
    #             self.position[0] = collideRect.right
    #         else:
    #             self.position[0] = collideRect.left
    #         self.velocity[0] = 0  # Stop horizontal movement
    #     else:
    #         if dy > 0:
    #             self.position[1] = collideRect.bottom
    #             self.velocity[1] = 0  # Stop vertical movement
    #         else:
    #             self.position[1] = collideRect.top
    #             self.velocity[1] = 0  # Stop vertical movement
