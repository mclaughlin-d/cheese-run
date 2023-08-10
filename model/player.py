from typing import List
from model.character import Character

class Player(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """
    FALL_A = 4
    JUMP_Y_VEL = -50

    def __init__(self, hp: int, ran: int, dp: int, frames: List[str], posn: List[int], dim: tuple, tokens: int = 0, ground: int = 500):
        super().__init__(hp, ran, dp, frames, posn, dim, tokens)
        self.vel = [0,0]

        self.jumping = False
        self.falling = False

        self.ground = ground

    def jump(self):
        if self.pos[1] >= self.ground:
            self.jumping = False
            self.pos[1] = self.ground
            self.vel = [0,0]
        else:
            self.pos[1] += self.vel[1]
            self.vel[1] += Player.FALL_A

    def fall(self):
        # note- need to set initial velocity when these actions change
        if self.pos[1] >= self.ground:
            self.falling = False
            self.pos[1] = self.ground
            self.vel = [0,0]
        else:
            self.pos[1] += self.vel[1]
            self.vel[1] += Player.FALL_A