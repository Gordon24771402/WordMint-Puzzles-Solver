import numpy as np

# 01: Capture Data
data = []
print('Copy and Paste: ')
while True:
    row = input()
    if row == '':
        break
    data.append(row.lower().split(' '))
data = np.array(data)

# 02: Return Word
while True:
    wordExpect = input("Enter a Word: ").lower()
    if wordExpect == '':
        break

    startIndex = np.where(data == wordExpect[0])

    # Left
    for mainCoordinate in range(len(startIndex[0])):
        x = startIndex[0][mainCoordinate]
        y = startIndex[1][mainCoordinate]
        wordSearch = ''

        try:
            for i in range(len(wordExpect)):
                wordSearch += data[x][y - i]
            if wordSearch == wordExpect:
                print(wordSearch)
        except:
            wordSearch = ''

    # Right
    for mainCoordinate in range(len(startIndex[0])):
        x = startIndex[0][mainCoordinate]
        y = startIndex[1][mainCoordinate]
        wordSearch = ''

        try:
            for i in range(len(wordExpect)):
                wordSearch += data[x][y + i]
            if wordSearch == wordExpect:
                print(wordSearch)
        except:
            wordSearch = ''

    # Up
    for mainCoordinate in range(len(startIndex[0])):
        x = startIndex[0][mainCoordinate]
        y = startIndex[1][mainCoordinate]
        wordSearch = ''

        try:
            for i in range(len(wordExpect)):
                wordSearch += data[x - i][y]
            if wordSearch == wordExpect:
                print(wordSearch)
        except:
            wordSearch = ''

    # Down
    for mainCoordinate in range(len(startIndex[0])):
        x = startIndex[0][mainCoordinate]
        y = startIndex[1][mainCoordinate]
        wordSearch = ''

        try:
            for i in range(len(wordExpect)):
                wordSearch += data[x + i][y]
            if wordSearch == wordExpect:
                print(wordSearch)
        except:
            wordSearch = ''

    # Up-Left
    for mainCoordinate in range(len(startIndex[0])):
        x = startIndex[0][mainCoordinate]
        y = startIndex[1][mainCoordinate]
        wordSearch = ''

        try:
            for i in range(len(wordExpect)):
                wordSearch += data[x - i][y - i]
            if wordSearch == wordExpect:
                print(wordSearch)
        except:
            wordSearch = ''

    # Up-Right
    for mainCoordinate in range(len(startIndex[0])):
        x = startIndex[0][mainCoordinate]
        y = startIndex[1][mainCoordinate]
        wordSearch = ''

        try:
            for i in range(len(wordExpect)):
                wordSearch += data[x - i][y + i]
            if wordSearch == wordExpect:
                print(wordSearch)
        except:
            wordSearch = ''

    # Down-Left
    for mainCoordinate in range(len(startIndex[0])):
        x = startIndex[0][mainCoordinate]
        y = startIndex[1][mainCoordinate]
        wordSearch = ''

        try:
            for i in range(len(wordExpect)):
                wordSearch += data[x + i][y - i]
            if wordSearch == wordExpect:
                print(wordSearch)
        except:
            wordSearch = ''

    # Down-Right
    for mainCoordinate in range(len(startIndex[0])):
        x = startIndex[0][mainCoordinate]
        y = startIndex[1][mainCoordinate]
        wordSearch = ''

        try:
            for i in range(len(wordExpect)):
                wordSearch += data[x + i][y + i]
            if wordSearch == wordExpect:
                print(wordSearch)
        except:
            wordSearch = ''

