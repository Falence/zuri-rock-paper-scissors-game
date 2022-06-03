import random


class Game:
    """A Rock-Paper-Scissors game."""

    def __init__(self):
        self.moves = ['R', 'P', 'S']
        self.player_name = ''
        self.player_move = ''
        self.cpu_move = ''

    def say_welcome(self):
        """Prints the game's welcome message and instructions."""
        print("---------------------------------------------")
        print("|  WELCOME TO THE ROCK-PAPER-SCISSORS GAME  |")
        print("---------------------------------------------")
        print("INSTRUCTIONS:")
        print("- How to win:")
        print("\t> Rock (R) beats Scissors (S) ")
        print("\t> Paper (P) beats Rock (R) ")
        print("\t> Scissors (S) beats Paper (P) ")
        print("- How to play:")
        print("\t> You'll be playing against the CPU.")
        print("\t> Moves: use 'R' for Rock, 'P' for Paper & 'S' for Scissors.")
        print("======================================================================")

    def get_player_name(self):
        """Gets player's name."""
        try:
            name = input(
                "Player name (press enter to use 'PLAYER 1'): ").upper().split()[0]
        except IndexError:
            return 'PLAYER 1'
        else:
            return name

    def get_player_move(self):
        """Gets user's move - R or P or S."""
        return input(f'{self.player_name}, enter your move (R or P or S): ').upper()

    def get_cpu_move(self):
        """Generates CPU move - R or P or S."""
        return random.choice(self.moves)

    def display_moves(self):
        """Displays the moves of both the player and CPU on screen."""
        print("-------------------------------------------------")
        print(f"{self.player_name} [{self.player_move}] : CPU [{self.cpu_move}]")

    def display_winner(self, winner):
        """Displays the winner."""
        if winner == 'CPU':
            print(f"{winner} WINS!")
            print("GAME OVER!!!")
        else:
            print(f"{winner}, YOU WIN!")
            print("CONGRATS!")
        print("-------------------------------------------------")

    def play(self):
        """Starts ROCK-PAPER-SCISSORS game"""

        self.say_welcome()
        self.player_name = self.get_player_name()

        while True:
            self.player_move = self.get_player_move()
            self.cpu_move = self.get_cpu_move()

            if self.player_move not in self.moves:
                print("-------------------------------------------------")
                print("Invalid input! --> R (ROCK), P (PAPER) & S (SCISSORS)")
                continue

            elif self.player_move == self.cpu_move:
                self.display_moves()
                print("IT'S A DRAW!!!")
                print("-------------------------------------------------")
                print("\t\tRESTARTING GAME")
                print("-------------------------------------------------")

            elif self.player_move == 'R':
                if self.cpu_move == 'S':
                    self.display_moves()
                    self.display_winner(self.player_name)
                    break
                elif self.cpu_move == 'P':
                    self.display_moves()
                    self.display_winner('CPU')
                    break

            elif self.player_move == 'P':
                if self.cpu_move == 'R':
                    self.display_moves()
                    self.display_winner(self.player_name)
                    break
                elif self.cpu_move == 'S':
                    self.display_moves()
                    self.display_winner('CPU')
                    break

            elif self.player_move == 'S':
                if self.cpu_move == 'P':
                    self.display_moves()
                    self.display_winner(self.player_name)
                    break
                elif self.cpu_move == 'R':
                    self.display_moves()
                    self.display_winner('CPU')
                    break


# Create and play game
new_game = Game()
new_game.play()
