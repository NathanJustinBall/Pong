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
        self.x_increment = 0
        self.y_increment = 0
        self.negative_y = 1
        self.negative_x = 1
        self.player_score = 0
        self.enemy_score = 0

        # sound
        pygame.mixer.init()
        root_sound = "./sound/"
        self.enemy_sound = pygame.mixer.Sound(root_sound+"blip enemy.wav")
        self.player_sound = pygame.mixer.Sound(root_sound + "blip player.wav")
        self.bounce_sound = pygame.mixer.Sound(root_sound + "bounce.wav")


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
            self.get_ball_cords()
            self.enemy_batten_ai()

            if check.for_reset():
                self.ball_y = self.screen_height / 2
                self.ball_x = self.screen_width / 2

    def blit_to_screen(self):
        self.screen.fill((0, 0, 0))
        # blit player batten
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.batten_x, self.batten_y, 20, 150))

        # blit enemy batten
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.enemy_batten_x, self.enemy_batten_y, 20, 150))

        # blit ball
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.ball_x, self.ball_y, 30, 30))

        # blit game score "player"
        label = self.game_font.render("Player score: "+str(self.player_score), 1, (255, 255, 255))
        self.screen.blit(label, (self.screen_width - 300, 100))

        # blit game score "enemy"
        label = self.game_font.render("Enemy score: " + str(self.enemy_score), 1, (255, 255, 255))
        self.screen.blit(label, (100, 100))

        # display flip
        pygame.display.flip()

    def get_ball_cords(self):
        # print(self.ball_x)
        new_angle = self.ball_check_bounce()

        self.ball_angle = new_angle

        if self.ball_x >= self.screen_width:
            self.ball_x = self.screen_width/2
            self.ball_y = self.screen_height/2
            self.ball_angle = random.randint(90, 270)
            self.enemy_score += 1

        elif self.ball_x <= 0:
            self.ball_x = self.screen_width/2
            self.ball_y = self.screen_height / 2
            self.ball_angle = random.randint(90, 270)
            self.player_score += 1

    def ball_check_bounce(self):
        new_angle = self.ball_angle
        # polar to cartesion conversion first
        self.x_increment = self.ball_speed * math.cos(self.ball_angle)
        self.y_increment = self.ball_speed * math.sin(self.ball_angle)

        self.ball_x += (self.x_increment*self.negative_x)
        self.ball_y += (self.y_increment*self.negative_y)

        if self.ball_y >= self.screen_height or self.ball_y < 0:
            self.negative_y = -self.negative_y
            self.bounce_sound.play()

        # player batten bounce
        if self.ball_x >= self.batten_x:
            if self.ball_y < self.batten_y + 150 and self.ball_y > self.batten_y:
                self.negative_x = -self.negative_x
                self.player_sound.play()

        # enemy batten bounce
        elif self.ball_x <= self.enemy_batten_x:
            if self.ball_y < self.enemy_batten_y + 150 and self.ball_y > self.enemy_batten_y:
                self.negative_x = -self.negative_x
                self.enemy_sound.play()

        return new_angle

    def enemy_batten_ai(self):
        if self.ball_y > self.enemy_batten_y:
            self.enemy_batten_y += self.batten_speed

        elif self.ball_y < self.enemy_batten_y:
            self.enemy_batten_y -= self.batten_speed




