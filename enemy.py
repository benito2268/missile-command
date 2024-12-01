import pygame as pg
import missile
import defs
import math
import random as rand

# TODO change this, maybe move to another class even
CITIES = [(200, defs.V_FULL), (400, defs.V_FULL), (800, defs.V_FULL)]

# this class copies A LOT of the normal missile code
# after all, an ememy is just a missle going the other direction
# targeting the cities
class Enemy(missile.Missile):
    def __init__(self):
        pos = CITIES[rand.randint(0, 2)]
        super().__init__(pos)

        self.source = (rand.randint(0, defs.H_FULL), 0)
        self.rect = pg.Rect(*self.source, 6, 6)

        # enemies have much slower speed
        self.speed = 1

        self.trail_size = 3
        self.trail_fade_speed = 1
        self.trail_color = defs.GREY
        self.trail_draw_speed = 5

    # called when a player missile collides with this missile
    def destroy(self):
        pass