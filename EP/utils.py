from typing import List, Tuple

import numpy as np


def factorizer(coffs_of_dividend: List, coffs_of_divisor: List) -> (Tuple, bool):
    rem_is_zero = False
    dividend = np.array(coffs_of_dividend)
    divisor = np.array(coffs_of_divisor)
    quotient, remainder = np.polydiv(dividend, divisor)
    if len(remainder) == 1 and remainder[0] == 0.0:
        rem_is_zero = True
    return (quotient, remainder), rem_is_zero

