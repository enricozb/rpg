# __all__ = ["GameState", "TRANSITION", "START_MENU", "PLAYING", "PAUSED"]

TRANSITION_VAL = 0
START_MENU_VAL = 1
PLAYING_VAL = 2
PAUSED_VAL = 3

class GameState:
    def __init__(self, state=START_MENU_VAL, from_state=None, to_state=None):
        self.state = state
        self.from_state = from_state
        self.to_state = to_state

    def __eq__(self, other):
        return self.state == other.state

    def __ne__(self, other):
        return not self.__eq__(other)

# Game states:
TRANSITION = GameState(TRANSITION_VAL)
START_MENU = GameState(START_MENU_VAL)
PLAYING = GameState(PLAYING_VAL)
PAUSED = GameState(PAUSED_VAL)