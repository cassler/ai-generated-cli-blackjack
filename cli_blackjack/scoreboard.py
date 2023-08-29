from player import Player

class Scoreboard:
    """Class representing a scoreboard for the game of blackjack."""

    def __init__(self, player: Player, dealer: Player):
        self.player = player
        self.dealer = dealer
        self.player_wins: int = 0
        self.dealer_wins: int = 0
        self.ties: int = 0

    def update_score(self) -> None:
        """Update the score based on the player's and dealer's hands."""
        if self.player.score > 21 or (self.dealer.score <= 21 and self.dealer.score > self.player.score):
            self.dealer_wins += 1
        elif self.dealer.score > 21 or self.player.score > self.dealer.score:
            self.player_wins += 1
        else:
            self.ties += 1

    def display_score(self) -> None:
        """Display the current score."""
        print(f"Player Wins: {self.player_wins}, Dealer Wins: {self.dealer_wins}, Ties: {self.ties}")

    def reset(self) -> None:
        """Reset the scoreboard for a new game."""
        self.player_wins = 0
        self.dealer_wins = 0
        self.ties = 0
