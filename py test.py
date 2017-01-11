import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
is_blue = True
x = 0
y = 0

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue

        #Get Key
        pressed = pygame.key.get_pressed()

        #CONTROLS:
        #if pressed[pygame.K_UP]: 
        #if pressed[pygame.K_DOWN]:
        if pressed[pygame.K_LEFT]: x -= 2
        if pressed[pygame.K_RIGHT]: x += 2


        #GRAVITY
        if 600-y > 60:
            y += 5
            print(y)
        
        
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

        #GAME TICK AND DISPLAY
        pygame.display.flip()
        clock.tick(60)
