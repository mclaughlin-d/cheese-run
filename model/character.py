from abc import ABC, abstractmethod
from typing import List

class Character():
    """_summary_

    """

    def __init__(self, hp: int, ran: int, dp: int, frames: List[str], posn: List[int], dim: tuple, tokens: int = 0):
        self._hp = hp
        self._ran = ran
        self._dp = dp
        self._frames = frames
        self._curr_frame_index = 0
        self.posn = posn
        self.dim = dim
        self._tokens = tokens

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
        self._hp = hp_val

    def incr_tokens(self, t_delta: int) -> None:
        self._tokens += t_delta
        if self._tokens < 0:
            self._tokens = 0

    def update_curr_frame(self) -> None:
        if self._curr_frame_index == len(self._frames - 1):
            self._curr_frame_index = 0
        else:
            self._curr_frame_index += 1

    def get_curr_frame(self) -> str:
        return self._frames[self._get_curr_frame]