from abc import ABC, abstractmethod

class Element(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """
    def __init__(self, pos: tuple, dim: tuple) -> None:
        self._pos = pos
        self._dim = dim

        def was_hit(self):
            pass

        @abstractmethod
        def interact(self):
            pass
