from __future__ import annotations

import re
from typing import Dict, List


with open("solutions/day-7/input.txt") as f:
    input_data = f.read().splitlines()


def get_rules(data: List[str]) -> Dict[str, Dict[str, int]]:
    """Returns a dict of what bags go in each bag."""
    contains_split = re.compile(r"bags?.?$")
    bags = {}

    for line in data:
        color, contains = line.split(" bags contain ")
        if not contains == "no other bags.":
            contains = [contains_split.sub("", item).strip() for item in contains.split(",")]
            sub_bags = dict(reversed(a.split(" ", 1)) for a in contains)
        else:  # If there aren't any bags within the bag
            sub_bags = {}
        bags.update({color: sub_bags})

    return bags


class Bag:
    """Class for bags and methods to get data about them."""
    rules = get_rules(input_data)

    def __init__(self, name: str, amount: int = 1):
        self.name = name
        self.amount = int(amount)
        self.bags = self._sub_bags()

    def _sub_bags(self) -> List[Bag]:
        """Get the bags that fit inside the parent bag."""
        return [Bag(name, amount) for name, amount in self.rules[self.name].items()]

    def contains_color(self, target: str = "shiny gold") -> bool:
        """Checks if the bag contains a certain color."""
        for bag in self.bags:
            if bag.name == target or bag.contains_color(target):
                return True

        return False

    def bags_inside(self):
        """Returns the number of bags inside a certain bag."""
        if self.bags:
            return (sum(bag.bags_inside() for bag in self.bags)+1) * self.amount  # +1 includes the sub-bags themselves
        else:
            return self.amount


def shiny_gold_bags() -> int:
    """Get the number of shiny gold bags in a bag."""
    return sum(1 for bag in Bag.rules if Bag(bag).contains_color())


def bags_in_shiny_gold():
    """Get the number of bags in a shiny gold bag."""
    return Bag("shiny gold").bags_inside() - 1  # -1 since we don't count the shiny bag itself


if __name__ == "__main__":
    print(shiny_gold_bags())  # Star 1
    print(bags_in_shiny_gold())  # Star 2
