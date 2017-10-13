import pygame

from urpg.constants import SCALE
from urpg.ui import SliceSprite

def clamp(n, nmin, nmax):
    return max(min(nmax, n), nmin)

class Dialog:
    # Constant position and dimensions of dialog box
    x = 512
    y = 656
    width = 1000
    height = 200

    # Text starting position
    t_x = x - width / 2 + 33
    t_y = y - height / 2 + 33

    # Bounds of corners
    bound = 11 * SCALE

    # Resources
    image = SliceSprite(
        pygame.image.load('urpg/resources/img/ui_dialog_box.png'),
        bound // SCALE
    )
    font = pygame.font.Font('urpg/resources/ttf/vga.ttf', 32)

    def __init__(self, message):
        self._message = self.prepare_text(message)
        self._text_len = len(message)
        self._progress = {'box': 0, 'text': 0}
        self.scale()

    def prepare_text(self, text):
        words = text.split()
        message = []
        last = 0
        for i in range(len(words)):
            text = self.font.render(
                ' '.join(words[last:i + 1]),
                False,
                [0] * 3
            )

            if text.get_width() > Dialog.width - 2 * Dialog.bound:
                message.append(' '.join(words[last:i]) + ' ')
                last = i

        if last != i + 1:
            message.append(' '.join(words[last:i + 1]))

        return message

    def scale(self):
        self.image.width = clamp(
            Dialog.width * self._progress['box'] // 100,
            2 * Dialog.bound,
            self.width
        )
        self.image.height = clamp(
            2 * Dialog.height * self._progress['box'] // 100,
            2 * Dialog.bound,
            self.height
        )
        self.image.x = self.x - self.image.width / 2
        self.image.y = self.y - self.image.height / 2

    def handle_event(self, event):
        return False

    def draw_text(self, surface):
        progress = int(self._progress['text'])
        line = 0
        for i, line in enumerate(self._message):
            text = self.font.render(line[:progress], False, (255, 255, 255))
            surface.blit(text, (self.t_x, self.t_y + i * text.get_height()))
            progress -= len(line)

            if progress <= 0:
                break

    def draw(self, surface):
        self.image.draw(surface)

        if self._progress['box'] < 100:
            self._progress['box'] += 1
            self.scale()

        else:
            self.draw_text(surface)
            self._progress['text'] = min(
                self._progress['text'] + 0.3,
                self._text_len
            )

