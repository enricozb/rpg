import pygame
from pygame.locals import *

from urpg.game_state import GameState
from urpg.ui import Dialog, SliceSprite

class UI:
    def __init__(self, game):
        ''' Initializes a UI class bound to its parent Game class '''
        self.game = game
        self.dialogs = [Dialog('Hello, World!')]

        self.image = pygame.image.load('urpg/resources/img/ui_dialog_box.png')
        self.image = SliceSprite(self.image, 11)
        self.image.width = 500
        self.image.height = 100
        self.image.x = 100
        self.image.y = 100

    def render(self):
        if self.game.state == GameState.TRANSITION:
            pass
        elif self.game.state == GameState.START_MENU:
            self.render_start_menu()
        elif self.game.state == GameState.PLAYING:
            pass
        elif self.game.state == GameState.PAUSED:
            pass

    def handle_event(self, event):
        if self.dialogs:
            if self.dialogs[-1].handle_event(event):
                self.dialogs.pop()

    def render_start_menu(self):
        if self.dialogs:
            self.dialogs[-1].draw(self.game.screen)
