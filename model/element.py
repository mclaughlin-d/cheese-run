from abc import ABC, abstractmethod
from model.character import Character

class Element(ABC):
    """Represents any game component the player can interact with.

    Args:
        ABC (ABC): The abstract base class.
    """
    def __init__(self, posn: tuple, dim: tuple, imgpath: str) -> None:
        self._posn = posn
        self._dim = dim
        self._imgpath = imgpath
        self._vel = (0,0)

        @abstractmethod
        def interact(self):
            pass

        def is_below(self, char: Character) -> bool:
            """Determines whether the obstacle is below the character.

            Args:
                char (Character): The character being tested.

            Returns:
                bool: Whether the obstacle is below the character.
            """
            return(
                (self._posn[0] <= char.pos[0] + char.dim[0] <= self._posn[0] + self._dim[0]) and
                (self._posn[1] < char.pos[1] + char.dim[1])
            )

        def was_hit(self, char: Character) -> bool:
            """Determines if a character has interacted with the game element.

            Args:
                char (Character): The character being tested. 

            Returns:
                bool: Whether or not the character 'hit' the element. 
            """
            return (
                (self._posn[0] <= char.pos[0] + char.dim[0] <= self._posn[0] + self._dim[0]) and
                (self._posn[1] <= char.pos[1] + char.dim[1] <= self._posn[1] + self._dim[1])
            )
        
        def update_posn(self) -> None:
            """Updates the elements position based on its velocity.
            """
            self._posn = self._posn[0] + self._vel[0], self._posn[1] + self._vel[1]

        def set_vel(self, x_vel: int, y_vel: int) -> None:
            """Sets the velocity attribute based on the parameters passed.

            Args:
                x_vel (int): The new x-velocity of the element.
                y_vel (int): The new y-velocity of the element.
            """
            self._vel = x_vel, y_vel
