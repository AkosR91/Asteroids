import pygame  # pyright: ignore[reportMissingImports]
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
import player #type: ignore

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    gamer = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Create a player instance at the center of the screen
    clock = pygame.time.Clock()  # Initialize the clock
    dt = 0.0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill((0, 0, 0))  # Clear the screen with black
        log_state()
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return
        gamer.draw(screen)  # Draw the player on the screen
        pygame.display.flip()  # Update the full display surface to the screen
        dt = clock.tick(60) / 1000
        
        #print(f"Delta time (dt): {dt} seconds")

if __name__ == "__main__":
    main()
