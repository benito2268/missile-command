import pygame as pg
import random as rand
import defs
import player
import enemy
import city
import math

# a percentage of sorts
ENEMY_SPAWN_CHANCE = 1
ENEMY_SPAWN_OUT_OF = 300

# generator that gives the amount of enemies in a round
def get_round_caps():
    # will crash after round 999
    for i in range(999):
        # + 3 to ensure log(i) >= 1
        yield int(20 * math.log(i + 3))

def main():
    pg.init()
    pg.font.init()

    p = player.Player((0, 0), "sprites/crosshair.png")
    screen = pg.display.set_mode((defs.H_FULL, defs.V_FULL))
    clock = pg.time.Clock()
    bg = pg.image.load("sprites/background.png")
    base = pg.image.load("sprites/base.png")

    # hard code cities for now (ever?)
    cities = [
        city.City((260, 900)),
        city.City((500, 890)),
        city.City((900, 880)),
        city.City((1140, 900)),
    ]

    round_caps = iter(get_round_caps())
    round_cap = next(round_caps)
    round_no = 1
    en_this_round = 0
    enemies = []

    # main game loop
    while True:
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit(0)

        #pg.draw.rect(screen, defs.RED, pg.Rect(100, 100, 6, 6))
        screen.fill(defs.BLACK)
        screen.blit(bg, (0,0))
        screen.blit(base, (0, defs.V_FULL - 200))

        # draw the crosshair
        p.update(screen, enemies)
        p.draw(screen)

        # determine whether to spawn an enemy
        if en_this_round <= round_cap:
            i = rand.randint(0, ENEMY_SPAWN_OUT_OF)
            if i < ENEMY_SPAWN_CHANCE:
                enemies.append(enemy.Enemy(cities))
                en_this_round += 1
        else:
            round_cap = next(round_caps)
            en_this_round = 0
            round_no += 1

        for c in cities:
            c.draw(screen)

        # TODO this part doesn't work
        #to_rm = []
        for i, e in enumerate(enemies):
            e.update(screen, enemies)
        
        #   if e.explosion and e.explosion.done:
        #        to_rm.append(i)
        #
            e.draw(screen)

        #for i in to_rm:
        #    del enemies[i]

        pg.display.flip()

if __name__ == "__main__":
    main()