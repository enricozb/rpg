import pygame

from urpg.ui import SliceSprite

def clamp(n, nmin, nmax):
    return max(min(nmax, n), nmin)

class Dialog:
    x = 512
    y = 656
    width = 1000
    height = 200
    image = SliceSprite(
                pygame.image.load('urpg/resources/img/ui_dialog_box.png'), 11
            )

    def __init__(self, message):
        self._message = message
        self._progress = 2

        self.scale()

    def scale(self):
        self.image.width = clamp(Dialog.width * self._progress // 100, 67, self.width)
        self.image.height = clamp(2 * Dialog.height * self._progress // 100, 67, self.height)
        self.image.x = self.x - self.image.width / 2
        self.image.y = self.y - self.image.height / 2

    def handle_event(self, event):
        return False

    def draw(self, surface):
        self.image.draw(surface)

        if self._progress < 100:
            self._progress += 1
            self.scale()

        else:
            pass

