"""
Module containing functionality for reading and writing to different type of files.
"""

import os
import csv
import json


def read_txt(file_path):
    """
    Reads all lines from file into a list of strings.

    Args:
        file_path (str): Path to file

    Returns:
        list[str]: List of read lines
    """
    with open(file_path, "r") as f:
        return f.readlines()


def read_csv(file_path):
    """
    Reads all lines from csv file into a list representing the header 
    and a seperate list holding all data.

    Args:
        file_path (str): Path to file

    Returns:
        tuple[list[str], list[list[str]]]: Header, other rows
    """
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        header = next(reader)  # Save header
        rows = []
        for row in reader:
            rows.append(row)
        return header, rows


def write_csv(file_path, header, data):
    """
    Saves passed data to a csv file, writing the header and data

    Args:
        file_path (str): Path to file to write
        header (list[str]): List with header values
        data (list[list[str]]): List containing each row (as a list of string)
    """
    with open(file_path, "w", newline="") as f:  # Add encoding='UTF8' if needed, newline removes emptyline between rows
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)


def read_json(file_path):
    """
    Reads the object from the json file.

    Args:
        file_path (str): Path to json file

    Returns:
        any: Object contained in file
    """
    with open(file_path, "r") as f:
        json_object = json.load(f)
        return json_object


def write_json(file_path, data):
    """
    Saves passed object into a json file.

    Args:
        file_path (str): Path to file
        data (any): Object to save in json file
    """
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4, sort_keys=True)


def update_json_dictionary(file_path, data):
    """
    Updates the dictionary contained in the json file.

    Args:
        file_path (str): Path to json file
        data (dict): Dictionary to update
    """
    read_json = {}

    if os.path.isfile(file_path):  # Read only if file exists.
        with open(file_path, "r") as f:
            read_json = json.load(f)

    read_json.update(data)

    write_json(file_path, read_json)  # Save to file
