import tkinter as tk

class Display():
    """Displays all of the images corresponding to each active game element. 
    """
    def __init__(self, bg_path, width, height, play_path, player_posn):
        self.win = tk.Tk()
        self.win.bind('<KeyPress>', self.handle_keypress) #bind keypress to window

        self.canvas = tk.Canvas(self.win, width, height)
        self.background = self.canvas.create_image(0, 0, image=tk.PhotoImage(bg_path))
        self.player = self.canvas.create_image(player_posn[0], player_posn[1], image=tk.PhotoImage(play_path))
        self.canvas.pack()

    def add_elt(self, path: str, pos: list) -> None:
        return self.canvas.create_image(pos[0], pos[1], image=path)

    def del_elt(self, id):
        self.canvas.delete(id)

    def move_elt(self, elt, pos: list):
        self.canvas.coords(elt, pos[0], pos[1])

    def handle_keypress(self, key):
        return key
    
    def update_player(self, x, y):
        pass