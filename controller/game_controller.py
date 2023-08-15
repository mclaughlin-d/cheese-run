import random
import time
import tkinter as tk

from view.display import Display
from model.player import Player
from model.obstacle import Obstacle
from model.token import Token
from model.sound import GameSound


class GameController():
    """Controls gameplay.
    """

    """Stores all of the game elements currently active.
    """
    SMALL_SIZE = None
    MED_SIZE = {
        'board-width': 1200, # could change idk check background img size
        'board-height': 700,
        'player-width': 180,
        'player-height': 72,
        'player-frames': ['../assets/mouse_1_med.png', '../assets/mouse_2_med.png'],

    }
    LARGE_SIZE = None

    sizes = [SMALL_SIZE, MED_SIZE, LARGE_SIZE]

    REFRESH_INTERVAL = 0.008 # constant that controlls time interval between display updates

    SCORES_PATH = 'assets/text/scores.txt'

    def __init__(self):
        # create window: SHOULD THSI BE IN DISPLAY INSTEAD?

        self.win = tk.Tk()
        self.win.title("Cheese Run")
        self.win.bind('<space>', self.handle_keypress) #bind keypress to window
        self.win.bind('<Escape>', lambda e: self.win.destroy())
        self.win.bind('<Return>', self.write_score)
        self.win.bind('<Right>', self.restart_game)
        self._display = Display(self.win, 'assets/background_med.png', 'assets/ground_med.png', 1500, 750, 'assets/mouse_1_med.png', [200,592])

        self._playing = False
        self._start_screen = True
        self._running = True
        self._score_screen = False
        self._last_refresh = None # initialize when game first created
        self._start_time = None # initialized when game first created
        self._last_player_refresh = None

        self.game_objs = []
        self.obstacles = []
        self.obst_canv_objs = []

        self.tokens = []
        self.tok_canv_objs = []

        self.random_cieling = 10000

        # sounds:
        self.token_sound = GameSound(GameSound.TOKEN_SOUND)
        self.jump_sound = GameSound(GameSound.JUMP_SOUND)

        self.elt_vel = [-5, 0]

        self.player = Player(
            100,
            20,
            5,
            ['assets/mouse_1_med.png', 'assets/mouse_2_med.png'],
            [200, 592], # position, may need to adjust
            [180, 78], 
            0,
            592,
        )

    def determine_size(self) -> None:
        """Determines the sizes of the files/window based on the screen size.
        """
        s_width = self._win.winfo_screenwidth
        s_height = self._win.winfo_screenheight
        
    def set_rules(self, rule_filepath: str) -> None:
        """Sets the rules label for the display.

        Args:
            rule_filepath (str): The filepath for the rules.txt file.
        """
        rules_str = ""
        try:
            with open(rule_filepath, 'r') as f:
                for line in f:
                    rules_str += line
                    if line.strip('\n')[-1] == '.':
                        rules_str += '\n'

        except FileNotFoundError:
            print("File not found.")
            return
        
        self._display.set_rules(rules_str)


    def update_rand_cieling(self) -> None:
        self.random_cieling = int(self.random_cieling - (time.time() - self._start_time)/100)
        if self.random_cieling < 100:
            self.random_cieling = 100

    def gen_obstacle(self):
        """Uses the length of game play to randomly determine obstacle generation
        """
        if random.randint(1, self.random_cieling) < 20:
            type = random.randint(1, 2)
            if type == 1:
                self.add_obstacle(
                    [1500 + Obstacle.TYPE_1['dim'][0], 660 - Obstacle.TYPE_1['dim'][1]],
                    Obstacle.TYPE_1['dim'],
                    Obstacle.TYPE_1['path'],
                    True,
                    1
                )
            elif type == 2:
                self.add_obstacle(
                    [1500 + Obstacle.TYPE_2['dim'][0],660 - Obstacle.TYPE_2['dim'][1]],
                    Obstacle.TYPE_2['dim'],
                    Obstacle.TYPE_2['path'],
                    True,
                    2
                )
            elif type == 3:
                self.add_obstacle(
                    [1500 + Obstacle.TYPE_3['dim'][0], 660 - Obstacle.TYPE_3['dim'][1]],
                    Obstacle.TYPE_3['dim'],
                    Obstacle.TYPE_3['path'],
                    True,
                    3
                )

    def gen_token(self):
        if random.randint(1, 10000) < 20:
            y_pos = random.randint(50, 580 - Token.MED_TOKEN['dim'][1])
            self.add_token(
                [1500 + Token.MED_TOKEN['dim'][0], y_pos],
                Token.MED_TOKEN['dim'],
                Token.MED_TOKEN['path']
            )

    def add_token(self, pos, dim, path):
        new_token = Token(pos, dim, path)
        self.tokens.append(new_token)
        self.tok_canv_objs.append(
            self._display.add_elt(new_token._imgpath, new_token.posn)
        )

    def update_view(self):
        for obst, obst_obj in zip(self.obstacles, self.obst_canv_objs):
            self._display.move_elt(obst_obj, obst.posn)
        
        for tok, tok_obj in zip(self.tokens, self.tok_canv_objs):
            self._display.move_elt(tok_obj, tok.posn)

    def update_player_posn(self):
        self._display.update_player(self.player.posn[0], self.player.posn[1])

    def handle_keypress(self, key) -> None:
       
        if self._start_screen:
            self._start_screen = False
            self._score_screen = False
            self._playing = True

        elif self._playing:
            if self.player.state == Player.RUN_STATE:
                self.player.jump()
                self.jump_sound.play_async()
                self.player.set_state(Player.JUMP_STATE)

    def restart_game(self, key) -> None:
        self._score_screen = False
        self._start_screen = True
        self._display.remove_score_screen()
        self.player = Player(
            100,
            20,
            5,
            ['assets/mouse_1_med.png', 'assets/mouse_2_med.png'],
            [200, 592], # position, may need to adjust
            [180, 78], 
            0,
            592,
        )

        for obj in self.obst_canv_objs:
            self._display.del_elt(obj)
        for tok_obj in self.tok_canv_objs:
            self._display.del_elt(tok_obj)

        self.obstacles = []
        self.obst_canv_objs = []
        self.tokens = []
        self.tok_canv_objs = []

    def update_posns(self) -> None:
        """Updates the positions of each object in the game.
        """
        for obst in self.obstacles:
            obst.update_posn()
        for tok in self.tokens:
            tok.update_posn()

    def update_frames(self) -> None:
        self.player.update_curr_frame()

    def add_obstacle(self, pos, dim, path, block, type) -> None:
        """Adds a new obstacle to the board. 
        """
        if len(self.obstacles) > 0:
            last_obst = self.obstacles[-1]
            if pos[0] > 1500 and last_obst.x_overlap(pos[0], dim[0]):
                return
            
        new_obstacle = Obstacle(pos, dim, path, block, type)# add parameters later!
        new_obstacle.vel = self.elt_vel
        self.obstacles.append(new_obstacle)
        self.obst_canv_objs.append(
            self._display.add_elt(new_obstacle._imgpath, new_obstacle.posn)
        )

    def update_elt_vel(self) -> None:
        self.elt_vel = [-1 * int(5 + 2*(time.time() - self._start_time)), 0]
    
    def player_collide(self):
        # NOTE = may make more sense to mvoe some of these to player instead
        is_above = False
        for obst in self.obstacles:
            if obst.is_above(self.player):
                self.player.min_y = obst.posn[1] + obst.dim[1]
            elif obst.is_below(self.player):
                self.player.ground = obst.posn[1] - self.player.dim[1]
                is_above = True
            elif obst.collided(self.player):
                obst.interact(self.player)

        if (not is_above) and self.player.ground != 592:
            self.player.set_state(Player.FALL_STATE)
            self.player.ground = 592
            self.player.vel = [0, 3]
            self.player.fall()

    def player_collect(self):
        tokens_to_del = []
        tok_canv_objs_to_del = []
        for i in range(len(self.tokens)):
            token = self.tokens[i]
            if token.collided(self.player):
                tokens_to_del.append(token)
                tok_canv_objs_to_del.append(self.tok_canv_objs[i])
                token.interact(self.player)
                self.token_sound.play_async()
                self._display.del_elt(self.tok_canv_objs[i])
                self._display.update_token_msg(self.player.num_tokens)

        for tok, obj in zip(tokens_to_del, tok_canv_objs_to_del):
            self.tokens.remove(tok)
            self.tok_canv_objs.remove(obj)

    def remove_elts(self):
        obst_to_remove = []
        obst_obj_to_remove = []
        for i in range(len(self.obstacles)):
            if self.obstacles[i].posn[0] + self.obstacles[i].dim[0] < 0:
                obst_to_remove.append(self.obstacles[i])
                self._display.del_elt(self.obst_canv_objs[i])
                obst_obj_to_remove.append(self.obst_canv_objs[i])

        for obst, obj in zip(obst_to_remove, obst_obj_to_remove):
            self.obstacles.remove(obst)
            self.obst_canv_objs.remove(obj)

        tokens_to_remove = []
        tok_obj_to_remove = []
        for i in range(len(self.tokens)):
            token = self.tokens[i]
            if token.posn[0] + token.dim[0] < 0:
                tokens_to_remove.append(token)
                tok_obj_to_remove.append(self.tok_canv_objs[i])

        for tok, tok_obj in zip(tokens_to_remove, tok_obj_to_remove):
            self.tokens.remove(tok)
            self.tok_canv_objs.remove(tok_obj)

    def calc_score(self):
        time_factor = int(time.time() - self._start_time)
        token_factor = self.player.tokens
        return time_factor * 10 + token_factor

    def write_score(self, key):
        score = self.calc_score()
        name = self.get_name()
        try:
            with open(GameController.SCORES_PATH, 'a') as f:
                f.write('\n' + name + ' ' + str(score))

        except FileNotFoundError:
            print("Scores file not found.")
            return
        
    def get_high_score(self) -> str:
        high_score = 0
        high_name = 'anonymous'
        try:
            with open(GameController.SCORES_PATH, 'r') as f:
                for line in f:
                    try: 
                        stuff = line.split()
                        name = ' '.join(stuff[0:len(stuff) - 1])
                        score = int(stuff[-1])
                        if score > high_score:
                            high_score = score
                            high_name = name
                    except:
                        print("Error getting data.")
                
        except FileNotFoundError:
            print("Scores file not found.")
            return high_score
        
        return high_name, high_score
    
    def set_high_score_label(self):
        name, score = self.get_high_score()
        self._display.set_high_score_label(f"The high score:\n{name}: {score}")

    def get_name(self):
        return self._display.get_score_name()

    def run_game(self) -> None:
        # starting stuff
        # grab screen size
        # determine window sizes and all that - ORand pass to game object do this elsewhere 
        # change objects as needed

        # set start time

        # intro screen stuff
        
        while self._running:
            self.random_cieling = 10000
            self.set_rules('assets/text/rules.txt')
            self._start_time = time.time()
            self._last_refresh = self._start_time
            self._last_player_refresh = self._start_time
            while self._start_screen:
                self.win.update_idletasks()
                self.win.update()
            self._display.remove_rules()
            self._display.update_token_msg(0)
            self._display.place_token_label()
            # do game stuff
            while self._playing:
            # refresh the view every 0.005 seconds
                if time.time() - self._last_refresh >= GameController.REFRESH_INTERVAL:
                    # randomly generate new obstacles and tokens
                    self.gen_obstacle()
                    self.gen_token()

                    self.update_posns()
                    self.player_collide()
                    self.player_collect()
                    self.remove_elts()
                    self.update_view()

                    if self.player.state == Player.JUMP_STATE:
                        self.player.jump()
                        self._display.update_player(self.player.posn)
                    elif self.player.state == Player.FALL_STATE:
                        self.player.fall()
                        self._display.update_player(self.player.posn)

                    self._last_refresh = time.time()
                    self.update_rand_cieling()

                if time.time() - self._last_player_refresh >= Player.WALK_INTERVAL:
                    self.player.update_curr_frame()
                    self._display.update_player_frame(self.player.get_curr_frame(), self.player.posn)
                    self._last_player_refresh = time.time()
                    

                if self.player.check_hp() <= 0:
                    self._playing = False

                self.win.update_idletasks()
                self.win.update()

            self._display.remove_token_label()
            self._score_screen = True
            self._display.set_score_label(self.calc_score())
            self.set_high_score_label()
            self._display.create_score_screen()
            while self._score_screen:
                self.win.update_idletasks()
                self.win.update()
            
            self._start_screen = True