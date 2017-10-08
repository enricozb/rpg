'''
Using Pygame to load a sample map
'''
import pygame
from pygame.locals import *

sample_map = [[(1, 0), (1, 0), (1, 0), (0, 0)],
              [(1, 0), (0, 0), (1, 0), (1, 0)],
              [(0, 0), (1, -1), (1, 0), (1, 0)],
              [(1, -1), (1, -2), (0, -1), (1, 0)]]

class Game:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont("monospace", 15)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1024, 768), DOUBLEBUF)

        self.grass = pygame.image.load("grass.png").convert_alpha()
        self.dirt = pygame.image.load("dirt.png").convert_alpha()

        size = self.grass.get_size()

        self.grass = pygame.transform.scale(self.grass, (size[0] * 3, size[1] * 3))
        self.dirt = pygame.transform.scale(self.dirt, (size[0] * 3, size[1] * 3))

    def naturals(self):
        count = 0
        while True:
            yield count
            count += 1

    def render_fps(self):
        label = self.font.render("FPS: " + str(self.clock.get_fps()), 1, (255,255,0))
        self.screen.blit(label, (100, 100))

    def render_map(self, loc):
        import math
        W = self.grass.get_width()
        H = self.grass.get_height()
        zhat = (-W//2, H//3)
        what = (-zhat[0], zhat[1])
        yhat = (0, -zhat[1])

        for r, row in enumerate(sample_map):
            for c, tile in enumerate(row):
                tile, h = tile
                h = math.sin(c + r + (pygame.time.get_ticks()/300))
                n_loc = (l + r * z + c * w + h * y for l, z, w, y in zip(loc, zhat, what, yhat))
                n_loc = list(n_loc)
                self.screen.blit(self.grass if tile else self.dirt, n_loc)

    def main_loop(self):
        for count in self.naturals():
            self.screen.fill(0)
            self.clock.tick()
            self.render_fps()
            self.render_map((200,200))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

Game().main_loop()
