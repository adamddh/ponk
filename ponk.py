"""File to figure out odds of winning a hand of poker."""

from cards import Card, Suit, Rank


def main():
    """main"""
    c_one = Card(Suit.CLUBS, Rank.ACE)
    print(c_one)


if __name__ == '__main__':
    main()
