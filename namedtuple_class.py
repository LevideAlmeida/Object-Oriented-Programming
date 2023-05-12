# namedtuples - immutable tuples with names for values
# we use namedtuples to create object classes that are just a
# attributes grouping, like classes without methods, or records of
# databases.
# the namedtuples are immutable like tuples.
# https://docs.python.org/3/library/typing.html#typing.NamedTuple


from typing import NamedTuple

class Card(NamedTuple):
    value: str = 'None'
    suit: str = 'None'

ace_of_spades = Card('A', '♠')
king_of_hearts = Card('K', '♥')
queen_of_clubs = Card('Q', '♣')
jack_of_diamonds = Card('J', '♦')

print(ace_of_spades)
print(ace_of_spades.value, ace_of_spades.suit)

print(king_of_hearts)
print(king_of_hearts.value, king_of_hearts.suit)

print(queen_of_clubs)
for value in queen_of_clubs:
    print(value, end=' ')

print()

print(jack_of_diamonds)
for value in jack_of_diamonds:
    print(value, end=' ')

print()