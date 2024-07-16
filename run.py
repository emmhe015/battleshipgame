import random

def create_board(size):
    """
    Creates a game board of given size.
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
    board (list): The game board to place ships on.
    size (int): The size of the grid.
    num_ships (int): The number of ships to place.
    """
    ships = 0
    while ships < num_ships:
        ship_row = random.randint(0, size-1)
        ship_col = random.randint(0, size-1)
        if board[ship_row][ship_col] != "S":
            board[ship_row][ship_col] = "S"
            ships += 1


def get_guess():
    """
    Prompts the user for a row and column guess.
    
    Returns:
    tuple: A tuple containing the row and column guessed by the user.
    """
    while True:
        try:
            row = int(input("Guess Row: "))
            col = int(input("Guess Col: "))
            return row, col
        except ValueError:
            print("Invalid input. Please enter integers.")

def is_valid_guess(guess, size):
    """
    Checks if a guess is within the bounds of the grid.
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
    main function to run the Battleships game
    """
    while True:
        try:
            size = int(input("Enter the size of the grid: "))
            if size<= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    player_board = create_board(size)
    computer_board = create_board(size)

    num_ships = 3
    place_ships(player_board, size, num_ships)
    place_ships(computer_board, size, num_ships)

    while True:
        print("\nPlayer's Board:")
        print_board(player_board)
        print("\nPlayer's Turn:")
        while True:
            player_guess = get_guess()
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