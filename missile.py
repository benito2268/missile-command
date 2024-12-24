import defs
import pygame as pg
import math
import explosion

BASE_STATIONS = [(115, 910), (700, 905), (1270, 905)]

class Missile(pg.sprite.Sprite):
 
    def __init__(self, pos, is_enemy=False):
        # Set the initial position (source) and the initial target.
        self.source = BASE_STATIONS[int((pos[0] // (defs.H_FULL / 3)))]
        self.rect = pg.Rect(*self.source, 12, 12)
        self.target = pos 

        self.is_enemy = False
        self.done = False
        self.reached_target = False

        self.trail = []

        # clear one square of the trail every __ frames
        # higher = slower fade
        self.trail_fade_speed = 3
        self.trail_fade_cnt = 0
        self.trail_size = 6
        self.trail_color = defs.WHITE
        self.trail_draw_speed = 0
        self.trail_draw_cnt = 0

        # Set the missile's speed (arbitrary scale factor)
        # higher = faster
        self.speed = 10

        self.explosion = None
        self.target_marker = pg.image.load("sprites/target.png")

    def explode(self, pos):
        self.reached_target = True
        self.explosion = explosion.Explosion(pos)
        
    def update(self, screen, enemies):
        if self.reached_target:
            if len(self.trail) == 0:
                self.done = True
            self.explosion.update(screen, enemies)
            return
        
        # color the previous position grey
        if self.trail_draw_cnt == self.trail_draw_speed:
            self.trail.append(pg.Rect(self.rect.x, self.rect.y, self.trail_size, self.trail_size))
            self.trail_draw_cnt = 0
        else:
            self.trail_draw_cnt += 1

        dx = self.target[0] - self.rect.centerx
        dy = self.target[1] - self.rect.centery

        distance = math.sqrt(dx**2 + dy**2)

        if math.floor(distance) > 6:
            inc_x = (dx / distance) * self.speed
            inc_y = (dy / distance) * self.speed

            self.rect.x += inc_x
            self.rect.y += inc_y
        else:
            # be done moving
            self.rect.x = self.target[0]
            self.rect.y = self.target[1]

            self.explode((self.target[0], self.target[1]))

    def draw(self, screen):
        for pix in self.trail:
            pg.draw.rect(screen, self.trail_color, pix)

        if not self.reached_target:
            pg.draw.rect(screen, defs.RED, self.rect)

            if not self.is_enemy:
                screen.blit(self.target_marker, self.target)

        # start clearing the trail once it has stopped growing
        if self.reached_target and self.trail:
            if self.trail_fade_cnt == self.trail_fade_speed:
                self.trail.pop(0)
                self.trail_fade_cnt = 0
            else:
                self.trail_fade_cnt += 1

            if not self.explosion.done:
                self.explosion.draw(screen)
