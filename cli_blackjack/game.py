from typing import Optional
from player import Player
from dealer import Dealer
from deck import Deck
from scoreboard import Scoreboard
from card import Card

class Game:
    """Class representing a game of blackjack."""

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer(self.deck)
        self.scoreboard = Scoreboard(self.player, self.dealer)
        self.is_game_over: bool = False

    def start_game(self) -> None:
        """Start a new game of blackjack."""
        self.is_game_over = False
        self.player.reset()
        self.dealer.reset()
        self.scoreboard.reset()
        self.deal_initial_cards()

    def deal_initial_cards(self) -> None:
        """Deal the initial cards to the player and dealer."""
        for _ in range(2):
            self.player.hit(self.dealer.deal())
            self.dealer.hit(self.dealer.deal())

    def player_turn(self) -> None:
        """Play the player's turn."""
        while not self.is_game_over:
            print(self.player)
            action = self.get_player_action()
            if action == 'h':
                self.player.hit(self.dealer.deal())
                if self.player.score > 21:
                    self.is_game_over = True
            else:
                break

    def dealer_turn(self) -> None:
        """Play the dealer's turn."""
        if not self.is_game_over:
            self.dealer.play()
            print(self.dealer)
            if self.dealer.score > 21:
                self.is_game_over = True

    def get_player_action(self) -> str:
        """Get the player's action (hit or stand)."""
        while True:
            action = input("Do you want to (h)it or (s)tand? ").lower()
            if action in ['h', 's']:
                return action
            else:
                print("Invalid input. Please enter 'h' to hit or 's' to stand.")

    def end_game(self) -> None:
        """End the current game and update the scoreboard."""
        self.scoreboard.update_score()
        self.scoreboard.display_score()
        self.is_game_over = True

    def play(self) -> None:
        """Play a game of blackjack."""
        self.start_game()
        while not self.is_game_over:
            self.player_turn()
            self.dealer_turn()
            self.end_game()
            if input("Do you want to play again? (y/n) ").lower() != 'y':
                break
            self.start_game()
