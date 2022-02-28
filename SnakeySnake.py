from ctypes.wintypes import SIZE
import pygame

class Snake():
    snake = []
    SIZE = (10, 10)
    def __init__(self):
        rect = pygame.Rect(WIN, RED, SIZE)
        
        


pygame.init()
clock = pygame.time.Clock()
size = width, height = (1000, 1000)
WIN = pygame.display.set_mode(size, pygame.RESIZABLE)


FPS = 90

GREEN = (22, 100, 22)
RED = (170, 12, 12)


def main():
    run = True
    while run:
        WIN.fill(GREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False

        pygame.display.update()

if __name__ == "__main__":
    main()
