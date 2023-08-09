from model.element import Element
from character import Character

class Obstacle(Element):
    """Represents an obstacle that hinders the player.

    Args:
        Element (Element): The parent class.
    """
    TYPE_1 = {
        # will eventually have a few of these with different image paths, types, damage, etc
    }

    def __init__(self, pos: tuple, dim: tuple, imgpath: str, block: bool, damage: int = 0) -> None:
        super().__init__(pos, dim, imgpath)
        self._block = block
        self._damage = damage

        def interact(self, char: Character):
            """Modifies the hp of the character.

            Args:
                char (Character): The character to modify.
            """
            if self._block:
                char.set_hp(0)
            else:
                char.update_hp(self._damage * -1)
        