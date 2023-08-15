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
            (self.x_overlap(char.posn[0], char.dim[0])) and
            (self.posn[1] >= char.posn[1] + char.dim[1])
        )
    
    def is_above(self, char: Character) -> bool:
        """Determines whether the obstacle is above the character.

        Args:
            char (Character): The character being tested.

        Returns:
            bool: Whether the obstacle is above the character.
        """
        return(
            (self.x_overlap(char.posn[0], char.dim[0])) and
            (self.posn[1] + self.dim[1] < char.posn[1])
        )

    def collided(self, char: Character) -> bool:
        """Determines if a character has interacted with the game element.

        Args:
            char (Character): The character being tested. 

        Returns:
            bool: Whether or not the character 'hit' the element. 
        """
        if char.ground == self.posn[1] - char.dim[1]:
            return False
        else:
            return (
                self.x_overlap(char.posn[0], char.dim[0]) and self.y_overlap(char.posn[1], char.dim[1])
            )

    
    def hit_bottom(self, char: Character) -> bool:
        """

        Args:
            char (Character): _description_

        Returns:
            bool: _description_
        """
        print("THIS METHOD WAS CALLED!")
        return (
            (self.posn[0] <= char.posn[0] + char.dim[0] <= self.posn[0] + self.dim[0]) and
            (char.posn[1] <= self.posn[1] + self.dim[1])
        )

    def hit_top(self, char: Character) -> bool:
        return (
            (self.posn[0] <= char.posn[0] + char.dim[0] <= self.posn[0] + self.dim[0]) and
            (char.posn[1] + char.dim[1] <= self.posn[1] + 5)
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
        self._vel = [x_vel, y_vel]

    def x_overlap(self, x, width) -> bool:
        """Determines whether the character's and obstacle's horizontal positions overlap.

        Args:
            char (Character): The character being tested

        Returns:
            bool: Whether or not their horizontal positions overlap
        """
        return (
            self.posn[0] <= x + width <= self.posn[0] + self.dim[0] or
            self.posn[0] <= x + 70 <= self.posn[0] + self.dim[0]
        )
    
    def y_overlap(self, y, width) -> bool:
        """Determines whether the character's and obstacle's vertical positions overlap.

        Args:
            char (Character): The character being tested

        Returns:
            bool: Whether or not their vertical positions overlap
        """
        return (
            self.posn[1] <= y <= self.posn[1] + self.dim[1] or
            self.posn[1] <= y + width <= self.posn[1] + self.dim[1]
        )