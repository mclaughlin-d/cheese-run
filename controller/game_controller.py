from view.display import Display
import tkinter as tk
import random
from model.player import Player
# from model.enemy import Enemy
from model.obstacle import Obstacle
from model.token import Token

import time

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

    REFRESH_INTERVAL = 0.005 # constant that controlls time interval between display updates

    def __init__(self):
        # create window: SHOULD THSI BE IN DISPLAY INSTEAD?
        self._display = Display('../assets/background_med.png', 1500, 750)

        self._playing = True
        self._last_refresh = None # initialize when game first created
        self._start_time = None # initialized when game first created

        self.game_objs = []
        self.obstacles = []
        self.obst_canv_objs = []

        self.tokens = []
        self.tok_canv_objs = []

        # self.enemies = []


        self.player = Player(
            100,
            20,
            5,
            ['../assets/mouse_1_med.png', '../assets/mouse_2_med.png'],
            [200, 500], # position, may need to adjust
            [180, 72], 
            0,
            500,
        )

        self.player_state = 'running' # can also be 'jumping' or 'falling'

    def determine_size(self) -> None:
        s_width = self._win.winfo_screenwidth
        s_height = self._win.winfo_screenheight
        

    def create_starting_elements(self) -> None:
        pass

    def gen_obstacle(self):
        """Uses the length of game play to randomly determine obstacle generation
        """
        if random.randint(1, (int(1000 - (time.time() - self._start_time/10000)))) < 100:
            self.add_obstacle()

    def gen_token(self):
        if random.randint(1, (int(1000 - (time.time() - self._start_time/10000)))) < 100:
            self.add_token()

    def add_token(self):
        new_token = Token() # ADD STUFF LATER!
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
        # NOTE - alt is to bind all of these events to window with corresponding lambda functions
        if key == "<space>": 
            if self.player_state != 'jumping':
                self.player.jump()
                self.player_state = 'jumping'
                self.player.set_state(Player.JUMP_STATE)

    def update_posns(self) -> None:
        """Updates the positions of each object in the game.
        """
        for obj in self.game_objs:
            obj.update_posn()

    def update_frames(self) -> None:
        self.player.update_curr_frame()

    def add_obstacle(self) -> None:
        """Adds a new obstacle to the board. 
        """
        new_obstacle = Obstacle()# add parameters later!
        self.obstacles.append(new_obstacle)
        self.obst_canv_objs.append(
            self._display.add_elt(new_obstacle._imgpath, new_obstacle.posn)
        )

    def get_elements(self) -> list:
        self.game_objs = [].extend(self.obstacles).extend(self.tokens).extend(self.enemies)
        return self.game_objs
    
    def player_collide(self):
        # NOTE = may make more sense to mvoe some of these to player instead
        for obst in self.obstacles:
            if obst.is_above(self.player):
                self.player.max_y = obst.posn[1] + obst.dim[1]
            elif obst.is_below(self.player):
                self.player.ground = obst.posn[1]
            elif obst.hit_top(self.player):
                self.player.ground = obst.posn[1]

    def player_collect(self):
        for token in self.tokens:
            if token.collided(self.player):
                token.interact(self.player)
                self.tokens.remove(token)

    def remove_elts(self):
        for i in range(len(self.obstacles)):
            if self.obstacles[i].pos[0] + self.obstacles[i].dim[0] < 0:
                del self.obstacles[i]
                self._display.del_elt(self.obst_canv_objs[i])
                del self.obst_canv_objs[i]

        for token in self.tokens:
            if token.pos[0] + token.dim[0] < 0:
                self.tokens.remove(token)

    def run_game(self) -> None:

        while self._playing:
            # do game stuff

            # refresh the view every 0.005 seconds
            if time.time() - self._last_refresh >= GameController.REFRESH_INTERVAL:
                self._board_control.update_posns()
                self.update_view()
                self._last_refresh = time.time()
