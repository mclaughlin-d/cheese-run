# from model.player import Player
# from model.enemy import Enemy
from model.obstacle import Obstacle
from model.token import Token


class BoardController():
    """Stores all of the game elements currently active.
    """
    def __init__(self):
        self.game_objs = []

        pass

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
        elif key == "<Space>": # guessing on this name here
            pass

    def update_posns(self) -> None:
        """Updates the positions of each object in the game.
        """
        for obj in self.game_objs:
            obj.update_posn()