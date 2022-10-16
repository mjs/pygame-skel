import sys, pygame

GRAVITY_TIMER = pygame.USEREVENT
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY_TIMER_MS = 5

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.key.set_repeat(5)
pygame.time.set_timer(GRAVITY_TIMER, GRAVITY_TIMER_MS)


class Block(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.color = (0, 0, 255)
        self.width = 50
        self.height = 50
        self.x = 100
        self.y = 100.0

        self.y_accel = 0.0
        self.max_y = SCREEN_HEIGHT - self.height

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, int(self.y), self.width, self.height], 5)

    def left(self):
        self.x = max(self.x - 1, 0)

    def right(self):
        self.x = min(self.x + 1, SCREEN_WIDTH - self.width)

    def jump(self):
        self.y_accel -= 0.1
        self.y -= 1

    def gravity_update(self):
        if self.y < self.max_y:
            self.y_accel += 0.03
            self.y += self.y_accel
        else:
            self.y = self.max_y
            self.y_accel = 0


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

            if event.key == pygame.K_UP:
                block.jump()

        if event.type == GRAVITY_TIMER:
            block.gravity_update()

