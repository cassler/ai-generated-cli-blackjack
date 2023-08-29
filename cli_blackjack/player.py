from typing import List
from card import Card

class Player:
    """Class representing a player in the game of blackjack."""

    def __init__(self):
        self.hand: List[Card] = []
        self.score: int = 0

    def hit(self, card: Card) -> None:
        """Add a card to the player's hand and update the score."""
        self.hand.append(card)
        self.score += card.value

    def stand(self) -> None:
        """Player chooses to not take any more cards."""
        pass

    def reset(self) -> None:
        """Reset the player's hand and score for a new game."""
        self.hand = []
        self.score = 0

    def __str__(self) -> str:
        """Return a string representation of the player's hand and score."""
        hand_str = ', '.join(str(card) for card in self.hand)
        return f"Hand: {hand_str}, Score: {self.score}"
