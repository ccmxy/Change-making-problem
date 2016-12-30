import sys

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
def changedp(V, A):
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
    for i in range(2, A + 1):
        if i in V:
            #the index(i) is the denomination of one of our coins,
            #so we only need 1 coin to make i cents
            X.append(1)
            matrix.append([0, i])
        else:
            min = 1000
            #loop to find min{ (X[1]+X[leng-1]), (X[2]+X[len-2]), (X[3]+X[len-3])... (X[len-1]+X[1]) }
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
    for i in range(0, len(V)):
        coinPurse.append(0)

    print matrix
    loadCoinPurse(matrix, lastVal, V, coinPurse)
    return coinPurse, X[-1]



def loadCoinPurse(matrix, lastVal, V, coinPurse):

    if lastVal[0] == 0:
        index = V.index(lastVal[1])
        coinPurse[index] += 1

    elif lastVal[0] == 1 and lastVal[1] != 1:
        index = V.index(1)
        coinPurse[index] += 1

        lastVal = matrix[lastVal[1]]
        loadCoinPurse(matrix, lastVal, V, coinPurse)

    elif lastVal[0] == 1 and lastVal[1] == 1:
        index = V.index(1)
        coinPurse[index] += 2


    elif lastVal[0] != 1:
        index = V.index(lastVal[0])
        coinPurse[index] += 1
        lastVal = matrix[lastVal[1]]
        loadCoinPurse(matrix, lastVal, V, coinPurse)

def greedyChange(myArray, value):

   #assuming the array is sorted, you don't need to sort,
   # else the array will need to be sorted into descending order
   # so that the largest value is the first value in the array;
   changeArray = []
   for i in range(0, len(myArray)):
       changeArray.insert(i, 0)
   coins = 0
   i = len(myArray) -1;
   count = 0
   while (value >= 0):
       if (myArray[i] <= value):
           value = value - myArray[i]
           coins += 1
           count += 1
       else:
           changeArray.pop(i)
           changeArray.insert(i, count)
           count = 0
           if (value == 0):
               break
           i -= 1
   return changeArray, coins


def main():
    filename = raw_input('Enter a filename: ')
    outFile = open(filename.split(".txt")[0] + "change.txt", 'w')
    lines = loadInput(filename)


    for i in range(0, len(lines), 2):
        outFile.write("\n\nAlgorithm changedp: ")
        changeArray, minCoins = changedp(lines[i], int(lines[i+1][0]))
        print>>outFile, changeArray, minCoins

        outFile.write("Alorithm greedy: ")
        changeArray, minCoins = greedyChange(lines[i], int(lines[i+1][0]))
        print>>outFile, changeArray, minCoins


if __name__ == "__main__": main()
