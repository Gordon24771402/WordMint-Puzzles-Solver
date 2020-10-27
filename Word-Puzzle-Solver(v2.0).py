import numpy as np

# 01: Capture Data
data = []
print('Copy and Paste: ')
while True:
    row = input()
    if row == '':
        break
    data.append(row.upper().split(' '))
data = np.array(data)

# 02: Return Word
while True:
    wordExpect = input("Enter a Word: ").upper()
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
                answer = data.copy()
                for i in range(len(wordExpect)):
                    answer[x][y - i] = '*'
                for x in answer:
                    print(" ".join(map(str, x)))
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
                answer = data.copy()
                for i in range(len(wordExpect)):
                    answer[x][y + i] = '*'
                for x in answer:
                    print(" ".join(map(str, x)))
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
                answer = data.copy()
                for i in range(len(wordExpect)):
                    answer[x - i][y] = '*'
                for x in answer:
                    print(" ".join(map(str, x)))
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
                answer = data.copy()
                for i in range(len(wordExpect)):
                    answer[x + i][y] = '*'
                for x in answer:
                    print(" ".join(map(str, x)))
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
                answer = data.copy()
                for i in range(len(wordExpect)):
                    answer[x - i][y - i] = '*'
                for x in answer:
                    print(" ".join(map(str, x)))
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
                answer = data.copy()
                for i in range(len(wordExpect)):
                    answer[x - i][y + i] = '*'
                for x in answer:
                    print(" ".join(map(str, x)))
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
                answer = data.copy()
                for i in range(len(wordExpect)):
                    answer[x + i][y - i] = '*'
                for x in answer:
                    print(" ".join(map(str, x)))
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
                answer = data.copy()
                for i in range(len(wordExpect)):
                    answer[x + i][y + i] = '*'
                for x in answer:
                    print(" ".join(map(str, x)))
        except:
            wordSearch = ''

