from typing import List

class Character():
    """A class to represent a character in the game.
    """

    def __init__(self, hp: int, ran: int, dp: int, frames: List[str], posn: List[int], dim: tuple, tokens: int = 0):
        self._hp = hp
        self._ran = ran
        self._dp = dp
        self._frames = frames
        self._curr_frame_index = 0
        self.posn = posn
        self.dim = dim
        self.tokens = tokens # should change to token_bonus or smth
        self.num_tokens = 0

    def update_hp(self, hp_delta: int) -> None:
        """Updates the hp of the character.

        Args:
            hp_delta (int): The change in hp.
        """
        self.set_hp(self._hp + hp_delta)

    def set_hp(self, hp_val: int) -> None:
        """Sets the characters hp attribute.

        Args:
            hp_val (int): The new hp value.
        """
        if type(hp_val) == int:
            self._hp = hp_val
    
    def check_hp(self) -> int:
        """Used to get the value of a Character's hp.

        Returns:
            int: The character's current hp.
        """
        return self._hp

    def incr_tokens(self, t_delta: int) -> None:
        """Increments the token bonus and the number of tokens.

        Args:
            t_delta (int): The bonus provided by the collected token.
        """
        self.tokens += t_delta
        self.num_tokens += 1
        if self.tokens < 0:
            self.tokens = 0

    def update_curr_frame(self) -> None:
        """Changes the currently displayed frame of the Character.
        """
        if self._curr_frame_index == len(self._frames) - 1:
            self._curr_frame_index = 0
        else:
            self._curr_frame_index += 1

    def get_curr_frame(self) -> str:
        """Gets the currently displayed frame of the Character.

        Returns:
            str: A path to the Character's current frame. 
        """
        return self._frames[self._curr_frame_index]