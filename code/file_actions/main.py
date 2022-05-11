"""
Module for the main functionality of converting data from one file type to others.
"""

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
        print(data[i])


if __name__ == "__main__":
    main()
