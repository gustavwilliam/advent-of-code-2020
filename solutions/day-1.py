import math
import itertools
from typing import List


def get_addents(data: List[int], answer: int, amount: int) -> List[int]:
    """
    Returns the addents from the data list whose sum is the provided answer.
    
    'answer' is the target sum.
    'amount' indicates the number of addents the answer has.
    """
    for addents in itertools.combinations(data, amount):
        if sum(addents) == answer:
            return addents
                

answer = math.prod(get_addents(data, 2020, 3))
print(answer)
