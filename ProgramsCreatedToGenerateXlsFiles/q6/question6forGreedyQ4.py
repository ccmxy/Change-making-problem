import sys
import timeit
import xlwt

def loadInput(fileName):

        # Loads arrays from Coin1.txt
        coins = []
        with open(fileName) as file:
                for line in file:
                        if line.strip():
                                data = line.replace('[', '').replace(']','').replace(' ', '')
                                coins.append([int(num) for num in data.split(',') if num not in '\n'])

                return coins



# # # # # # # # # # # #
# changedp
# # # # # # # # # # # #
def changedp(inputArray, inputValue):
    #X is an array where the index(idx) represents a number of cents,
    # and the value at each index is the minimum number of coins it takes
    # to get to idx cents.
    #  X[cents] = lowestNumCoins
    X = []

    #matrix is an array where the index(m_idx) represents a number of cents,
    # and value at each index is a [lowerXIndex, higherXIndex] element
    #that represents the X[idx] indexes of lowest numCoins value for:
    #       X[lowerXIndex] + X[higherXIndex] = numCoins, where
    #       lowerXIndex + higherXIndex = m_idx
    matrix = []

    #start with v0 and v1 values
    X.append(0)
    X.append(1)
    matrix.append([0, 0])
    matrix.append([0, 1])

    #Build matrix[][] and X[]
    for i in range(2, inputValue + 1):
        if i in inputArray:
            #the index(i) is the denomination of one of our coins,
            #so we only need 1 coin to make i cents
            X.append(1)
            matrix.append([0, i])
        else:
            min = 1000
            #loop to find min{ (X[1]+X[leng-1]), (X[2]+X[len-2]), (X[3]+X[len-3])... (X[1]+X[len-1]) }
            for j in range(1, len(X)):
                temp = X[j] + X[len(X) - j]
                if temp < min:
                    min = temp
                    lowerIndex = j
                    upperIndex = len(X) - j

            matrix.append([lowerIndex, upperIndex])
            X.append(min)

    coinPurse = []

    lastVal = matrix[-1]
    for i in range(0, len(inputArray)):
        coinPurse.append(0)


    printCoins(matrix, lastVal, X, inputArray, coinPurse)
    return coinPurse, X[-1]






def printCoins(matrix, lastVal, X, inputArray, coinPurse):

    if lastVal[0] == 0:
        index = inputArray.index(lastVal[1])
        coinPurse[index] += 1

    elif lastVal[0] == 1 and lastVal[1] != 1:
        index = inputArray.index(1)
        coinPurse[index] += 1

        lastVal = matrix[lastVal[1]]
        printCoins(matrix, lastVal, X, inputArray, coinPurse)

    elif lastVal[0] == 1 and lastVal[1] == 1:
        index = inputArray.index(1)
        coinPurse[index] += 2


    elif lastVal[0] != 1:
        index = inputArray.index(lastVal[0])
        coinPurse[index] += 1
        lastVal = matrix[lastVal[1]]
        printCoins(matrix, lastVal, X, inputArray, coinPurse)


def greedyChange(myArray, value):

            #assuming the array is sorted, you don't need to sort,
            # else the array will need to be sorted into descending order
            # so that the largest value is the first value in the array;
            coins = 0
            i = len(myArray) -1;
            count = 0
            changeArray = []
            while (value > -1):
                if (myArray[i] <= value):
                    value = value - myArray[i]
                    coins += 1
                    count += 1
                else:
                    changeArray.insert(i, count)
                    count = 0
                    if (value == 0):
                        break
                    i -= 1
            return changeArray, coins



book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet("Sheet 1")

sheet1.write(0,0,"n")
sheet1.write(0,1,"v1")
sheet1.write(0,2,"v2")

V1 = [1, 2, 6, 12, 24, 48, 60]
V2 = [1, 6, 13, 37, 150]

j = 1
for i in range(2000, 2202):
    setup = "from __main__ import changedp, greedyChange, V1, V2, i"
    sheet1.write(j, 0, i)
    time1 = timeit.timeit("greedyChange(V1, i)", setup, number=1)
    sheet1.write(j, 1, time1)
    time2 = timeit.timeit("greedyChange(V2, i)", setup, number=1)
    sheet1.write(j, 2, time2)

    j += 1

book.save("Q6DataForQ4Greedy.xls")
