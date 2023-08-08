from model.board import Board
import tkinter as tk

import time

class GameController():
    """Controls gameplay.
    """

    REFRESH_RATE = 0.005 # constant that controlls time interval between display updates

    def __init__(self):
        # create window:
        self._win = tk.Tk()
        self._win.bind('<KeyPress>', self.handle_keypress) #bind keypress to window
       

    def create_starting_elements(self):
        pass

    def handle_keypress(self, key):

        # NOTE - alt is to bind all of these events to window with corresponding lambda functions
        if key == "<Left>":
            pass
        elif key == "<Right>":
            pass
        elif key == "<Up>":
            pass
        elif key == "<Down>":
            pass
        elif key == "<Space>": # guessing on this name here
            pass

    def run_game(self):
        pass   