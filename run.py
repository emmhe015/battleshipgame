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