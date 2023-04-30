# Enum -> Enumerations

# Enumerations in programming, are used in situations where we have
# a determined number of things to choose

# Enums have members and their value are constants


import enum

# directions = enum.Enum('Directions', ['RIGHT', 'LEFT'])

class Directions(enum.Enum):
    RIGHT = 1
    LEFT = 2
    UP = enum.auto()
    DOWN = enum.auto()

print(Directions(1), Directions['RIGHT'], Directions.RIGHT)


def move(direction):
    if direction not in Directions:
        raise ValueError('Invalid direction')

    print(f'move to {direction} ({direction.value})')


move(Directions.RIGHT)
move(Directions.LEFT)
move(Directions.UP)
move(Directions.DOWN)
