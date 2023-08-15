from typing import List
from model.character import Character

class Player(Character):
    """A class to represent the player of the game.

    Args:
        Character (Character): The parent class.
    """

    FALL_A = 3
    JUMP_Y_VEL = -50
    
    JUMP_STATE = 'jumping'
    FALL_STATE = 'falling'
    RUN_STATE = 'running'

    WALK_INTERVAL = 0.4

    def __init__(self, hp: int, ran: int, dp: int, frames: List[str], posn: List[int], dim: tuple, tokens: int = 0, ground: int = 592):
        super().__init__(hp, ran, dp, frames, posn, dim, tokens)
        self.vel = [0,0]

        self.ground = ground
        self.min_y = 50
        self.state = Player.RUN_STATE

    def jump(self):
        """Used to update the player's attributes while the player is jumping.
        """
        if self.posn[1] <= self.min_y:
            self.set_state(Player.FALL_STATE)
            self.vel = [0,0]

        elif self.posn[1] + self.vel[1] > self.ground:
            self.set_state(Player.RUN_STATE)
            self.posn[1] = self.ground
            self.vel = [0,0]

        else:
            self.posn[1] += self.vel[1]
            self.vel[1] += Player.FALL_A

    def fall(self):
        """Used to update the player's attributes while the player is falling.
        """
        if self.posn[1] >= self.ground:
            self.state = Player.RUN_STATE
            self.posn[1] = self.ground
            self.vel = [0,0]
        else:
            self.posn[1] += self.vel[1]
            self.vel[1] += Player.FALL_A

    def set_state(self, state: str) -> None:
        """Sets the state and modifies appropriate player attributes.

        Args:
            state (str): The new state of the player.

        Raises:
            ValueError: The state given was not an accepted state value.
        """
        self.state = state 
        if state == Player.JUMP_STATE:
            self.vel = [0, Player.JUMP_Y_VEL]
        elif state == Player.FALL_STATE or state == Player.RUN_STATE:
            self.vel = [0,0]
        else:
            raise ValueError