import pygame as pg
import sys
from aim import Aim
from duck import Duck
from hit import Hit
from assets import *
from settings import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.duck = Duck(self)
        self.aim = Aim(self)
        self.hit = Hit(self)

    def update(self):
        self.hit.update(self.duck.x, self.duck.y, self.aim.x, self.aim.y)
        self.aim.update()
        self.duck.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.blit(background, (0, 0))
        self.duck.draw(self.hit.hit_duck)
        self.hit.draw(self.duck.x, self.duck.y, self.aim.x, self.aim.y)
        self.aim.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
