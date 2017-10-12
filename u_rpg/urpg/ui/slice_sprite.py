import pygame

class SliceSprite(pygame.sprite.Sprite):

    # Only supports slicing `bound` distance away from every edge.
    def __init__(self, image, bound):
        pygame.sprite.Sprite.__init__(self)

        *_, w, h = image.get_rect()
        self._image = pygame.transform.scale(image, (w * 3, h * 3))
        self._sliced_image = None
        self._rect = self._image.get_rect()
        self._bound = bound * 3

    def draw(self, surface):
        x, y, *_ = self._rect
        if (not self._sliced_image or
                self._sliced_image.get_rect() != self._rect):
            self.generate_slices()

        surface.blit(self._sliced_image, (x, y))

    def generate_slices(self):
        b = self._bound

        x, y, w, h = self._image.get_rect()
        mw = w - 2 * b
        mh = h - 2 * b
        wr = w - b
        hb = h - b

        rects = [
            (0, 0, b, b),  (b, 0, mw, b),  (wr, 0, b, b),
            (0, b, b, mh), (b, b, mw, mh), (wr, b, b, mh),
            (0, hb, b, b), (b, hb, mw, b), (wr, hb, b, b),
        ]

        x, y, w, h = self._rect
        mw = w - 2 * b
        mh = h - 2 * b

        scales = [
            (b, b),  (mw, b),  (b, b),
            (b, mh), (mw, mh), (b, mh),
            (b, b),  (mw, b),  (b, b),
        ]

        translations = [
            (0, 0), (b, 0), (mw + b, 0),
            (0, b), (b, b), (mw + b, b),
            (0, b + mh), (b, b + mh), (mw + b, b + mh),
        ]

        self._sliced_image = pygame.Surface((w, h))
        for rect, scale, translation in zip(rects, scales, translations):
            self._sliced_image.blit(
                pygame.transform.smoothscale(
                    self._image.subsurface(
                        pygame.rect.Rect(rect)
                    ), scale
                ), translation
            )

    @property
    def width(self):
        return self._rect.width

    @width.setter
    def width(self, width):
        self._rect.width = width

    @property
    def height(self):
        return self._rect.height

    @height.setter
    def height(self, height):
        self._rect.height = height

    @property
    def x(self):
        return self._rect.x

    @x.setter
    def x(self, x):
        self._rect.x = x

    @property
    def y(self):
        return self._rect.y

    @y.setter
    def y(self, y):
        self._rect.y = y

