from abc import ABC, abstractmethod
from model.character import Character

class Element(ABC):
    """Represents any game component the player can interact with.

    Args:
        ABC (ABC): The abstract base class.
    """
    def __init__(self, pos: tuple, dim: tuple, imgpath: str) -> None:
        self._pos = pos
        self._dim = dim
        self._imgpath = imgpath

        @abstractmethod
        def interact(self):
            pass

        def was_hit(self, char: Character):
            """Determines if a character has interacted with the game element.

            Args:
                c_pos (tuple): The character's position coordinate (top left of character)
                c_dim (tuple): The character's dimensions (length and width)

            Returns:
                Bool: Whether or not the character 'hit' the element. 
            """
            return (
                (self._pos[0] <= char.pos[0] + char.dim[0] <= self._pos[0] + self._dim[0]) and
                (self.pos[1] <= char.pos[1] + char.dim[1] <= self._pos[1] + self._dim[1])
            )
