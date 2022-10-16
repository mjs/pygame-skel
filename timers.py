import sys, pygame

GRAVITY_TIMER = pygame.USEREVENT

pygame.init()


screen = pygame.display.set_mode([640,480])
pygame.key.set_repeat(5)
pygame.time.set_timer(GRAVITY_TIMER, 5)

x = 100
y = 100

while True:
    screen.fill([255,255,255])
    pygame.draw.rect(screen, (0, 0, 255), [x, y, 50, 50], 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x += 1

            if event.key == pygame.K_RIGHT:
                x += 1

        if event.type == GRAVITY_TIMER:
            y += 1
            if y > 480 - 50:
                y = 480 - 50

    pygame.display.flip()
