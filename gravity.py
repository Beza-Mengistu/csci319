from .abstract import AbstractGameFSM
from . import AnimateFSM
from statemachine import State


class GravityFSM(AbstractGameFSM):
    # def __init__(self, obj):
    #     super().__init__(obj) 
    #     self.jumpTimer = 0
    #     self.gravity = 200
    #     self.jumpSpeed = 100
    #     self.jumpTime = 0.2

    grounded = State(initial=True)
    jumping = State()
    falling = State()

    jump = grounded.to(jumping) | falling.to.itself(internal=True)
    fall = jumping.to(falling) | grounded.to(falling)
    land = falling.to(grounded) | jumping.to(grounded)


    def __init__(self, obj):
        super().__init__(obj) 
        self.jumpTimer = 0
        self.gravity = 200
        self.jumpSpeed = 100
        self.jumpTime = 0.2

        # # Define states
        # self.grounded = State(initial=True)
        # self.jumping = State()
        # self.falling = State()

        # # Define transitions
        # self.jump = self.grounded.to(self.jumping) | self.falling.to.itself(internal=True)
        # self.fall = self.jumping.to(self.falling) | self.grounded.to(self.falling)
        # self.land = self.falling.to(self.grounded) | self.jumping.to(self.grounded)



    def updateState(self):
        if self.canFall() and self == "jumping":
            self.fall()

    def canFall(self):
        return self.jumpTimer < 0
    
    def on_enter_jumping(self):
        self.jumpTimer = self.jumpTime

    def update(self, seconds=0):
        if self == "falling":
            self.obj.velocity[1] += self.gravity * seconds
        elif self == "jumping":
            self.obj.velocity[1] = -self.jumpSpeed
            self.jumpTimer -= seconds
        else:
            self.obj.velocity[1] = 0

        super().update(seconds)






