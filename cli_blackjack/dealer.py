from typing import List
from card import Card
from deck import Deck
from player import Player

class Dealer(Player):
    """Class representing the dealer in the game of blackjack."""

    def __init__(self, deck: Deck):
        super().__init__()
        self.deck = deck

    def deal(self) -> Card:
        """Deal a card from the deck."""
        return self.deck.draw()

    def play(self) -> None:
        """Play the dealer's turn. Dealer hits until score is 17 or higher."""
        while self.score < 17:
            self.hit(self.deal())

    def reset(self) -> None:
        """Reset the dealer's hand, score, and deck for a new game."""
        super().reset()
        self.deck.reset()
