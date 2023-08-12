from model.element import Element
from model.character import Character

class Obstacle(Element):
    """Represents an obstacle that hinders the player.

    Args:
        Element (Element): The parent class.
    """

    TYPE_1 = {
        'path': 'assets/obst_1_med.png',
        'dim': [189, 78]
    }
    TYPE_2 = {
        'path': 'assets/obst_2_med.png',
        'dim': [204, 162]
    }
    TYPE_3 = {
        'path': 'assets/obst_3_med.png',
        'dim': [72, 99]
    }
    def __init__(self, pos: tuple, dim: tuple, imgpath: str, block: bool, type: int, damage: int = 0) -> None:
        super().__init__(pos, dim, imgpath)
        self._block = block
        self._damage = damage
        self.type = type

    def interact(self, char: Character):
        """Modifies the hp of the character.

        Args:
            char (Character): The character to modify.
        """
        if self._block:
            char.set_hp(0)
        else:
            char.update_hp(self._damage * -1)
        