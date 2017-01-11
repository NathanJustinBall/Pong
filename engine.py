import pygame
import check
import random
import math


class Main:
    def __init__(self, screen):
        screen_info = pygame.display.Info()
        self.screen_height = screen_info.current_h
        self.screen_width = screen_info.current_w
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.batten_y = screen_info.current_h/2
        self.batten_x = screen_info.current_w - 50
        self.ball_y = self.screen_height/2
        self.ball_x = self.screen_width/2
        self.enemy_batten_y = screen_info.current_h/2
        self.enemy_batten_x = 50
        self.batten_speed = 3
        # init ball angle like this
        self.ball_angle = random.randint(0, 359)
        self.ball_speed = 4
        self.game_font = pygame.font.SysFont("calibri", 40)

    def control(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if self.batten_y > 0:
                self.batten_y -= self.batten_speed
        if pressed[pygame.K_DOWN]:
            if self.batten_y < self.screen_height-150:
                self.batten_y += self.batten_speed

    def tick(self):
        while True:
            self.control()
            self.blit_to_screen()
            self.clock.tick()
            check.for_quit()

            if check.for_reset():
                self.ball_y = self.screen_height / 2
                self.ball_x = self.screen_width / 2

    def blit_to_screen(self):
        self.screen.fill((0, 0, 0))
        # blit player batten
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.batten_x, self.batten_y, 20, 150))

        # blit enemy batten

        # blit ball
        pygame.draw.circle(self.screen, (255, 255, 255), (self.get_ball_cords()), 20)

        # blit game info
        label = self.game_font.render("Ball angle = "+str(self.ball_angle), 1, (255, 0, 0))
        self.screen.blit(label, (self.screen_width- 300, 100))

        # display flip
        pygame.display.flip()

    def get_ball_cords(self):
        # polar to cartesion conversion first
        x_increment = self.ball_speed * math.cos(self.ball_angle)
        y_increment = self.ball_speed * math.sin(self.ball_angle)

        self.ball_x += x_increment
        self.ball_y += y_increment

        # print(self.ball_x)
        new_angle = self.ball_check_bounce()

        self.ball_angle = new_angle

        if self.ball_x >= self.screen_width:
            self.ball_x = self.screen_width/2
            self.ball_y = self.screen_height/2
            self.ball_angle = random.randint(0, 359)
        elif self.ball_x <= 0:
            self.ball_x = self.screen_width/2
            self.ball_y = self.screen_height / 2
            self.ball_angle = random.randint(0, 359)

        return int(self.ball_x), int(self.ball_y)

    def ball_check_bounce(self):
        new_angle = self.ball_angle
        if self.ball_y >= 1060 or self.ball_y < 20:
            new_angle = int(math.degrees(math.atan(self.ball_y/self.ball_x))+90)

        #if self.ball_x >= self.screen_width-60:
         #   if self.ball_y <= self.batten_y+75 and self.ball_y >=self.ball_y-75 :
                # new_angle =


        return new_angle




