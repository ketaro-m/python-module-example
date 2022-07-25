import myModule.utils as utils
import numpy as np

class Module:
    """Summary line.
    """

    def add(self, x, y):
        """sum

        Args:
            x (int): 1st argument
            y (int): 2nd argument

        Returns:
            int: sum result

        Examples:
            >>> print(testfunc(2,5))
            7
        """
        return utils.add(x, y)
