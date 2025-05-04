import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

print("Hello I anm coding right now is it registering)")

if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
    print("Game Over")
    