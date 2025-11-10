from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame 
from constants import LINE_WIDTH, SHOT_RADIUS
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), SHOT_RADIUS, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt