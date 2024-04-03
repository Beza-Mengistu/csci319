from . import AbstractGameFSM
from utils import vec, magnitude, EPSILON, scale, RESOLUTION

from statemachine import State

class MovementFSM(AbstractGameFSM):
    
    def __init__(self, obj):
        super().__init__(obj)
    
    def update(self, seconds):
        super().update(seconds)

        # Add out of bounds checks here (for the ghost)
        # if self.obj.position[0] < 0:
        #     self.obj.velocity[0] = max(self.obj.velocity[0], 0)
        # elif self.obj.position[0] > RESOLUTION[0] - self.obj.getSize()[0]:
        #     self.obj.velocity[0] = min(self.obj.velocity[0], 0)
        # elif self.obj.position[1] < 0:
        #     self.obj.velocity[1] = max(self.obj.velocity[1], 0)
        # elif self.obj.position[1] > RESOLUTION[1] - self.obj.getSize()[1]:
        #     self.obj.velocity[1] = min(self.obj.velocity[1], 0)

        #makes sure the character wraps around the other side of the screen when out of bounds
        self.obj.position[0] = self.obj.position[0] % RESOLUTION[0] #left and right
        self.obj.position[1] = self.obj.position[1] % RESOLUTION[1] #up and down


class AccelerationFSM(MovementFSM):
    """Axis-based acceleration with gradual stopping."""
    not_moving = State(initial=True)
    
    negative = State()
    positive = State()
    
    stalemate = State()
    
    decrease  = not_moving.to(negative) | positive.to(stalemate) | negative.to.itself(internal = True) | stalemate.to.itself(internal = True)
    
    increase = not_moving.to(positive) | negative.to(stalemate) | positive.to.itself(internal = True) | stalemate.to.itself(internal = True)
    
    stop_decrease = negative.to(not_moving) | stalemate.to(positive) | not_moving.to.itself(internal = True) | positive.to(not_moving)
    
    stop_increase = positive.to(not_moving) | stalemate.to(negative) | not_moving.to.itself(internal = True) | negative.to(not_moving)
    
    stop_all      = not_moving.to.itself(internal=True) | negative.to(not_moving) | \
                    positive.to(not_moving) | stalemate.to(not_moving)
    
    def __init__(self, obj, axis=0):
        self.axis      = axis
        self.direction = vec(0,0)
        self.direction[self.axis] = 1
        self.accel = 200
        
        super().__init__(obj)

    def update(self, seconds=0):
        if self == "positive":
            self.obj.velocity += self.direction * self.accel * seconds
        elif self == "negative":
            self.obj.velocity -= self.direction * self.accel * seconds
                
        elif self == "stalemate":
            pass
        else:
            if self.obj.velocity[self.axis] > self.accel * seconds:
                self.obj.velocity[self.axis] -= self.accel * seconds
            elif self.obj.velocity[self.axis] < -self.accel * seconds:
                self.obj.velocity[self.axis] += self.accel * seconds
            else:
                self.obj.velocity[self.axis] = 0
            
        
    
        super().update(seconds)

    def isIncreasing(self):
        return self == "positive"

    def isDecreasing(self):
        return self == "negative"