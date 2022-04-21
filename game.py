"""Classes for player and game"""

from collections import Counter, defaultdict

from cards import Card


class Player:
    """Player has 2 cards"""

    def __init__(self, card_one: Card, card_two: Card) -> None:
        self.cards: set = {card_one, card_two}
        if len(self.cards) != 2:
            raise ValueError("Player must have 2 unique cards")


class Board:
    """Board has 3 to five cards"""

    def __init__(self,
                 card_one: Card = None,
                 card_two: Card = None,
                 card_three: Card = None,
                 card_four: Card = None,
                 card_five: Card = None) -> None:
        # make sure there are no duplicate cards
        self.cards = set()
        if card_one is not None:
            self.cards.add(card_one)
        if card_two is not None:
            self.cards.add(card_two)
        if card_three is not None:
            self.cards.add(card_three)

        if card_four is not None and len(self.cards) != 3:
            raise ValueError("There must already be three cards")

        if card_four is not None:
            self.cards.add(card_four)
            if len(self.cards) != 4:
                raise ValueError("All cards must be unique")
        # add card 5 if it exists
        if card_five is not None and card_four is None:
            raise ValueError("Card 4 must be filled first")
        if card_five is not None:
            self.cards.add(card_five)
            if len(self.cards) != 5:
                raise ValueError("All cards must be unique")


class Hand:
    """Get a hand of cards"""

    def __init__(self, board: Board, player: Player) -> None:
        board_len = len(board.cards)
        player_len = len(player.cards)

        # union of board and player cards
        self.hand: set[Card] = board.cards.union(player.cards)

        if len(self.hand) != board_len + player_len:
            raise ValueError("All cards must be unique")

    def has_pair(self) -> bool:
        """Return True if there is a pair"""
        return self.has_n_group(2)

    def has_two_pair(self) -> bool:
        """Return True if there are two pairs"""
        card_ranks = [card.rank for card in self.hand]
        counts = Counter(card_ranks)
        return sum(count == 2 for count in counts.values()) >= 2

    def has_trips(self) -> bool:
        """Return True if there are three of a kind"""
        return self.has_n_group(3)

    def has_n_group(self, number: int):
        """
        Determine if a hand has `number` of a kind

        Args:
            arg0 (int): Number of cards to have that rank in a hand

        Returns:
            bool: True if hand has exactly `number` of a kind for any rank
        """
        card_ranks = [card.rank for card in self.hand]
        counts = Counter(card_ranks)
        return any(count == number for count in counts.values())

    def has_straight(self):
        """Return True if there is a straight"""
        card_ranks = [card for sublist in [card.rank.value for card in self.hand]
                      for card in sublist]
        counts = defaultdict(int)
        for card in card_ranks:
            for idx in range(card-4, card+1):
                counts[idx] += 1

        return any(count == 5 for count in counts.values())

    def has_flush(self):
        """Return True if there is a flush"""
        card_suits = [card.suit for card in self.hand]
        counts = Counter(card_suits)
        return any(count == 5 for count in counts.values())

    def has_full_house(self):
        """Return True if there is a full house"""
        return self.has_pair() and self.has_trips()

    def has_quads(self):
        """Return True if there are four of a kind"""
        return self.has_n_group(4)

    def has_straight_flush(self):
        """Return True if there is a straight flush"""
        cards = [card.rank.value[0] +
                 card.suit.value * 20 for card in self.hand]
        # hand case where card.rank.value has two items in it
        cards.extend([card.rank.value[1] +
                      card.suit.value * 20 for card in self.hand
                      if len(card.rank.value) > 1])

        counts = defaultdict(int)
        for card in cards:
            for idx in range(card-4, card+1):
                counts[idx] += 1

        return any(count == 5 for count in counts.values())

    def has_royal_flush(self):
        """Return True if there is a royal flush"""
        cards = [card.rank.value[0] +
                 card.suit.value * 20 for card in self.hand]
        # hand case where card.rank.value has two items in it
        cards.extend([card.rank.value[1] +
                      card.suit.value * 20 for card in self.hand
                      if len(card.rank.value) > 1])

        counts = defaultdict(int)
        for card in cards:
            for idx in range(card-4, card+1):
                counts[idx] += 1

        # indexes of 10's, as these will have 5 counts
        # in a royal flush
        ten_pos = [30, 50, 70, 90]

        return any(count == 5 and num in ten_pos for num, count in counts.items())

    def high_card(self):
        """Return the 5 highest cards in the hand in order"""
        return sorted(self.hand, reverse=True)[:5]
