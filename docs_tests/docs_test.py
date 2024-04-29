"""docs_test.py file level string
"""

import numpy as np


class NumpySummer(object):
    """Numpy Summer that inits and always outputs the sum of 2 init numbers"""

    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def sum(self) -> np.ndarray:
        """Sum of init numbers

        Returns
        -------
        np.ndarray
            array of sum
        """
        return np.sum([self.a, self.b], dtype=int)

    def sum_others(self, a: int, b: int) -> int:
        """Sum two numbers

        Parameters
        ----------
        a : int
            First number to sum
        b : int
            Second number to sum number to sum

        Returns
        -------
        int
            Sum of numbers
        """
        return a + b
