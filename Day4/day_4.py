"""
advent of code 2023 - Day 4 (parts 1 & 2) [python3]

Author: Eugene Dupler
"""

def main():
    # Open our data file
    input_file = "Day4/input_data.txt"

    try:
        with open(input_file, 'r') as file:
            data = file.read().splitlines()
    except Exception as e:
        print(e)


    # Part 1
    points = 0
    for line in data:

        card_count = match_total(line) - 1
        if card_count >= 0:
            points += (2 ** card_count)

    print("Part 1:", points)

    # Part 2
    counts = list()
    [counts.append(0) for x in (range(len(data)))]

    card = 0
    for line in data:
        add_counts(card, counts, line)
        card += 1

    print("Part 2:", sum(counts))


def add_counts(card, counts, line):
        counts[card] += 1 # increment this card count
        card_count = match_total(line)
        # print('card ' + str(card + 1) + ' has ' + str(card_count) + ' matches.')
        for next in (range(1,card_count+1)):
            if (next + card) < len(counts):
                counts[next + card] += 1 * counts[card] # This was the tricky part - you have to multiply the count of copies
        card += 1 # go to the next card


def match_total(line):
    cardnumber = line.split(':')[0].split(' ')[-1]
    keynums = line.split(':')[-1].split('|')[0]
    chknums = line.split(':')[-1].split('|')[-1]

    # Use sets to make it easier to check for matches
    key_set = set()
    chk_set = set()

    [key_set.add(x) for x in keynums.split()]
    [chk_set.add(x) for x in chknums.split()]
    
    counter = 0
    for chk in chk_set:
        if { chk }.intersection(key_set):
            counter += 1

    return counter

    
    
if __name__ == "__main__":
    main()