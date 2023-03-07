from settings import *
import pygame as pg
from assets import *


class Aim:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.aim_radius = AIM_RADIUS
        self.x, self.y = AIM_POS

    def movement(self):
        speed = AIM_SPEED * self.game.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            if self.y > AIM_RADIUS:
                self.y -= speed
        if keys[pg.K_DOWN]:
            if self.y < HEIGHT - AIM_RADIUS:
                self.y += speed
        if keys[pg.K_RIGHT]:
            if self.x < WIDTH - AIM_RADIUS:
                self.x += speed
        if keys[pg.K_LEFT]:
            if self.x > AIM_RADIUS:
                self.x -= speed

    def draw(self):
        # TODO add or draw a better scope with border limits.
        pg.draw.circle(self.game.screen, 'red', (self.x, self.y), self.aim_radius)
        #self.screen.blit(scope, (self.x, self.y))

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
