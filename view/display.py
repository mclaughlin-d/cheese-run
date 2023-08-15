import tkinter as tk
from PIL import Image

class Display():
    """Displays all of the images corresponding to each active game element. 
    """
    # NOTE = cannot have photoimage here bcs tk needs a root window or smth - INVESTIGATE

    def __init__(self, win, bg_path, ground_path, width, height, play_path, player_posn):
        self.win = win

        self.canvas = tk.Canvas(self.win, width=width, height=height)
        self.bg_img = tk.PhotoImage(file=bg_path)
        self.background = self.canvas.create_image(0, 0, image=self.bg_img, anchor="nw")

        self.ground_img = tk.PhotoImage(file=ground_path)
        self.ground = self.canvas.create_image(0, height-90, image=self.ground_img, anchor="nw")

        self.player_img = tk.PhotoImage(file=play_path)
        self.player = self.canvas.create_image(player_posn[0], player_posn[1], image=self.player_img, anchor="nw")
    
        self.token_text = "Tokens Collected: "
        self.token_label = tk.Label(self.win, font='arial', text=self.token_text, anchor='nw')
        self.token_label.place(x=20, y=20)
        self.canvas.pack()


        # may be easier and faster to store in a dict with the filepaths as keys or smth

        self.TOKEN_MED_IMG = tk.PhotoImage(file='assets/cheese_med.png')
        self.OBST_1_MED_IMG = tk.PhotoImage(file='assets/obst_1_med.png')
        self.OBST_2_MED_IMG = tk.PhotoImage(file='assets/obst_2_med.png')
        self.OBST_3_MED_IMG = tk.PhotoImage(file='assets/obst_3_med.png')

    def add_elt(self, path: str, pos: list) -> None:
        print("ADDED ELT")
        img = self.canvas.create_image(pos[0], pos[1], image=self.imgpath_mux(path), anchor="nw")
        self.canvas.pack()
        return img

    def del_elt(self, id):
        self.canvas.delete(id)

    def move_elt(self, elt, pos: list):
        self.canvas.coords(elt, pos[0], pos[1])
    
    def update_player(self, pos: list):
        self.move_elt(self.player, pos)

    def update_player_frame(self, path: str, pos: list):
        self.player_img = tk.PhotoImage(file=path)
        self.player = self.canvas.create_image(pos[0], pos[1], image=self.player_img, anchor="nw")

    def imgpath_mux(self, path):
        if path == 'assets/cheese_med.png':
            return self.TOKEN_MED_IMG
        elif path == 'assets/obst_1_med.png':
            return self.OBST_1_MED_IMG
        elif path == 'assets/obst_2_med.png':
            return self.OBST_2_MED_IMG
        elif path == 'assets/obst_3_med.png':
            return self.OBST_3_MED_IMG
        
    def update_token_msg(self, num_collected):
        self.token_text = "Tokens Collected: " + str(num_collected)
        self.token_label.config(text = self.token_text)