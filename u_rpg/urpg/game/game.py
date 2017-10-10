import pygame
from pygame.locals import *

from urpg.event_handler import EventHandler
from urpg.game_state import GameState
from urpg.map import Map
from urpg.ui import UI

class Game:
    '''
    The class that handles the initialization and destruction of the display
    and is the entrypoint for events.
    '''
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 768), DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self.state = GameState.START_MENU
        self.ui = UI(self)
        self.map = Map()
        self.event_handler = EventHandler(self)
        self.init_fonts()

    def init_fonts(self):
        self.fonts = {}
        self.fonts['mono'] = pygame.font.SysFont("monospace", 30)

    def render(self):
        self.ui.render()
        self.map.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return pygame.QUIT
            #self.event_handler.handle(event)


    def run(self):
        '''
        Entry point for starting the game.
        '''
        while True:
            self.clock.tick()
            self.render()
            if self.handle_events() == pygame.QUIT:
                return
            pygame.display.flip()

