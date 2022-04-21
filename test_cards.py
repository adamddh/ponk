"""Unittest class for creating cards"""

import unittest

from cards import Card, Rank, Suit


class TestCards(unittest.TestCase):
    """Test class for Cards"""

    def test_creation(self):
        """Test creation of all 52 cards"""
        self.assertIsInstance(Card(Suit.CLUBS, Rank.ACE), Card)
        self.assertIsInstance(Card(Suit.CLUBS, Rank.TWO), Card)
        self.assertIsInstance(Card(Suit.CLUBS, Rank.THREE), Card)
        self.assertIsInstance(Card(Suit.CLUBS, Rank.FOUR), Card)
        self.assertIsInstance(Card(Suit.CLUBS, Rank.FIVE), Card)
        self.assertIsInstance(Card(Suit.CLUBS, Rank.SIX), Card)
        self.assertIsInstance(Card(Suit.CLUBS, Rank.SEVEN), Card)
        self.assertIsInstance(Card(Suit.CLUBS, Rank.EIGHT), Card)
        self.assertIsInstance(Card(Suit.CLUBS, Rank.NINE), Card)
        self.assertIsInstance(Card(Suit.CLUBS, Rank.TEN), Card)
        self.assertIsInstance(Card(Suit.CLUBS, Rank.JACK), Card)
        self.assertIsInstance(Card(Suit.CLUBS, Rank.QUEEN), Card)
        self.assertIsInstance(Card(Suit.CLUBS, Rank.KING), Card)

        self.assertIsInstance(Card(Suit.DIAMONDS, Rank.ACE), Card)
        self.assertIsInstance(Card(Suit.DIAMONDS, Rank.TWO), Card)
        self.assertIsInstance(Card(Suit.DIAMONDS, Rank.THREE), Card)
        self.assertIsInstance(Card(Suit.DIAMONDS, Rank.FOUR), Card)
        self.assertIsInstance(Card(Suit.DIAMONDS, Rank.FIVE), Card)
        self.assertIsInstance(Card(Suit.DIAMONDS, Rank.SIX), Card)
        self.assertIsInstance(Card(Suit.DIAMONDS, Rank.SEVEN), Card)
        self.assertIsInstance(Card(Suit.DIAMONDS, Rank.EIGHT), Card)
        self.assertIsInstance(Card(Suit.DIAMONDS, Rank.NINE), Card)
        self.assertIsInstance(Card(Suit.DIAMONDS, Rank.TEN), Card)
        self.assertIsInstance(Card(Suit.DIAMONDS, Rank.JACK), Card)
        self.assertIsInstance(Card(Suit.DIAMONDS, Rank.QUEEN), Card)
        self.assertIsInstance(Card(Suit.DIAMONDS, Rank.KING), Card)

        self.assertIsInstance(Card(Suit.SPADES, Rank.ACE), Card)
        self.assertIsInstance(Card(Suit.SPADES, Rank.TWO), Card)
        self.assertIsInstance(Card(Suit.SPADES, Rank.THREE), Card)
        self.assertIsInstance(Card(Suit.SPADES, Rank.FOUR), Card)
        self.assertIsInstance(Card(Suit.SPADES, Rank.FIVE), Card)
        self.assertIsInstance(Card(Suit.SPADES, Rank.SIX), Card)
        self.assertIsInstance(Card(Suit.SPADES, Rank.SEVEN), Card)
        self.assertIsInstance(Card(Suit.SPADES, Rank.EIGHT), Card)
        self.assertIsInstance(Card(Suit.SPADES, Rank.NINE), Card)
        self.assertIsInstance(Card(Suit.SPADES, Rank.TEN), Card)
        self.assertIsInstance(Card(Suit.SPADES, Rank.JACK), Card)
        self.assertIsInstance(Card(Suit.SPADES, Rank.QUEEN), Card)
        self.assertIsInstance(Card(Suit.SPADES, Rank.KING), Card)

        self.assertIsInstance(Card(Suit.HEARTS, Rank.ACE), Card)
        self.assertIsInstance(Card(Suit.HEARTS, Rank.TWO), Card)
        self.assertIsInstance(Card(Suit.HEARTS, Rank.THREE), Card)
        self.assertIsInstance(Card(Suit.HEARTS, Rank.FOUR), Card)
        self.assertIsInstance(Card(Suit.HEARTS, Rank.FIVE), Card)
        self.assertIsInstance(Card(Suit.HEARTS, Rank.SIX), Card)
        self.assertIsInstance(Card(Suit.HEARTS, Rank.SEVEN), Card)
        self.assertIsInstance(Card(Suit.HEARTS, Rank.EIGHT), Card)
        self.assertIsInstance(Card(Suit.HEARTS, Rank.NINE), Card)
        self.assertIsInstance(Card(Suit.HEARTS, Rank.TEN), Card)
        self.assertIsInstance(Card(Suit.HEARTS, Rank.JACK), Card)
        self.assertIsInstance(Card(Suit.HEARTS, Rank.QUEEN), Card)
        self.assertIsInstance(Card(Suit.HEARTS, Rank.KING), Card)
