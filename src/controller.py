import constants as c
import event_handler


class Controller:
    """Class used to control the game 'scenes' or 'states' ie: load screen,
    level screen, character select. It runs the current states update
    method, and also checks to see if the current state is_done, and then
    flips the game to the next state."""
    def __init__(self, display, clock, state_dict):
        self.display = display
        self.clock = clock
        self.event_handler = event_handler.EventHandler()
        self.state_dict = state_dict
        self.current_state = self.state_dict[c.STARTING_STATE]
        self.running = True

    def run(self):
        """The main game loop"""
        while self.running:
            # Tick the clock and get the change in time (dt)
            dt = self.clock.tick(c.FPS)

            # Handle user input
            self.event_handler.handle_events()

            # Update the current state
            self.current_state.update(dt)
            # If the current state is finished, it runs its flip state method and changes the current state to the next.
            if self.current_state.is_done:
                self.current_state.cleanup()
                self.current_state = self.current_state.flip_state(self.current_state.next_state)

            # Render the display
            self.current_state.render(self.display)
