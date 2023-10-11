#simple function to be tested
''' General utilities
'''

from typing import Union

import numpy as np


def square(input_value: Union[int, float, np.ndarray]) -> Union[float, np.ndarray]:
    '''This function takes as input an int or a float and gives as output
     its square as a float. Alternatively, it takes as input a np.ndarray and
     gives as output a np.ndarray with the elements squared.

     Arguments:
     ----------
     input_value: number
         The input number to be squared


     Return:
     ------
         The square of input_value: float

     '''

    return input_value**2
