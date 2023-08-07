from model.element import Element
from model.character import Character

class Token(Element):
    """Represents a token the player can collect.

    Args:
        Element (Element): The parent class.
    """
    def __init__(self, pos: tuple, dim: tuple, imgpath: str, bonus: int) -> None:
        super().__init__(pos, dim, imgpath)
        self._bonus = bonus

        def interact(self, char: Character):
            # NOTE - will need to interact with player specifically to add points
            # or perhaps will call a player method to determine interaction
            return
