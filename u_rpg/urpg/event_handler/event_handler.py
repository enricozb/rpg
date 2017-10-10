class EventHandler:
    def __init__(self, game):
        self.game = game

        # Order matters, UI first since UI will hopefully never be under the
        # map, and some UI should capture arrow keys
        self.handlers = game.ui, game.map

    def handle(self, event):
        # Likely iterate through UI, then Map, to properly pass events.
        for handler in self.handlers:
            if handler.handle(event):
                break

