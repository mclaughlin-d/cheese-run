from model.player import Player
# from model.enemy import Enemy
from model.obstacle import Obstacle
from model.token import Token


class BoardController():
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

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self.game_objs = []
        self.obstacles = []
        self.tokens = []
        self.enemies = []

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

    def handle_keypress(self, key) -> None:
        # NOTE - alt is to bind all of these events to window with corresponding lambda functions
        if key == "<Left>":
            pass
        elif key == "<Right>":
            pass
        elif key == "<Up>":
            pass
        elif key == "<Down>":
            pass
        elif key == "<space>": 
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
        for obst in self.obstacles:
            if obst.pos[0] + obst.dim[0] < 0:
                self.obstacles.remove(obst)

        for token in self.tokens:
            if token.pos[0] + token.dim[0] < 0:
                self.tokens.remove(token)