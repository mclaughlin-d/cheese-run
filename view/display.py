import tkinter as tk
from typing import List

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
        self.rules_label = tk.Label(self.win, font='arial', text=self.rules_text, anchor=tk.N)

        self.score_text = "Your score was: "
        self.score_label = tk.Label(self.win, font='arial', text=self.score_text, anchor='nw')

        self.high_score_text = ""
        self.high_score_label = tk.Label(self.win, font='arial', text = self.rules_text, anchor = tk.N)
        self.name_label = tk.Label(self.win, text="Type your name and press 'enter' to submit your score.\nPress the right arrow key to restart the game, or 'esc' to exit.\n", font='arial', bg='white')
        self.name_entry = tk.Entry(self.win, width=40)

        self.canvas.pack()

        self.TOKEN_MED_IMG = tk.PhotoImage(file='assets/cheese_med.png')
        self.OBST_1_MED_IMG = tk.PhotoImage(file='assets/obst_1_med.png')
        self.OBST_2_MED_IMG = tk.PhotoImage(file='assets/obst_2_med.png')
        self.OBST_3_MED_IMG = tk.PhotoImage(file='assets/obst_3_med.png')
        self.TITLE_IMG = tk.PhotoImage(file='assets/title_med.png')

    def add_elt(self, path: str, pos: List[int]) -> int:
        """Adds an element to the display.

        Args:
            path (str): The path to the element's image file.
            pos (List[int]): A list representing the top left corner coordinates.

        Returns:
            int: The ID of the image object created.
        """
        img = self.canvas.create_image(pos[0], pos[1], image=self.imgpath_mux(path), anchor="nw")
        self.canvas.pack()
        return img

    def place_token_label(self) -> None:
        """Places the token label onto the screen.
        """
        self.token_label.place(x=20, y=20)

    def remove_token_label(self) -> None:
        """Removes the token label from the screen
        """
        self.token_label.place_forget()

    def set_rules(self, rules: str) -> None:
        """Sets the value of the rules label and places it on screen.

        Args:
            rules (str): The rules to be displayed.
        """
        self.rules_text = rules
        self.rules_label.config(text = self.rules_text, image=self.TITLE_IMG, compound='top', bg='white', anchor=tk.N)
        self.rules_label.place(x=485, y=60)

    def remove_rules(self) -> None:
        """Removes the rules label from the screen.
        """
        self.rules_label.place_forget()

    def del_elt(self, id: int) -> None:
        """Deletes the element from the screen.

        Args:
            id (int): The ID of the element to be deleted.
        """
        self.canvas.delete(id)

    def move_elt(self, elt: int, pos: List[int]) -> None:
        """Moves the element to the specified position.

        Args:
            elt (int): The ID of the element to be moved.
            pos (List[int]): The new coordinates of the element.
        """
        self.canvas.coords(elt, pos[0], pos[1])
    
    def update_player(self, pos: List[int]) -> None:
        """Updates the player's position.

        Args:
            pos (List[int]): The new coordinates of the player.
        """
        self.move_elt(self.player, pos)

    def update_player_frame(self, path: str, pos: list) -> None:
        """Updates the player's image being displayed.

        Args:
            path (str): The path to the new image file.
            pos (list): The coordinates of the player.
        """
        self.player_img = tk.PhotoImage(file=path)
        self.player = self.canvas.create_image(pos[0], pos[1], image=self.player_img, anchor="nw")

    def imgpath_mux(self, path: str) -> None:
        """Returns the right PhotoImage object based on the file path.
        """
        if path == 'assets/cheese_med.png':
            return self.TOKEN_MED_IMG
        elif path == 'assets/obst_1_med.png':
            return self.OBST_1_MED_IMG
        elif path == 'assets/obst_2_med.png':
            return self.OBST_2_MED_IMG
        elif path == 'assets/obst_3_med.png':
            return self.OBST_3_MED_IMG
        
    def update_token_msg(self, num_collected: int) -> None:
        """Updates the amount of tokens displayed on the token label.

        Args:
            num_collected (int): The number of tokens currently collected.
        """
        self.token_text = "Tokens Collected: " + str(num_collected)
        self.token_label.config(text = self.token_text, bg='white')

    def get_score_name(self) -> str:
        """Gets the name entered by the user corresponding to the latest run.

        Returns:
            str: The name entered by the user.
        """
        name = self.name_entry.get()
        self.name_entry.config(state=tk.DISABLED)
        self.name_entry.place_forget()
        if name == '':
            name = 'anonymous'
        
        return name
    
    def set_score_label(self, score: int) -> None:
        """Sets the score label after a run.

        Args:
            score (int): The score to be displayed on the label.
        """
        self.score_text = "Your score was: " + str(score)
        self.score_label.config(text = self.score_text, bg='white')

    def set_high_score_label(self, text: str) -> None:
        """Sets the high score label value.

        Args:
            text (str): The text to be displayed for the high score.
        """
        self.high_score_text = text
        self.high_score_label.config(text = self.high_score_text, bg='white')

    def create_score_screen(self) -> None:
        """Creates the score screen by placing the right elements.
        """
        self.score_label.place(relx=0.5, y = 50)
        self.high_score_label.place(relx=0.5, y=100)
        self.name_label.place(relx=0.5, y=150)
        self.name_entry = tk.Entry(self.win, width=40)
        self.name_entry.config(state=tk.NORMAL)
        self.name_entry.place(relx=0.5, y=200)

    def remove_score_screen(self) -> None:
        """Removes the score screen by hiding all the score screen elements
        """
        self.high_score_label.place_forget()
        self.score_label.place_forget()
        self.name_entry.place_forget()
        self.name_label.place_forget()