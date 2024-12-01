import pygame as pg

class Explosion:
    def __init__(self, pos):
        self.pos = pos
        self.anim = [
            "sprites/explosion1.png",
            "sprites/explosion2.png",
            "sprites/explosion3.png",
            "sprites/explosion4.png",
            "sprites/explosion5.png",
        ]

        self.stage = 0
        self.done = False

        # controls how many frames between each transition of the animation
        self.anim_speed = 10
        self.anim_cnt = 0

        self.image = pg.image.load(self.anim[0])
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, screen):
        if self.stage == len(self.anim):
            if self.anim_cnt != len(self.anim):
                self.anim_cnt += 1
                return
            self.done = True
            return

        if self.anim_cnt == self.anim_speed:
            self.image = pg.image.load(self.anim[self.stage])
            self.rect = self.image.get_rect(center=self.pos)
            self.stage += 1
            self.anim_cnt = 0
        else:
            self.anim_cnt += 1


    def draw(self, screen):
        screen.blit(self.image, self.rect)