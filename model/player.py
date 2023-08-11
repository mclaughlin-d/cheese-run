from typing import List
from model.character import Character

class Player(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """

    FALL_A = 4
    JUMP_Y_VEL = -50
    
    JUMP_STATE = 'jumping'
    FALL_STATE = 'falling'
    RUN_STATE = 'running'

    def __init__(self, hp: int, ran: int, dp: int, frames: List[str], posn: List[int], dim: tuple, tokens: int = 0, ground: int = 500):
        super().__init__(hp, ran, dp, frames, posn, dim, tokens)
        self.vel = [0,0]

        self.ground = ground
        self.max_y = 800 # change to be smth related to board later (max is usually board height, but changes if obstacle abpve)
        self.state = Player.RUN_STATE

    def jump(self):
        if self.posn[1] <= self.max_y:
            self.state = Player.FALL_STATE
            self.vel = [0,0]

        elif self.posn[1] >= self.ground:
            self.state = Player.RUN_STATE
            self.posn[1] = self.ground
            self.vel = [0,0]
        else:
            self.posn[1] += self.vel[1]
            self.vel[1] += Player.FALL_A

    def fall(self):
        # note- need to set initial velocity when these actions change
        if self.posn[1] >= self.ground:
            self.state = Player.RUN_STATE
            self.posn[1] = self.ground
            self.vel = [0,0]
        else:
            self.posn[1] += self.vel[1]
            self.vel[1] += Player.FALL_A

    def set_state(self, state: str) -> None:
        # NOTE - may not even need this?
        # also may be better to just have one state var for string and not use booleans
        if state in [Player.RUN_STATE, Player.FALL_STATE, Player.JUMP_STATE]:
            self.state = state
        else:
            raise ValueError