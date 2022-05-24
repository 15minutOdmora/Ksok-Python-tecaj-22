"""
Module for the main functionality of converting data from one file type to others.
"""

import os
from file_handling import *
import conversions


DATA_PATH = "code/file_actions/data/"


def main():
    
    full_path = DATA_PATH + "dallas_players.txt"

    # Read and clean lines
    data = []
    for line in read_txt(full_path):
        clean_line = line[:-1]
        line_data = clean_line.split(" ")
        data.append(line_data)

    # Convert data
    for i in range(1, len(data)):
        data[i][-1] = conversions.dollars_to_euro(data[i][-1])
        data[i][-3] = conversions.lbs_to_kg(data[i][-3])
        data[i][-4] = conversions.imperial_to_metric(data[i][-4])

    header = data[0]
    data = data[1:]

    # Save to csv
    write_csv(os.path.join(DATA_PATH, "dallas_players.csv"), header, data)

    # Save to json
    data_list = []
    for player in data:
        player_dict = {}
        # Populate player dict
        for i, column in enumerate(header): # ["ena", "dva"] -> [(0, "ena"), (1, "dva")]
            player_dict[column] = player[i]

        data_list.append(player_dict)

    write_json(os.path.join(DATA_PATH, "dallas_players.json"), data_list)
    
    # Example reading some data from saved json
    read_data = read_json(os.path.join(DATA_PATH, "dallas_players.json"))
    doncic = read_data[7]
    print(doncic["Name"])


if __name__ == "__main__":
    main()
