from model.board import Board
import tkinter as tk

class GameController():
    """Controls gameplay.
    """
    def __init__(self):

        # create window:
        self._win = tk.Tk()
        self._win.bind('<KeyPress>', self.handle_keypress) #bind keypress to window
        
        pass

    def create_starting_elements(self):
        pass

    def handle_keypress(self, key):
        pass
