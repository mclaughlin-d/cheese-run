from abc import ABC, abstractmethod
from model.character import Character

class Element(ABC):
    """Represents any game component the player can interact with.

    Args:
        ABC (ABC): The abstract base class.
    """
    def __init__(self, posn: tuple, dim: tuple, imgpath: str, vel: tuple) -> None:
        self._posn = posn
        self._dim = dim
        self._imgpath = imgpath
        self._vel = vel

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
        
        def update_posn(self):
            """Updates the elements position based on its velocity.
            """
            self._pos = self._pos[0] + self._vel[0], self._pos[1] + self._vel[1]

        def set_vel(self, x_vel: int, y_vel: int):
            """Sets the velocity attribute based on the parameters passed.

            Args:
                x_vel (int): The new x-velocity of the element.
                y_vel (int): The new y-velocity of the element.
            """
            self._vel = x_vel, y_vel
