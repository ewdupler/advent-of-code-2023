"""
advent of code 2023 - Day 2 (parts 1 & 2) [python3]

Author: Eugene Dupler
"""

def main():
    # Open our data file
    input_file = "Day2/input_data.txt"

    try:
        with open(input_file, 'r') as file:
            data = file.read().splitlines()
    except Exception as e:
        print(e)