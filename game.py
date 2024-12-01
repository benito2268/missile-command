import pygame as pg
import random as rand
import defs
import player
import enemy

# a percentage of sorts
ENEMY_SPAWN_CHANCE = 10
ENEMY_SPAWN_OUT_OF = 10000

def main():
    pg.init()

    p = player.Player((0, 0), "sprites/crosshair.png")
    screen = pg.display.set_mode((defs.H_FULL, defs.V_FULL))
    clock = pg.time.Clock()
    bg = pg.image.load("sprites/background.png")

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

        # draw the crosshair
        p.update(screen)
        p.draw(screen)

        # determine whether to spawn an enemy
        i = rand.randint(0, ENEMY_SPAWN_OUT_OF)
        if i < ENEMY_SPAWN_CHANCE:
            enemies.append(enemy.Enemy())

        # TODO remove done enemies
        for e in enemies:
            e.update(screen)
            e.draw(screen)

        pg.display.flip()

if __name__ == "__main__":
    main()