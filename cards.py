"""File to contain cards class"""

from enum import Enum
from itertools import product


class Suit(Enum):
    """Enum for the suits of a card."""
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4


class Rank(Enum):
    """Enum for the ranks of a card."""
    TWO = (2, )
    THREE = (3, )
    FOUR = (4, )
    FIVE = (5, )
    SIX = (6, )
    SEVEN = (7, )
    EIGHT = (8, )
    NINE = (9, )
    TEN = (10, )
    JACK = (11, )
    QUEEN = (12, )
    KING = (13, )
    ACE = (14, 1)


class Card:
    """Card class"""

    def __init__(self, suit: Suit, rank: Rank):
        """Initialize card"""
        self.suit = suit
        # check if rank is in 1-14, else raise ValueError
        if rank.value[0] not in range(1, 15):
            raise ValueError("Rank must be in 1-14")
        self.rank = rank

    def __str__(self):
        """Return string representation of card"""
        return f"{self.rank} of {self.suit}"


# create the set of all 52 cards called CARDS
CARDS = {Card(suit, rank) for suit, rank in product(Suit, Rank)}


def main():
    """Main function"""
    for card in CARDS:
        print(card)


if __name__ == '__main__':
    main()
