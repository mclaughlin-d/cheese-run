from model.element import Element

class Obstacle(Element):
    """_summary_

    Args:
        Element (_type_): _description_
    """
    def __init__(self, pos: tuple, dim: tuple) -> None:
        super().__init__(pos, dim)

        