"""
Command line tic tac toe game.
"""


def output_field(field):
    i = 0
    for row in field:
        print("\t" + "|".join(row))
        i += 1
        if i != 3:
            print("\t-----")

def create_columns(field):
    columns = [[], [], []]
    for row in field:
        columns[0].append(row[0])
        columns[1].append(row[1])
        columns[2].append(row[2])
    return columns
        
def check_winner(field):
    # Rows
    for row in field:
        if row[0] == row[1] and row[1] == row[2]:
            return True, row[0]
    # Columns
    for column in create_columns(field):
        if column[0] == column[1] and column[1] == column[2]:
            return True, column[0]
    # Diagonals
    # Top left - Bottom right
    if field[0][0] == field[1][1] and field[1][1] == field[2][2]:
        return True, field[0][0]
    # Bottom left - Top right
    if field[2][0] == field[1][1] and field[1][1] == field[0][2]:
        return True, field[2][0]

    return False, None

def validate_winner(winner):
    if winner == " ":
        return False, None
    else:
        return True, winner

def get_row_column(string):
    return int(string[0]), int(string[1])

def main():
    field = [
        [" ", " ", " "], 
        [" ", " ", " "], 
        [" ", " ", " "]
    ]

    player1 = "X"
    player2 = "O"

    for i in range(9):
        if i % 2 == 0:
            current_player = player1
        else:
            current_player = player2

        print(f"Turn {i + 1}, player {current_player} your turn:")
        output_field(field)
        
        move = input("Row, Column: ")

        row, column = get_row_column(move)

        # Place player move
        field[row][column] = current_player

        won, winner = check_winner(field)
        won, winner = validate_winner(winner)
        if won:
            print(f"Player {winner} won!")
            output_field(field)
            return

    print("The game was a draw!")
    output_field(field)
    
main()