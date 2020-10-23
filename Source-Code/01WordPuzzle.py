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
    wordSearch = input('Enter a Word: ').lower()
    if wordSearch == '':
        break

    startIndex = np.where(data == wordSearch[0])
    for mainCoordinate in range(len(startIndex[0])):
        x = startIndex[0][mainCoordinate]
        y = startIndex[1][mainCoordinate]

        if x == 0 and y == 0:
            peripheral = np.array([
                '', '', '',
                '', data[x][y + 1],
                '', data[x + 1][y], data[x + 1][y + 1]
            ])
        elif x == 0 and y == len(data[0]) - 1:
            peripheral = np.array([
                '', '', '',
                data[x][y - 1], '',
                data[x + 1][y - 1], data[x + 1][y], ''
            ])
        elif x == len(data) - 1 and y == len(data[0]) - 1:
            peripheral = np.array([
                data[x - 1][y - 1], data[x - 1][y], '',
                data[x][y - 1], '',
                '', '', ''
            ])
        elif x == len(data) - 1 and y == 0:
            peripheral = np.array([
                '', data[x - 1][y], data[x - 1][y + 1],
                '', data[x][y + 1],
                '', '', ''
            ])
        elif x == 0:
            peripheral = np.array([
                '', '', '',
                data[x][y - 1], data[x][y + 1],
                data[x + 1][y - 1], data[x + 1][y], data[x + 1][y + 1]
            ])
        elif y == len(data[0]) - 1:
            peripheral = np.array([
                data[x - 1][y - 1], data[x - 1][y], '',
                data[x][y - 1], '',
                data[x + 1][y - 1], data[x + 1][y], ''
            ])
        elif x == len(data) - 1:
            peripheral = np.array([
                data[x - 1][y - 1], data[x - 1][y], data[x - 1][y + 1],
                data[x][y - 1], data[x][y + 1],
                '', '', ''
            ])
        elif y == 0:
            peripheral = np.array([
                '', data[x - 1][y], data[x - 1][y + 1],
                '', data[x][y + 1],
                '', data[x + 1][y], data[x + 1][y + 1]
            ])
        else:
            peripheral = np.array([
                data[x - 1][y - 1], data[x - 1][y], data[x - 1][y + 1],
                data[x][y - 1], data[x][y + 1],
                data[x + 1][y - 1], data[x + 1][y], data[x + 1][y + 1]
            ])

        print(peripheral)
