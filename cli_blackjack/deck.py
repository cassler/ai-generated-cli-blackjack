from typing import List
from random import shuffle
from card import Card, Suit, Rank

class Deck:
    """Class representing a deck of cards."""

    def __init__(self):
        self.cards: List[Card] = [Card(suit, rank) for suit in Suit for rank in Rank]
        self.shuffle()

    def shuffle(self) -> None:
        """Shuffle the deck of cards."""
        shuffle(self.cards)

    def draw(self) -> Card:
        """Draw a card from the deck."""
        return self.cards.pop()

    def reset(self) -> None:
        """Reset the deck for a new game."""
        self.__init__()
