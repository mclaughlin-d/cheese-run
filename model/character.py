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
        self._pos = pos
        self._dim = dim

