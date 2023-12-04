"""
advent of code 2023 - Day 3 (parts 1 & 2) [python3]

Author: Eugene Dupler
"""
import re

def main():
    # Open our data file
    input_file = "Day3/input_data.txt"

    try:
        with open(input_file, 'r') as file:
            data = file.read().splitlines()
    except Exception as e:
        print(e)


    # Part 1
    print("Part 1:", sum(findnums(data)))

    # Part 2
    print("Part 2:", gearsum(data))


def findnums(data):
    hits = list()

    for linenum in range(len(data)):

        search = re.compile('[0-9]+')
        
        for this in search.finditer(data[linenum]):
            if this.start() == 0:
                minstart = 0
            else:
                minstart = this.start() - 1

            if this.end() == len(data[linenum]):
                maxend = len(data[linenum]) - 1
            else:
                maxend = this.end()
                
            if this.start() > 0 and data[linenum][minstart] != '.':
                # prev char
                hits.append(int(this.group()))
            elif this.end() < (len(data[linenum]) - 1) and data[linenum][maxend] != '.':
                # next char
                hits.append(int(this.group()))
            elif linenum > 0 and re.search('[^.0-9]', data[linenum - 1][minstart:maxend+1]):
                # prev line, even on diagonal
                hits.append(int(this.group()))
            elif linenum != (len(data) - 1) and re.search('[^.0-9]', data[linenum + 1][minstart:maxend+1]):
                # next line, even on diagonal
                hits.append(int(this.group()))
    return hits


def gearsum(indata):
    # Buffer our list with a 1 char bounding box
    indata.insert(0, '.' * len(indata[0]))
    indata.append('.' * len(indata[-1]))
    data = list(map((lambda x: '.' + x + '.'), indata))

    # Gear locations
    gearloc = set() # x, y
    for y in range(len(data)):
        search = re.compile('\*')
        for this in search.finditer(data[y]):
            gearloc.add((this.start(), y))

    # Number locations
    numloc = set() # number, x, y
    for y in range(len(data)):
        search = re.compile('[0-9]+')
        for this in search.finditer(data[y]):
            numloc.add((this.group(), this.start(), y))

    found = list()

    sum = 0

    for gear in gearloc:
        # print(gear)
        thisgear = set()
    
        for numset in numloc:
            checkbox = set()
            num, x, y = numset
            # print('num', num, x, y)

            for ybox in (y-1,y,y+1):
                for xbox in (range(x-1,len(str(num))+x+1)):
                    checkbox.add((xbox,ybox))

            gearset = { gear }
            # print(gear, checkbox)
            if gearset.intersection(checkbox):
                thisgear.add(numset)
                # print(numset)

        if len(thisgear) == 2:
            prod = 1
            for this_numset in thisgear:
                prod *= int(this_numset[0])
            sum += prod

    return sum
    
    
if __name__ == "__main__":
    main()