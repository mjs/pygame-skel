import sys, pygame

GRAVITY_TIMER = pygame.USEREVENT
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.key.set_repeat(5)
pygame.time.set_timer(GRAVITY_TIMER, 3)


class Block(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.x = 100
        self.y = 100
        self.width = 50
        self.height = 50
        self.color = (0, 0, 255)

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height], 5)

    def left(self):
        self.x = max(self.x - 1, 0)

    def right(self):
        self.x = min(self.x + 1, SCREEN_WIDTH - self.width)

    def gravity_update(self):
        self.y += 1
        self.y = min(self.y, SCREEN_HEIGHT - self.height)


block = Block()

while True:
    screen.fill([255,255,255])
    block.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                block.left()

            if event.key == pygame.K_RIGHT:
                block.right()

        if event.type == GRAVITY_TIMER:
            block.gravity_update()

