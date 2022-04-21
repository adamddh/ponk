"""Test file for game.py"""

import unittest


from cards import Card, Rank, Suit
from game import Board, Hand, Player


class TestGame(unittest.TestCase):
    """Test class for Game"""

    def test_creation(self):
        """Test creation of Game"""
        # get 2 random cards for one player
        card_one = Card(Suit.CLUBS, Rank.TWO)
        card_two = Card(Suit.DIAMONDS, Rank.THREE)

        # get 3 random cards for the board
        card_three = Card(Suit.HEARTS, Rank.FOUR)
        card_four = Card(Suit.SPADES, Rank.FIVE)
        card_five = Card(Suit.CLUBS, Rank.SIX)

        # create player
        player = Player(card_one, card_two)

        # create board
        board = Board(card_three, card_four, card_five)

        # create hand
        Hand(board, player)

    def test_has_pair(self):
        """Test if hand has a pair"""

        card_one = Card(Suit.CLUBS, Rank.TWO)
        card_two = Card(Suit.DIAMONDS, Rank.TWO)

        card_three = Card(Suit.HEARTS, Rank.FOUR)
        card_four = Card(Suit.SPADES, Rank.FIVE)
        card_five = Card(Suit.CLUBS, Rank.SIX)

        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five)
        hand = Hand(board, player)
        self.assertTrue(hand.has_pair())

        card_one = Card(Suit.CLUBS, Rank.TWO)
        card_two = Card(Suit.DIAMONDS, Rank.SEVEN)

        card_three = Card(Suit.HEARTS, Rank.TWO)
        card_four = Card(Suit.SPADES, Rank.FIVE)
        card_five = Card(Suit.CLUBS, Rank.SIX)

        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five)
        hand = Hand(board, player)
        self.assertTrue(hand.has_pair())

        card_one = Card(Suit.CLUBS, Rank.TWO)
        card_two = Card(Suit.DIAMONDS, Rank.SEVEN)

        card_three = Card(Suit.HEARTS, Rank.TWO)
        card_four = Card(Suit.SPADES, Rank.FIVE)
        card_five = Card(Suit.CLUBS, Rank.FIVE)

        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five)
        hand = Hand(board, player)
        self.assertTrue(hand.has_pair())

        card_one = Card(Suit.CLUBS, Rank.TWO)
        card_two = Card(Suit.DIAMONDS, Rank.SEVEN)

        card_three = Card(Suit.HEARTS, Rank.ACE)
        card_four = Card(Suit.SPADES, Rank.FIVE)
        card_five = Card(Suit.CLUBS, Rank.SIX)

        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five)
        hand = Hand(board, player)
        self.assertFalse(hand.has_pair())

    def test_has_two_pair(self):
        """Test if hand has two pair"""
        card_one = Card(Suit.CLUBS, Rank.TWO)
        card_two = Card(Suit.DIAMONDS, Rank.TWO)

        card_three = Card(Suit.HEARTS, Rank.FOUR)
        card_four = Card(Suit.SPADES, Rank.FIVE)
        card_five = Card(Suit.CLUBS, Rank.SIX)
        card_six = Card(Suit.DIAMONDS, Rank.SIX)
        card_seven = Card(Suit.HEARTS, Rank.SEVEN)

        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_two_pair())

        card_one = Card(Suit.CLUBS, Rank.TWO)
        card_two = Card(Suit.DIAMONDS, Rank.THREE)

        card_three = Card(Suit.HEARTS, Rank.TWO)
        card_four = Card(Suit.SPADES, Rank.THREE)
        card_five = Card(Suit.CLUBS, Rank.SIX)
        card_six = Card(Suit.DIAMONDS, Rank.SIX)
        card_seven = Card(Suit.HEARTS, Rank.SEVEN)

        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_two_pair())

        card_one = Card(Suit.CLUBS, Rank.ACE)
        card_two = Card(Suit.DIAMONDS, Rank.TWO)

        card_three = Card(Suit.HEARTS, Rank.THREE)
        card_four = Card(Suit.SPADES, Rank.THREE)
        card_five = Card(Suit.CLUBS, Rank.FOUR)
        card_six = Card(Suit.DIAMONDS, Rank.FOUR)
        card_seven = Card(Suit.HEARTS, Rank.FIVE)

        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_two_pair())

        card_one = Card(Suit.CLUBS, Rank.ACE)
        card_two = Card(Suit.DIAMONDS, Rank.TWO)

        card_three = Card(Suit.HEARTS, Rank.FOUR)
        card_four = Card(Suit.SPADES, Rank.FIVE)
        card_five = Card(Suit.CLUBS, Rank.SIX)
        card_six = Card(Suit.DIAMONDS, Rank.EIGHT)
        card_seven = Card(Suit.HEARTS, Rank.SEVEN)

        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertFalse(Hand(board, player).has_two_pair())

        card_one = Card(Suit.CLUBS, Rank.ACE)
        card_two = Card(Suit.DIAMONDS, Rank.TWO)

        card_three = Card(Suit.HEARTS, Rank.ACE)
        card_four = Card(Suit.SPADES, Rank.FIVE)
        card_five = Card(Suit.CLUBS, Rank.SIX)
        card_six = Card(Suit.DIAMONDS, Rank.EIGHT)
        card_seven = Card(Suit.HEARTS, Rank.SEVEN)

        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertFalse(Hand(board, player).has_two_pair())

    def test_has_straight(self):
        """test is there is a straight in the hand"""
        card_one = Card(Suit.CLUBS, Rank.TWO)
        card_two = Card(Suit.DIAMONDS, Rank.THREE)
        card_three = Card(Suit.HEARTS, Rank.FOUR)
        card_four = Card(Suit.SPADES, Rank.FIVE)
        card_five = Card(Suit.CLUBS, Rank.SIX)
        card_six = Card(Suit.DIAMONDS, Rank.SEVEN)
        card_seven = Card(Suit.HEARTS, Rank.EIGHT)

        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_straight())

        card_one = Card(Suit.CLUBS, Rank.TWO)
        card_two = Card(Suit.DIAMONDS, Rank.THREE)
        card_three = Card(Suit.HEARTS, Rank.FOUR)
        card_four = Card(Suit.SPADES, Rank.FIVE)
        card_five = Card(Suit.CLUBS, Rank.SIX)
        card_six = Card(Suit.DIAMONDS, Rank.SEVEN)
        card_seven = Card(Suit.HEARTS, Rank.ACE)

        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_straight())

        card_one = Card(Suit.CLUBS, Rank.TWO)
        card_two = Card(Suit.DIAMONDS, Rank.THREE)
        card_three = Card(Suit.HEARTS, Rank.TEN)
        card_four = Card(Suit.SPADES, Rank.JACK)
        card_five = Card(Suit.CLUBS, Rank.QUEEN)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.ACE)

        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_straight())

        card_one = Card(Suit.CLUBS, Rank.TWO)
        card_two = Card(Suit.DIAMONDS, Rank.THREE)
        card_three = Card(Suit.HEARTS, Rank.TEN)
        card_four = Card(Suit.SPADES, Rank.JACK)
        card_five = Card(Suit.CLUBS, Rank.NINE)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.ACE)

        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertFalse(Hand(board, player).has_straight())

    def test_has_flush(self):
        """"Test for flush"""
        card_one = Card(Suit.CLUBS, Rank.TWO)
        card_two = Card(Suit.CLUBS, Rank.THREE)
        card_three = Card(Suit.CLUBS, Rank.TEN)
        card_four = Card(Suit.CLUBS, Rank.JACK)
        card_five = Card(Suit.CLUBS, Rank.NINE)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.ACE)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_flush())

        card_one = Card(Suit.CLUBS, Rank.TWO)
        card_two = Card(Suit.DIAMONDS, Rank.THREE)
        card_three = Card(Suit.HEARTS, Rank.TEN)
        card_four = Card(Suit.SPADES, Rank.JACK)
        card_five = Card(Suit.CLUBS, Rank.NINE)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.ACE)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertFalse(Hand(board, player).has_flush())

    def test_has_full_house(self):
        """Test for full house"""
        card_one = Card(Suit.CLUBS, Rank.TWO)
        card_two = Card(Suit.DIAMONDS, Rank.TWO)
        card_three = Card(Suit.HEARTS, Rank.TEN)
        card_four = Card(Suit.SPADES, Rank.TEN)
        card_five = Card(Suit.CLUBS, Rank.TEN)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.ACE)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_full_house())

        card_one = Card(Suit.CLUBS, Rank.TWO)
        card_two = Card(Suit.DIAMONDS, Rank.TEN)
        card_three = Card(Suit.HEARTS, Rank.TEN)
        card_four = Card(Suit.SPADES, Rank.TWO)
        card_five = Card(Suit.CLUBS, Rank.TEN)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.ACE)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_full_house())

        card_one = Card(Suit.CLUBS, Rank.THREE)
        card_two = Card(Suit.DIAMONDS, Rank.FOUR)
        card_three = Card(Suit.HEARTS, Rank.TEN)
        card_four = Card(Suit.SPADES, Rank.TEN)
        card_five = Card(Suit.CLUBS, Rank.TEN)
        card_six = Card(Suit.DIAMONDS, Rank.FIVE)
        card_seven = Card(Suit.HEARTS, Rank.FIVE)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_full_house())

        card_one = Card(Suit.CLUBS, Rank.THREE)
        card_two = Card(Suit.DIAMONDS, Rank.FOUR)
        card_three = Card(Suit.HEARTS, Rank.TEN)
        card_four = Card(Suit.SPADES, Rank.TEN)
        card_five = Card(Suit.CLUBS, Rank.TEN)
        card_six = Card(Suit.DIAMONDS, Rank.SIX)
        card_seven = Card(Suit.HEARTS, Rank.FIVE)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertFalse(Hand(board, player).has_full_house())

        card_one = Card(Suit.CLUBS, Rank.THREE)
        card_two = Card(Suit.DIAMONDS, Rank.FOUR)
        card_three = Card(Suit.HEARTS, Rank.TEN)
        card_four = Card(Suit.SPADES, Rank.TWO)
        card_five = Card(Suit.CLUBS, Rank.TEN)
        card_six = Card(Suit.DIAMONDS, Rank.SIX)
        card_seven = Card(Suit.HEARTS, Rank.FIVE)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertFalse(Hand(board, player).has_full_house())

        card_one = Card(Suit.CLUBS, Rank.ACE)
        card_two = Card(Suit.DIAMONDS, Rank.FOUR)
        card_three = Card(Suit.HEARTS, Rank.SEVEN)
        card_four = Card(Suit.SPADES, Rank.ACE)
        card_five = Card(Suit.CLUBS, Rank.TEN)
        card_six = Card(Suit.DIAMONDS, Rank.ACE)
        card_seven = Card(Suit.HEARTS, Rank.FIVE)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertFalse(Hand(board, player).has_full_house())

    def test_has_quads(self):
        """test for quads"""
        card_one = Card(Suit.CLUBS, Rank.TWO)
        card_two = Card(Suit.DIAMONDS, Rank.TWO)
        card_three = Card(Suit.HEARTS, Rank.TWO)
        card_four = Card(Suit.SPADES, Rank.TWO)
        card_five = Card(Suit.CLUBS, Rank.TEN)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.ACE)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_quads())

        card_one = Card(Suit.CLUBS, Rank.ACE)
        card_two = Card(Suit.DIAMONDS, Rank.ACE)
        card_three = Card(Suit.HEARTS, Rank.ACE)
        card_four = Card(Suit.SPADES, Rank.ACE)
        card_five = Card(Suit.CLUBS, Rank.TEN)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.SEVEN)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_quads())

        card_one = Card(Suit.CLUBS, Rank.SIX)
        card_two = Card(Suit.DIAMONDS, Rank.ACE)
        card_three = Card(Suit.HEARTS, Rank.ACE)
        card_four = Card(Suit.SPADES, Rank.ACE)
        card_five = Card(Suit.CLUBS, Rank.TEN)
        card_six = Card(Suit.DIAMONDS, Rank.ACE)
        card_seven = Card(Suit.HEARTS, Rank.SEVEN)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_quads())

        card_one = Card(Suit.CLUBS, Rank.ACE)
        card_two = Card(Suit.DIAMONDS, Rank.ACE)
        card_three = Card(Suit.HEARTS, Rank.FOUR)
        card_four = Card(Suit.SPADES, Rank.ACE)
        card_five = Card(Suit.CLUBS, Rank.TEN)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.SEVEN)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertFalse(Hand(board, player).has_quads())

    def test_st_flush(self):
        """test for straight flush"""
        card_one = Card(Suit.CLUBS, Rank.ACE)
        card_two = Card(Suit.CLUBS, Rank.TWO)
        card_three = Card(Suit.CLUBS, Rank.FOUR)
        card_four = Card(Suit.CLUBS, Rank.THREE)
        card_five = Card(Suit.CLUBS, Rank.FIVE)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.SEVEN)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_straight_flush())

        card_one = Card(Suit.CLUBS, Rank.ACE)
        card_two = Card(Suit.CLUBS, Rank.KING)
        card_three = Card(Suit.CLUBS, Rank.QUEEN)
        card_four = Card(Suit.CLUBS, Rank.JACK)
        card_five = Card(Suit.CLUBS, Rank.TEN)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.SEVEN)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_straight_flush())

        card_one = Card(Suit.CLUBS, Rank.NINE)
        card_two = Card(Suit.CLUBS, Rank.KING)
        card_three = Card(Suit.CLUBS, Rank.QUEEN)
        card_four = Card(Suit.CLUBS, Rank.JACK)
        card_five = Card(Suit.CLUBS, Rank.TEN)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.SEVEN)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_straight_flush())

        card_one = Card(Suit.CLUBS, Rank.ACE)
        card_two = Card(Suit.SPADES, Rank.KING)
        card_three = Card(Suit.CLUBS, Rank.QUEEN)
        card_four = Card(Suit.CLUBS, Rank.JACK)
        card_five = Card(Suit.CLUBS, Rank.TEN)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.SEVEN)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertFalse(Hand(board, player).has_straight_flush())

    def test_royal_flush(self):
        """test for royal flush"""
        card_one = Card(Suit.CLUBS, Rank.ACE)
        card_two = Card(Suit.CLUBS, Rank.TWO)
        card_three = Card(Suit.CLUBS, Rank.FOUR)
        card_four = Card(Suit.CLUBS, Rank.THREE)
        card_five = Card(Suit.CLUBS, Rank.FIVE)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.SEVEN)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertFalse(Hand(board, player).has_royal_flush())

        card_one = Card(Suit.CLUBS, Rank.ACE)
        card_two = Card(Suit.CLUBS, Rank.KING)
        card_three = Card(Suit.CLUBS, Rank.QUEEN)
        card_four = Card(Suit.CLUBS, Rank.JACK)
        card_five = Card(Suit.CLUBS, Rank.TEN)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.SEVEN)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertTrue(Hand(board, player).has_royal_flush())

        card_one = Card(Suit.CLUBS, Rank.NINE)
        card_two = Card(Suit.CLUBS, Rank.KING)
        card_three = Card(Suit.CLUBS, Rank.QUEEN)
        card_four = Card(Suit.CLUBS, Rank.JACK)
        card_five = Card(Suit.CLUBS, Rank.TEN)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.SEVEN)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertFalse(Hand(board, player).has_royal_flush())

        card_one = Card(Suit.CLUBS, Rank.ACE)
        card_two = Card(Suit.SPADES, Rank.KING)
        card_three = Card(Suit.CLUBS, Rank.QUEEN)
        card_four = Card(Suit.CLUBS, Rank.JACK)
        card_five = Card(Suit.CLUBS, Rank.TEN)
        card_six = Card(Suit.DIAMONDS, Rank.KING)
        card_seven = Card(Suit.HEARTS, Rank.SEVEN)
        player = Player(card_one, card_two)
        board = Board(card_three, card_four, card_five, card_six, card_seven)
        self.assertFalse(Hand(board, player).has_royal_flush())


if __name__ == '__main__':
    unittest.main()
