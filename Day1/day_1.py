"""
advent of code 2023 - Day 1 (parts 1 & 2) [python3]

Author: Eugene Dupler
"""

def main():
    # Open our data file
    input_file = "Day1/input_data.txt"

    try:
        with open(input_file, 'r') as file:
            data = file.read().splitlines()
    except Exception as e:
        print(e)

    # Part 1
    sum = 0
    for line in data:
        sum += getdigits(line)

    print("Part 1: ", sum)


    # Part 2
    sum = 0
    for line in data:
        line = spellout(line)
        sum += getdigits(line)


    print("Part 2: ", sum)
    


def spellout(this_string):
    alphas = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    # This is sketchy and not well explained, but this string "eightwothree", should become "823" for
    # eval, not "8wo3".  It makes a huge difference in this line: "126dzbvg6two4oneightntd"

    for alpha in alphas:
        this_string = this_string.replace(alpha, alpha + str(alphas[alpha]) + alpha)

    return this_string

def getdigits(string):
    results = ""
    for character in string:
        if character.isnumeric():
            results += character

    return int(results[0] + results[-1])

if __name__ == "__main__":
    main()