## Implementation approach
We will use Python's built-in modules to implement the game. The `random` module will be used for card dealing. The `os` module will be used to clear the console for a fresh view each round. The `enum` module will be used to define card suits and ranks. The `collections` module will be used to keep track of the player's score. The game logic will be encapsulated in classes and functions for easy maintenance and extension.

## Python package name
```python
"cli_blackjack"
```

## File list
```python
[
    "main.py",
    "game.py",
    "player.py",
    "dealer.py",
    "card.py",
    "deck.py",
    "scoreboard.py"
]
```

## Data structures and interface definitions
```mermaid
classDiagram
    class Main{
        +main()
    }
    class Game{
        +start_game()
        +end_game()
    }
    class Player{
        +hit()
        +stand()
        +int score
    }
    class Dealer{
        +deal()
    }
    class Card{
        +str suit
        +str rank
        +int value
    }
    class Deck{
        +shuffle()
        +draw()
    }
    class Scoreboard{
        +update_score()
        +display_score()
    }
    Main "1" -- "1" Game: starts
    Game "1" -- "1" Player: has
    Game "1" -- "1" Dealer: has
    Game "1" -- "1" Scoreboard: has
    Player "1" -- "*" Card: has
    Dealer "1" -- "*" Card: has
    Dealer "1" -- "1" Deck: uses
```

## Program call flow
```mermaid
sequenceDiagram
    participant M as Main
    participant G as Game
    participant P as Player
    participant D as Dealer
    participant S as Scoreboard
    M->>G: start_game()
    G->>D: deal()
    D-->>P: Card
    D-->>G: Card
    G->>P: hit() or stand()
    P-->>G: Card or None
    G->>D: deal()
    D-->>G: Card
    G->>S: update_score()
    S-->>G: Score
    G->>M: end_game()
```

## Anything UNCLEAR
The requirement is clear to me.