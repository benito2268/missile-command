import pygame as pg

class City(pg.sprite.Sprite):
    
    def __init__(self, pos):
        super().__init__()

        self.pos = list(pos)

        self.anim = [
            "sprites/city.png",
            "sprites/city.png", # TODO change 
            "sprites/city.png", # TODO change
        ]

        self.image = pg.image.load(self.anim[0])
        self.rect = self.image.get_rect(center=pos)

        # 3 levels
        # 0=ok, 1=damaged, 2=destroyed
        self.damage_lvl = 0

    def damage(self):
        # just in case - don't bomb destroyed cities
        if self.damage_lvl < 2:
            self.damage_lvl += 1

            # load the new sprite
            self.image = pg.image.load(self.anim[self.damage_lvl])
            self.rect = self.image.get_rect(center=self.pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    