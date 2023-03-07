from settings import *
import pygame as pg
import random
from assets import *


class Duck:
    def __init__(self, game):
        self.game = game
        self.x, self.y = DUCK_POS
        self.clock = pg.time.Clock()
        self.time_elapsed_since_last_action = 0
        self.screen = game.screen

    def movement(self):
        dt = self.clock.tick()
        self.time_elapsed_since_last_action += dt

        # TODO Increase the action time in a linear way to get harder to hit the duck.
        ## Should the movement be linear along the screen?
        if self.time_elapsed_since_last_action > 5000:
            self.x = random.uniform(0, WIDTH - DUCK_RADIUS)
            self.y = random.uniform(0, HEIGHT - DUCK_RADIUS)
            self.time_elapsed_since_last_action = 0

    def draw(self):
        # pg.draw.circle(self.game.screen, 'green', (
        #     (self.x + DUCK_RADIUS), (self.y + DUCK_RADIUS)), DUCK_RADIUS)
        self.screen.blit(fly_duck, (self.x, self.y))

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
