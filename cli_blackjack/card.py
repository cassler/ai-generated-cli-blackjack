## card.py

from enum import Enum

class Suit(Enum):
    """Enum representing the four suits in a deck of cards."""
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

class Rank(Enum):
    """Enum representing the thirteen ranks in a deck of cards."""
    ACE = ("Ace", 1)
    TWO = ("Two", 2)
    THREE = ("Three", 3)
    FOUR = ("Four", 4)
    FIVE = ("Five", 5)
    SIX = ("Six", 6)
    SEVEN = ("Seven", 7)
    EIGHT = ("Eight", 8)
    NINE = ("Nine", 9)
    TEN = ("Ten", 10)
    JACK = ("Jack", 10)
    QUEEN = ("Queen", 10)
    KING = ("King", 10)

    def __init__(self, rank, value):
        self.rank = rank
        self.value = value

class Card:
    """Class representing a playing card."""
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    @property
    def value(self) -> int:
        """Return the value of the card."""
        return self.rank.value

    def __str__(self) -> str:
        """Return a string representation of the card."""
        return f"{self.rank.rank} of {self.suit.value}"
