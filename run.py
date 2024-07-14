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