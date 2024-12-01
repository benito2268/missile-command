import pygame as pg
import missile
import defs

class Player(pg.sprite.Sprite):

    def __init__(self, pos, image):
        super().__init__()
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect(center=pos)
        self.pos = list(pos)
        self.CURSOR_SPEED = 5
        self.ticks = 0
        self.can_fire = True
        self.missiles = []
        
    # fire a missle
    def fire(self, pos, screen):
        if self.can_fire:
            print(f'fired a missile at {pos}')
            m = missile.Missile(pos)
            #m = pg.Rect(*pos, 10, 10)
            self.missiles.append(m)
            self.can_fire = False

    # move the crosshair when wasd pressed
    def update(self, screen):
        keys = pg.key.get_pressed()
        d_x = keys[pg.K_d] - keys[pg.K_a]
        d_y = keys[pg.K_s] - keys[pg.K_w]

        self.ticks += 1
        if self.ticks == 60:
            self.can_fire = True
            self.ticks = 0

        # check if a bullet was fired
        if keys[pg.K_SPACE]:
            self.fire(self.rect.center, screen)

        self.rect.x += d_x * self.CURSOR_SPEED
        self.rect.y += d_y * self.CURSOR_SPEED
        self.rect.clamp_ip(screen.get_rect())

        # update all the players missiles
        # TODO delete missiles that are done
        for m in self.missiles:
            m.update(screen)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        # draw the players missiles
        for m in self.missiles:
            m.draw(screen)