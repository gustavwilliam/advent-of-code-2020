from typing import List, Set


with open(f"solutions/day-6/input.txt") as f:
    input_data = f.read()


def parse_customs(data: str) -> List[List[str]]:
    """Returns a list of lists of strings, representing the answers of all members of all groups."""
    return [text.split("\n") for text in data.split("\n\n")]


def unique_answers(group: List[str]) -> Set[str]:
    """Finds the unique answers in a given group, that anyone gave."""
    answers = set() 
    for member in group:
        answers.update(answer for answer in member)

    return answers


def unanimous_answers(group: List[str]) -> Set[str]:
    """Finds the unique answers in a given group, that anyone gave."""
    answers = set.intersection(*(set(item) for item in group))

    return answers


def total_answers(data: str, challenge: int) -> int:
    """Gets the total amount of answers in the given sets of answers."""
    customs = parse_customs(data)

    if challenge == 1:
        groups = [unique_answers(a) for a in customs]
    elif challenge == 2:
        groups = [unanimous_answers(a) for a in customs]

    return sum(len(group) for group in groups)


if __name__ == "__main__":
    print(total_answers(input_data, 1))  # Challenge 1
    print(total_answers(input_data, 2))  # Challenge 2
