import pygame, sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)


    P1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    A_F_1 = AsteroidField()


    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

        updatable.update(dt)
        for a in asteroids:
           if P1.collides_with(a) == True:
            log_event("player_hit")
            print("Game over!")
            sys.exit()

        for a in asteroids:
            for s in shots:
                if s.collides_with(a) == True:
                    log_event("asteroid_shot")
                    a.split()
                    s.kill()

        log_state()
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        

    

    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
