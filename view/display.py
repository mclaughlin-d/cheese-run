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
    
        self.token_text = "Tokens Collected: 0"
        self.token_label = tk.Label(self.win, font='arial', text=self.token_text, anchor='nw')
        
        self.rules_text = ""
        self.rules_label = tk.Label(self.win, font='arial', text=self.rules_text, anchor=tk.CENTER)

        self.score_text = "Your score was: "
        self.score_label = tk.Label(self.win, font='arial', text=self.score_text, anchor='nw')

        self.high_score_text = ""
        self.high_score_label = tk.Label(self.win, font='arial', text = self.rules_text, anchor = tk.CENTER)
        self.name_label = tk.Label(self.win, text="Type your name and press 'enter' to submit.\nThen press the right arrow key to restart the game, or 'esc' to exit.\n", font='arial')
        self.name_entry = tk.Entry(self.win, width=40)

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

    def place_token_label(self):
        self.token_label.place(x=20, y=20)

    def set_rules(self, rules: str):
        self.rules_text = rules
        self.rules_label.config(text = self.rules_text)
        self.rules_label.place(x=30, y=50)

    def remove_rules(self):
        self.rules_label.place_forget()

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

    def get_score_name(self) -> str:
        name = self.name_entry.get()
        self.name_entry.config(state=tk.DISABLED)
        self.name_entry.place_forget()
        if name == '':
            name = 'anonymous'
        
        return name
    
    def set_score_label(self, score) -> None:
        self.score_text = "Your score was: " + str(score)
        self.score_label.config(text = self.score_text)

    def set_high_score_label(self, text) -> None:
        self.high_score_text = text
        self.high_score_label.config(text = self.high_score_text)

    def create_score_screen(self) -> None:

        self.score_label.place(relx=0.5, y = 50)
        self.high_score_label.place(relx=0.5, y=100)
        self.name_label.place(relx=0.5, y=150)
        self.name_entry = tk.Entry(self.win, width=40)
        self.name_entry.config(state=tk.NORMAL)
        self.name_entry.place(relx=0.5, y=200)

    def remove_score_screen(self):
        self.high_score_label.place_forget()
        self.score_label.place_forget()
        self.name_entry.place_forget()
        self.name_label.place_forget()