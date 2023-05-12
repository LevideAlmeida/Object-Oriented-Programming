# namedtuples - immutable tuples with names for values
# we use namedtuples to create object classes that are just a
# attributes grouping, like classes without methods, or records of
# databases.
# the namedtuples are immutable like tuples.
# https://docs.python.org/3/library/collections.html#collections.namedtuple

from collections import namedtuple

card = namedtuple('card', ['value', 'suit'], defaults=['None', 'None'])
ace_of_spades = card('A', '♠')
king_of_hearts = card('K', '♥')
queen_of_clubs = card('Q', '♣')
jack_of_diamonds = card('J', '♦')

print(ace_of_spades)
print(ace_of_spades.value)
print(ace_of_spades.suit, end='\n\n')

print(king_of_hearts)
print(king_of_hearts.value)
print(king_of_hearts.suit, end='\n\n')


print(queen_of_clubs)
for value in queen_of_clubs:
    print(value)

print()

print(jack_of_diamonds)
for value in jack_of_diamonds:
    print(value)

print()

the_card = card()

print(the_card)