"""Interactive Snakes and Ladders game with support for 2-4 players.

Refactored from the legacy spaghetti script to a clean, modular OOP structure.
"""

import random
import sys
import time

class SnakesAndLadders:
    def __init__(self):
        self.snake_squares = {16: 4, 33: 20, 48: 24, 62: 56, 78: 69, 94: 16}
        self.ladder_squares = {3: 12, 7: 23, 20: 56, 47: 53, 60: 72, 80: 94}
        self.players = {}
        self.positions = {}
        
    def roll_dice(self) -> int:
        """Roll a single 6-sided die."""
        return random.randint(1, 6)

    def move_player(self, player_name: str, current_pos: int) -> int:
        """Roll the die and move a player, applying snakes and ladders constraints."""
        roll = self.roll_dice()
        new_pos = current_pos + roll
        print(f"\n{player_name} rolled a {roll} and is now on {new_pos}.")
        
        if new_pos in self.snake_squares:
            landed = self.snake_squares[new_pos]
            print(f"Oh no! {player_name} got bitten by a snake! Slid down from {new_pos} to {landed}.")
            new_pos = landed
        elif new_pos in self.ladder_squares:
            landed = self.ladder_squares[new_pos]
            print(f"Awesome! {player_name} climbed a ladder! Advanced from {new_pos} to {landed}.")
            new_pos = landed
            
        return new_pos

    def setup_game(self, num_players: int = 0, player_names: list[str] = None):
        """Setup players and initial positions."""
        if not num_players:
            while True:
                try:
                    num_players = int(input("How many players are in the game? (2-4): "))
                    if 2 <= num_players <= 4:
                        break
                    print("Number of players must be between 2 and 4.")
                except ValueError:
                    print("Please enter a valid integer.")
                    
        self.players = {}
        self.positions = {}
        
        for i in range(num_players):
            if player_names and i < len(player_names):
                name = player_names[i]
            else:
                name = input(f"Enter the name of Player {i+1}: ").strip()
                if not name:
                    name = f"Player_{i+1}"
            self.players[i] = name
            self.positions[i] = 0
            
        print(f"\nWelcome {', '.join(self.players.values())} to Snakes and Ladders!")
        input("Press Enter to start the game...")

    def play(self):
        """Main game loop."""
        if not self.players:
            self.setup_game()
            
        game_over = False
        while not game_over:
            for idx, name in self.players.items():
                input(f"\n{name}'s turn (Press Enter to roll the die)...")
                new_pos = self.move_player(name, self.positions[idx])
                
                # Check for win condition
                if new_pos >= 100:
                    print(f"\nCONGRATULATIONS! {name} WINS THE GAME!")
                    game_over = True
                    break
                else:
                    self.positions[idx] = new_pos
                    print(f"{name} is currently at position {new_pos}.")
                    
        print("\nThank you for playing Snakes and Ladders!")
        time.sleep(1)

if __name__ == "__main__":
    game = SnakesAndLadders()
    game.play()
