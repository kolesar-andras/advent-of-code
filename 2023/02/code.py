import sys
import re

class Set:
    def __init__(self, str = ""):
        for pair in re.split(', *', str):
            if pair == "": continue
            match = re.fullmatch(f"([0-9]+) +({'|'.join(self.keys())})", pair)
            key = match.group(2) # colour
            value = int(match.group(1)) # number of items
            setattr(self, key, value)

    @staticmethod
    def keys() -> list[str]:
        return ['red', 'green', 'blue']

    def value(self, key: str) -> int:
        if (hasattr(self, key)):
            return getattr(self, key)
        return 0

    def max(self, other):
        result = Set()
        for key in self.keys():
            setattr(result, key, max([self.value(key), other.value(key)]))
        return result

    def power (self) -> int:
        result = 1
        for key in self.keys():
            result *= self.value(key)
        return result

    def __gt__(self, other) -> bool:
        for key in self.keys():
            if self.value(key) > other.value(key):
                return True
        return False

    def __eq__(self, other) -> bool:
        for key in self.keys():
            if self.value(key) != other.value(key):
                return False
        return True

    def __str__(self) -> str:
        colours = []
        for key in self.keys():
            if (hasattr(self, key)):
                colours.append(f"{getattr(self, key)} {key}")
        return ', '.join(colours)

class Game:
    id: int
    sets: list[Set]

    def __init__(self, line):
        match = re.fullmatch("Game ([0-9]+): *(.+)", line.strip())
        self.id = int(match.group(1))
        self.sets = []
        for str in re.split('; *', match.group(2)):
            set = Set(str)
            self.sets.append(set)

    def is_possible(self, constraint: Set) -> bool:
        for set in self.sets:
            if set > constraint:
                return False
        return True

    def min(self) -> Set:
        min = Set()
        for set in self.sets:
            min = min.max(set)
        return min

    def power(self) -> int:
        return self.min().power()

constraint = Set('12 red, 13 green, 14 blue')

if __name__ == "__main__":
    total_id = 0
    total_power = 0
    for line in sys.stdin:
        game = Game(line)
        if game.is_possible(constraint):
            total_id += game.id
        total_power += game.power()
    print(total_id)
    print(total_power)
