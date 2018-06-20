class State:
    """Base class for a game state. All game states should inherit from this base Class."""
    def __init__(self):
        self.is_done = False
        self.next_state = None

    def update(self, dt):
        pass

    def change_state(self, next_state):
        self.next_state = next_state

    def cleanup(self):
        self.is_done = False

