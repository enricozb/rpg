import pygame
from pygame.locals import *

from urpg.game_state import *

class UI:
    def __init__(self, game):
        ''' Initializes a UI class bound to its parent Game class '''
        self.game = game

    def render(self):
        if self.game.state == TRANSITION:
            pass
        elif self.game.state == START_MENU:
            self.render_start_menu()
        elif self.game.state == PLAYING:
            pass
        elif self.game.state == PAUSED:
            pass

    def handle_event(self, event):
        pass

    def render_start_menu(self):
        return
        text = self.game.fonts['mono'].render("Hello", False, (255, 255, 255))
        center = (self.game.screen.get_width()/2, self.game.screen.get_height()/2)
        self.game.screen.blit(label, label.get_rect(center=center))


