from abc import ABC, abstractmethod
from model.character import Character

class Element(ABC):
    """Represents any game component the player can interact with.

    Args:
        ABC (ABC): The abstract base class.
    """
    def __init__(self, posn: list, dim: tuple, imgpath: str) -> None:
        self.posn = posn
        self.dim = dim
        self._imgpath = imgpath
        self._vel = [-5, 0]

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
            (self.posn[0] <= char.posn[0] + char.dim[0] <= self.posn[0] + self.dim[0]) and
            (self.posn[1] > char.posn[1] + char.dim[1])
        )
    
    def is_above(self, char: Character) -> bool:
        """Determines whether the obstacle is above the character.

        Args:
            char (Character): The character being tested.

        Returns:
            bool: Whether the obstacle is above the character.
        """
        return(
            (self.posn[0] <= char.posn[0] + char.dim[0] <= self.posn[0] + self.dim[0]) and
            (self.posn[1] < char.posn[1])
        )

    def collided(self, char: Character) -> bool:
        """Determines if a character has interacted with the game element.

        Args:
            char (Character): The character being tested. 

        Returns:
            bool: Whether or not the character 'hit' the element. 
        """
        return (
            (self.posn[0] <= char.posn[0] + char.dim[0] <= self.posn[0] + self.dim[0]) and
            (self.posn[1] <= char.posn[1] + char.dim[1] <= self.posn[1] + self.dim[1])
        )
    
    def hit_bottom(self, char: Character) -> bool:
        return (
            (self.posn[0] <= char.posn[0] + char.dim[0] <= self.posn[0] + self.dim[0]) and
            (char.posn[1] <= self.posn[1] + self.dim[1])
        )

    def hit_top(self, char: Character) -> bool:
        return (
            (self.posn[0] <= char.posn[0] + char.dim[0] <= self.posn[0] + self.dim[0]) and
            (char.posn[1] + char.dim[1] <= self.posn[1])
        )
    
    def update_posn(self) -> None:
        """Updates the elements position based on its velocity.
        """
        self.posn[0] += self._vel[0]
        self.posn[1] += self._vel[1]

    def set_vel(self, x_vel: int, y_vel: int) -> None:
        """Sets the velocity attribute based on the parameters passed.

        Args:
            x_vel (int): The new x-velocity of the element.
            y_vel (int): The new y-velocity of the element.
        """
        self._vel = x_vel, y_vel
