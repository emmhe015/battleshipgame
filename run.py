import random

def create_board(size):
    """
    Creates a game board of given size.
    
    Args:
    size (int): The size of the grid.
    
    Returns:
    list: A 2D list representing the game board.
    """
    return [["O"] * size for _ in range(size)]

def print_board(board):
    """
    Prints the game board.
    
    Args:
    board (list): The game board to print.
    """
    for row in board:
        print(" ".join(row))

def place_ships(board, size, num_ships):
    """
    Places a specified number of ships randomly on the board.
    
    Args:
    board (list): The game board to place ships on.
    size (int): The size of the grid.
    num_ships (int): The number of ships to place.
    """
    ships = 0
    while ships < num_ships:
        ship_size = random.randint(1, size // 2)
        direction = random.choice(['H', 'V'])
        if direction == 'H':
            ship_row = random.randint(0, size-1)
            ship_col = random.randint(0, size-ship_size)
            if "S" not in board[ship_row][ship_col:ship_col+ship_size]:
                for i in range(ship_size):
                    board[ship_row][ship_col+i] = "S"
                ships += 1
        else:
            ship_row = random.randint(0, size-ship_size)
            ship_col = random.randint(0, size-1)
            if all(board[ship_row+i][ship_col] != "S" for i in range(ship_size)):
                for i in range(ship_size):
                    board[ship_row+i][ship_col] = "S"
                ships += 1

def get_guess(size):
    """
    Prompts the user for a row and column guess.
    
    Args:
    size (int): The size of the grid.
    
    Returns:
    tuple: A tuple containing the row and column guessed by the user.
    """
    while True:
        try:
            row = int(input(f"Guess Row (0-{size-1}): "))
            col = int(input(f"Guess Col (0-{size-1}): "))
            return row, col
        except ValueError:
            print("Invalid input. Please enter integers.")

def is_valid_guess(guess, size):
    """
    Checks if a guess is within the bounds of the grid.
    
    Args:
    guess (tuple): A tuple containing the row and column guessed.
    size (int): The size of the grid.
    
    Returns:
    bool: True if the guess is within bounds, False otherwise.
    """
    row, col = guess
    return 0 <= row < size and 0 <= col < size

def make_guess(board, guess):
    """
    Processes the user's guess and updates the board.
    
    Args:
    board (list): The game board to update.
    guess (tuple): A tuple containing the row and column guessed.
    
    Returns:
    bool: True if the guess hits a ship, False otherwise.
    """
    row, col = guess
    if board[row][col] == "S":
        board[row][col] = "X"
        return True
    elif board[row][col] == "O":
        board[row][col] = "-"
        return False

def all_ships_sunk(board):
    """
    Checks if all ships on the board have been sunk.
    
    Args:
    board (list): The game board to check.
    
    Returns:
    bool: True if all ships are sunk, False otherwise.
    """
    for row in board:
        if "S" in row:
            return False
    return True

def main():
    """
    Main function to run the Battleships game.
    """
    while True:
        try:
            size = int(input("Enter the size of the grid (minimum 5): "))
            if size < 5:
                print("Please enter a size of at least 5.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    num_ships = size // 2
    print(f"Placing {num_ships} ships on the board...")
    
    player_board = create_board(size)
    computer_board = create_board(size)

    place_ships(player_board, size, num_ships)
    place_ships(computer_board, size, num_ships)

    while True:
        print("\nPlayer's Board:")
        print_board(player_board)
        print("\nPlayer's Turn:")
        while True:
            player_guess = get_guess(size)
            if not is_valid_guess(player_guess, size):
                print("Guess out of bounds! Try again.")
                continue
            if make_guess(computer_board, player_guess):
                print("Hit!")
            else:
                print("Miss!")
            break

        if all_ships_sunk(computer_board):
            print("Player wins!")
            break

        print("\nComputer's Turn:")
        while True:
            computer_guess = (random.randint(0, size-1), random.randint(0, size-1))
            if is_valid_guess(computer_guess, size):
                if make_guess(player_board, computer_guess):
                    print(f"Computer hits at {computer_guess}!")
                else:
                    print(f"Computer misses at {computer_guess}.")
                break
        
        if all_ships_sunk(player_board):
            print("Computer wins!")
            break

if __name__ == "__main__":
    main()