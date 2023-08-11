from controller.board_controller import BoardController
from view.display import Display
import tkinter as tk
import random

import time

class GameController():
    """Controls gameplay.
    """

    REFRESH_INTERVAL = 0.005 # constant that controlls time interval between display updates

    def __init__(self):
        # create window: SHOULD THSI BE IN DISPLAY INSTEAD?
        self._display = Display('../assets/background_med.png', 1500, 750)

        self._board_control = BoardController()


        self._playing = True
        self._last_refresh = None # initialize when game first created
        self._start_time = None # initialized when game first created

        self.elt_tags = {

        }
       

    def determine_size(self) -> None:
        s_width = self._win.winfo_screenwidth
        s_height = self._win.winfo_screenheight
        

    def create_starting_elements(self) -> None:
        pass

    def handle_keypress(self, key) -> None:
        self._board_control.handle_keypress(key)

    def gen_obstacle(self):
        """Uses the length of game play to randomly determine obstacle generation
        """
        if random.randint(1, (int(1000 - (time.time() - self._start_time/10000)))) < 100:
            self._board_control.add_obstacle()

    def update_view(self):
        pass

    def run_game(self) -> None:

        while self._playing:
            # do game stuff

            # refresh the view every 0.005 seconds
            if time.time() - self._last_refresh >= GameController.REFRESH_INTERVAL:
                self._board_control.update_posns()
                # AND UPDATE IN VIEW AS WELL!!!
                self._last_refresh = time.time()

            
