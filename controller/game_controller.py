from controller.board_controller import BoardController
import tkinter as tk

import time

class GameController():
    """Controls gameplay.
    """

    REFRESH_INTERVAL = 0.005 # constant that controlls time interval between display updates

    def __init__(self):
        # create window: SHOULD THSI BE IN DISPLAY INSTEAD?
        self._win = tk.Tk()
        self._win.bind('<KeyPress>', self.handle_keypress) #bind keypress to window

        self._board_control = BoardController()

        self._playing = True
        self._last_refresh = None #initialize when game first created
       

    def create_starting_elements(self) -> None:
        pass

    def handle_keypress(self, key) -> None:
        self._board_control.handle_keypress(key)

    def run_game(self) -> None:

        while self._playing:
            # do game stuff

            # refresh the view every GameController.REFRESH_INTERVAL
            if time.time() - self._last_refresh >= GameController.REFRESH_INTERVAL:
                self._board_control.update_posns()
                # AND UPDATE IN VIEW AS WELL!!!
                self._last_refresh = time.time()

        pass   