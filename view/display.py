import tkinter as tk
from PIL import Image

class Display():
    """Displays all of the images corresponding to each active game element. 
    """
    def __init__(self, win, bg_path, ground_path, width, height, play_path, player_posn):
        self.win = win

        self.canvas = tk.Canvas(self.win, width=width, height=height)
        self.bg_img = tk.PhotoImage(file=bg_path)
        self.background = self.canvas.create_image(0, 0, image=self.bg_img, anchor="nw")

        self.ground_img = tk.PhotoImage(file=ground_path)
        self.ground = self.canvas.create_image(0, height-90, image=self.ground_img, anchor="nw")

        self.player_img = tk.PhotoImage(file=play_path)
        self.player = self.canvas.create_image(player_posn[0], player_posn[1], image=self.player_img, anchor="nw")
        self.canvas.pack()

    def add_elt(self, path: str, pos: list) -> None:
        return self.canvas.create_image(pos[0], pos[1], image=path)

    def del_elt(self, id):
        self.canvas.delete(id)

    def move_elt(self, elt, pos: list):
        self.canvas.coords(elt, pos[0], pos[1])
    
    def update_player(self, pos: list):
        self.move_elt(self.player, pos)

    def update_player_frame(self, path: str, pos: list):
        self.player_img = tk.PhotoImage(file=path)
        self.player = self.canvas.create_image(pos[0], pos[1], image=self.player_img, anchor="nw")