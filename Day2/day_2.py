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


    # Part 1
    game_sum = 0

    for line in data:
        game_desc, plays = line.split(':')
        game = game_desc.split(' ')[-1]
        if getrgb(plays):
            game_sum += int(game)

    print("Part 1:", game_sum)

    # Part 2
    game_sum = 0
    for line in data:
        game_desc, plays = line.split(':')
        game_sum += power(plays)

    print("Part 2:", game_sum)

    
def getrgb(plays):

    max = {
        "red": 12,
        "blue": 14,
        "green": 13
    }

    for play in plays.split(';'):
        red = 0
        blue = 0
        green = 0
        for die in play.split(','):
            count, color = die.split()
            if color == "red":
                red += int(count)
            elif color == "blue":
                blue += int(count)
            elif color == "green":
                green += int(count)
        if max["red"] < red or max["green"] < green or max["blue"] < blue:
            return False

    return True


def power(plays):
    mins = {
        "red": 1,
        "green": 1,
        "blue": 1
    }

    for play in plays.split(';'):
        for die in play.split(','):
            count, color = die.split()
            if int(mins[color]) < int(count):
                mins[color] = int(count)

    return mins["red"] * mins["green"] * mins["blue"]
    
    
if __name__ == "__main__":
    main()