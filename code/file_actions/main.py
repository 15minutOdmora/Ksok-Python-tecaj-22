"""
Module for the main functionality of converting data from one file type to others.
"""

import os

from file_handling import *
import conversions


DATA_PATH = "code/file_actions/data/"

def join_path(path1, path2):
    return os.path.join(path1, path2)


def get_from_txt_file():
    """
    Grabs header and all rows from set txt file.
    """
    rows = read_txt(join_path(DATA_PATH, "dallas_players.txt"))
    header = rows[0][:-1].split(" ")
    data = []
    for row in rows[1:]:
        data.append(row[:-1].split(" "))
    return header, data

def main():
    """
    Convert txt file to .csv and .json
    """
    header, data = get_from_txt_file()

    write_csv(join_path(DATA_PATH, "dallas_players.csv"), header, data)

    players = []
    for row in data:
        print(row)
        player = {}
        for i, column in enumerate(header):
            player[column] = row[i]
        players.append(player)
    
    write_json(join_path(DATA_PATH, "dallas_players.json"), players)


if __name__ == "__main__":
    main()