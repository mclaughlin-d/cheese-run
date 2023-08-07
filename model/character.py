from abc import ABC, abstractmethod
from typing import List

class Character(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """

    def __init__(self, hp: int, ran: int, dp: int, frames: List[str], pos: tuple, dim: tuple):
        self._hp = hp
        self._ran = ran
        self._dp = dp
        self._frames = frames
        self.pos = pos
        self.dim = dim

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