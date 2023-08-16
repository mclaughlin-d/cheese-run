from model.element import Element
from model.character import Character
from model.sound import GameSound

class Token(Element):
    """Represents a token the player can collect.

    Args:
        Element (Element): The parent class.
    """
    MED_TOKEN = {
        'path': 'assets/cheese_med.png',
        'dim': [57, 60]
    }

    def __init__(self, posn: tuple, dim: tuple, imgpath: str, bonus: int = 1) -> None:
        super().__init__(posn, dim, imgpath)
        self._bonus = bonus

    def interact(self, char: Character):
        """Interacts with the given character by incrementing token attributes.

        Args:
            char (Character): The Character being interacted with.
        """
        char.incr_tokens(self._bonus)