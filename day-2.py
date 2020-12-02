def parse_data(data: str) -> list:
    """
    Takes a data input string, splits and returns the components.

    Example:
    Input: "1-3 a: abcde"
    Output: [1, 3, "a", "abcde"}
    """
    reqs, text = [i.strip() for i in data.split(":")]
    req_occurances, req_letter = reqs.split()
    req_low, req_high = req_occurances.split("-")

    return [
        int(req_low),
        int(req_high),
        req_letter,
        text,
    ]


def check_requirements(requirements: list, challenge: int) -> bool:
    """Checks if the passed requirements are met for the specified challenge or not."""
    low, high, letter, text = requirements
    occurances = {i for i, char in enumerate(text) if char == letter}
    
    if challenge == 1:
        if low <= len(occurances) <= high:
            return True

    if challenge == 2:
        matches = {low-1, high-1} & occurances  # Subtract 1, since they start counting at 1 instead of 0
        if len(matches) == 1:
            return True
    
    return False


def is_valid(data: str, challenge: int) -> bool:
    """Checks if the input string is a valid password, for the provided challenge."""
    return check_requirements(parse_data(data), challenge)
