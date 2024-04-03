from gameObjects import Person, Drawable, Ghost, Key
from utils import vec, RESOLUTION, WORLD_SIZE
import pygame

class PlatformerGameEngine(object):
    def __init__(self):
        # Initialize game objects (Person character, platforms, etc.)
        self.person = Person(vec(16, WORLD_SIZE[1] - 75))
        self.ghost = Ghost((50,50), self)
        self.key = Drawable(vec(220, WORLD_SIZE[1] - 120), "keya.png")
        self.key2 = Key(vec(220, WORLD_SIZE[1] - 200))
        self.platforms = []  # List to store platform tiles
        self.loadPlatforms()  # Load platform tiles
        brickSize = vec(40,30)

    def loadPlatforms(self):
        # Define positions for platform tiles (example positions)
        platform_positions = [
            vec(0, WORLD_SIZE[1] - 32),
            vec(100, WORLD_SIZE[1] - 32),
            vec(200, WORLD_SIZE[1] - 32),
            vec(300, WORLD_SIZE[1] - 32),
            vec(200, WORLD_SIZE[1] - 100)
            # Add more positions as needed
        ]

        self.background = Drawable((0,0), "backg2.png")
        # Create Drawable objects for platform tiles and add them to the list
        for pos in platform_positions:
            platform = Drawable(pos, "dungeonBrick.png")  # Assuming "dungeonBrick.png" is the image of bricks
            platform.image = pygame.transform.scale(platform.image, vec(100,20) )
            self.platforms.append(platform)
        self.key.image = pygame.transform.scale(self.key.image, vec(20,20) )

    def draw(self, drawSurface):
        # Draw everything including platform tiles
        
        self.background.draw(drawSurface)
        for platform in self.platforms:
            platform.draw(drawSurface)
            pygame.draw.rect(drawSurface, (255, 0, 0), platform.getCollisionRect(), 2)  # Draw collision rect
        self.person.draw(drawSurface)
        pygame.draw.rect(drawSurface, (255, 0, 0), self.person.getCollisionRect(), 2)  # Draw person's collision rect
        self.ghost.draw(drawSurface)
        self.key.draw(drawSurface)

    def handleEvent(self, event):
        self.person.handleEvent(event)

    def update(self, seconds):
        self.person.update(seconds)
        self.ghost.update(seconds)
        Drawable.updateOffset(self.person, WORLD_SIZE)
        Drawable.updateOffset(self.ghost, WORLD_SIZE)
        self.checkCollision()

    def getPersonPosition(self): #returns the person's position so the ghost can follow
        return self.person.position
    
    def getPlCollisionRect(self, platform):
        return pygame.Rect(platform.position[0], platform.position[1], platform.getSize()[0], platform.getSize()[1])
    
    def checkCollision(self):
        person_rect = self.person.getCollisionRect()  # Get collision rectangle for the player
        for platform in self.platforms:
            platform_rect = self.getPlCollisionRect(platform)  # Get collision rectangle for each platform
            if person_rect.colliderect(platform_rect):  # Check for collision
                # Handle collision based on your game logic (e.g., stop player movement)
                self.person.handleCollision(platform)
            
    # def handleCollision(self, platform): #function for colliding with platforms
    #    # Stop vertical movement
    #     if self.person.velocity[1] > 0:
    #         self.person.UD.stop_increase()
    #     elif self.person.velocity[1] < 0:
    #         self.person.UD.stop_decrease()
                
    # def handleCollision(self, platform):
    #     person_rect = self.person.getCollisionRect()  # Get collision rectangle for the player
    #     platform_rect = self.getPlCollisionRect(platform)  # Get collision rectangle for the platform

    #     # Check if the platform is above or below the person
    #     if platform.position.y < self.person.position.y:
    #         # If the platform is above, adjust the person's position to be above the platform
    #         self.person.position.y = platform.position.y - person_rect.height
    #         self.person.velocity.y = 0  # Stop vertical movement
    #         self.person.UD.stop_increase()  # Stop upward movement
    #     else:
    #         # If the platform is below, adjust the person's position to be below the platform
    #         self.person.position.y = platform.position.y + platform_rect.height
    #         self.person.velocity.y = 0  # Stop vertical movement
    #         self.person.UD.stop_decrease()  # Stop downward movement

    