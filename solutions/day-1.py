import math
import itertools
from typing import List


def get_addents(data: List[int], answer: int, amount: int) -> List[int]:
    """
    Returns the addents from the data list whose sum is the provided answer.
    
    Finds the solution that has the provided 'amount' of addents.
    """
    for addents in itertools.combinations(data, amount):
        if sum(addents) == answer:
            return addents
                

answer = math.prod(get_addents(data, 2020, 3))
print(answer)
