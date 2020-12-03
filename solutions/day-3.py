from typing import List


def is_tree(pattern: List[str], row: int, col: int) -> bool:
    """Checks if the input pattern has a tree at the input coordinates."""
    width = len(pattern[0])    
    pat_col = col-col//(width-1)*(width-1)  # Turn width into an index

    if pattern[row][pat_col] == "#":
        return True
    return False
    

def trees_in_route(pattern: List[str], right: int, down: int) -> int:
    """Counts the number of trees in the given path."""
    trees = 0
    
    for i, row in enumerate(range(0, len(pattern), down)):
        if is_tree(pattern, row, i*right):
            trees += 1
            
    return trees
