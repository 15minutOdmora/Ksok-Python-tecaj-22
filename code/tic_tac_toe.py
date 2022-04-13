"""
Console Tic Tac Toe game.
"""


def output_field(field):
    """
    Print the field to the console.
    """
    print("\t"  + "|".join(field[0]))
    print("\t-----")
    print("\t"  + "|".join(field[1]))
    print("\t-----")
    print("\t" + "|".join(field[2]))


def read_player_input(niz):
    """
    Convert player input into row index and column index.
    """
    return int(niz[0]), int(niz[1])


def main():
    """
    Main method for running the game.
    """
    field = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    # Define player signs
    player_1 = "X"  
    player_2 = "O"
    # Main loop
    for i in range(9):
        # Get player move (position to place sign)
        player_move = input("Row, Column: ")
        row, column = read_player_input(player_move)

        # Define player on this turn
        # player = None
        if i % 2 == 0:
            player = player_1
        else:
            player = player_2
        # Set correct sign to field on passed position
        field[row][column] = player
        # Display field after update
        output_field(field)

# Call main method
main()