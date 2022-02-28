import pygame, random

SNAKEHEAD = pygame.image.load("SnakeBody.png")
SNAKEBODY = pygame.image.load("SnakeHead.png")

# snake.dir: 0,1 - Horizontal (L/R), 2,3 - Vertical (Down,Up)
class Food():
    def __init__(self):
        x = random.randint(0,width-10)
        y = random.randint(0,height-10)
        self.x = round(x/10)* 10
        self.y = round(y/10)* 10
        self.SIZE = (15, 15)
    
    def draw(self):
        pygame.draw.rect(WIN, RED, ((self.x, self.y), self.SIZE))
    


class Snake():
    def __init__(self):
        self.__SIZE = (15,15)
        self.dir = 1
        self.collectingFood = False
        starting_head = (width/2, height/2)
        self.snakeCoords = []
        for i in range(0, 4): self.snakeCoords.append( (starting_head[0], starting_head[1]+(i* self.__SIZE[1])-1) )
    
    def grabFood(self, food):
        
        #if self.snake[0].colliderect(food):
            #self.collectingFood = True
            #return True
        return False    

    def move(self):
        
        if self.dir == 2:
            self.snakeCoords.insert(0, (self.snakeCoords[0][0], self.snakeCoords[0][1]+ self.__SIZE[1]))
        elif self.dir == 3:
            self.snakeCoords.insert(0, (self.snakeCoords[0][0], self.snakeCoords[0][1]-self.__SIZE[1]))
        elif self.dir == 1:
            self.snakeCoords.insert(0, (self.snakeCoords[0][0]+ self.__SIZE[0], self.snakeCoords[0][1]))
        elif self.dir == 0:
            self.snakeCoords.insert(0, (self.snakeCoords[0][0]-self.__SIZE[0], self.snakeCoords[0][1]))
        
        if self.collectingFood:
            self.collectingFood = False
        else:
            self.snakeCoords.pop()
        


    def draw(self):
        self.snake = []
        for scale in (self.snakeCoords):
            rect = pygame.draw.rect(WIN, RED, (scale, self.__SIZE))
            self.snake.append(pygame.mask.from_surface(rect))
            
    

pygame.init()
clock = pygame.time.Clock()



RED = (217, 37, 37)
BLACK = (0,0,0)
GREEN = (32, 115, 54)


size = width, height = 1000, 1000
WIN = pygame.display.set_mode(size, pygame.RESIZABLE)

FPS = 30



def main():
    run = True
    s = Snake()
    foodArr = []
    for i in range(0, 15): foodArr.append(Food())
    while run:
        WIN.fill(GREEN)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and (s.dir == 0 or s.dir == 1):
                    s.dir = 3
                elif event.key == pygame.K_s and (s.dir == 0 or s.dir == 1):
                    s.dir = 2
                elif event.key == pygame.K_a and (s.dir == 3 or s.dir == 2):
                    s.dir = 0
                elif event.key == pygame.K_d and (s.dir == 3 or s.dir == 2):
                    s.dir = 1
        s.move()    
        s.draw()   
        for food in foodArr:
            food.draw()
            if s.grabFood(food):
                print("Grab")
                foodArr.remove(food)
        
        pygame.display.update()

if __name__ == '__main__':
    main()