from typing import Tuple, List

with open(f"solutions/day-5/input.txt") as f:
    input_data = f.read().splitlines() 


def _index(bsp_string: str) -> int:
    """Finds the position of a seat (row or col) given the bsp string representation."""
    high = 2 ** len(bsp_string) - 1  # - 1 to shift from length to index
    low = 0

    for instruction in bsp_string:
        if instruction in ("B", "R"):
            low += (high-low+1)/2
        elif instruction in ("F", "L"):
            high -= (high-low+1)/2

    return int(high)


def seat_coordinates(seat: str) -> Tuple[int]:
    """Gets the coordinates representing the input string, using bsp."""
    row_bsp = seat[:7]  # First 7 characters represent the row
    col_bsp = seat[7:]  # Last 3 characters represent the col

    return (_index(row_bsp), _index(col_bsp))


def seat_id(seat: str) -> int:
    """Get the seat id from the bsp seat string."""
    coordinates = seat_coordinates(seat)
    return coordinates[0]*8 + coordinates[1]


def highest_id(data: List[str]) -> int:
    """Finds the highest number id, given the input data."""
    return max(seat_id(seat) for seat in input_data)


def your_id(data: List[str]) -> int:
    """Finds the id that is missing from the continous series of ids."""
    ids = sorted([seat_id(seat) for seat in data])
    start_diff = ids[0]  # The difference between index and value of id

    for i, id_ in enumerate(ids):
        if id_ != i + start_diff:  # When the difference has changed
            return id_ - 1  # The change is noticed in the number after the target id


if __name__ == "__main__":
    print(highest_id(input_data))  # First star
    print(your_id(input_data))  # Second star
