from controller.board_controller import BoardController
import tkinter as tk
import random

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
        self._last_refresh = None # initialize when game first created
        self._start_time = None # initialized when game first created
       

    def create_starting_elements(self) -> None:
        pass

    def handle_keypress(self, key) -> None:
        self._board_control.handle_keypress(key)

    def gen_obstacle(self):
        """Uses the length of game play to randomly determine obstacle generation
        """
        if random.randint(1, (int(1000 - (time.time() - self._start_time/10000)))) < 100:
            self._board_control.add_obstacle()

    def run_game(self) -> None:

        while self._playing:
            # do game stuff

            # refresh the view every 0.005 seconds
            if time.time() - self._last_refresh >= GameController.REFRESH_INTERVAL:
                self._board_control.update_posns()
                # AND UPDATE IN VIEW AS WELL!!!
                self._last_refresh = time.time()

            
