
def loadInput(fileName):

        # Loads arrays from Coin1.txt
        coins = []
        with open(fileName) as file:
                for line in file:
                        if line.strip():
                                data = line.replace('[', '').replace(']','').replace(' ', '')
                                coins.append([int(num) for num in data.split(',') if num not in '\n'])

                return coins



def changeslowHelper(coinList, value):

    def changeslow(coins, change):

        minCoins = [0 for c in coins]
        minCoins[0] = change
        # now we recursively step through the algorithm at every level
        # and find the minimum amount for that level
        for coin in [c for c in coins if c <= change]:
            temp = (changeslow(coins, change - coin))
            temp[coins.index(coin)] += 1
            if sum(minCoins) > sum(temp):
                minCoins = temp
                bestSum = temp
        return (minCoins)


    finalCoins = changeslow(coinList, value)

    coinSum = sum(finalCoins)

    return (finalCoins, coinSum)


def main():
    filename = raw_input('Enter a filename: ')
    outFile = open(filename.split(".txt")[0] + "change.txt", 'w')
    lines = loadInput(filename)
    outFile.write("\n\nAlgorithm changeslow:\n")

    for i in range(0, len(lines), 2):
        finalCoins, finalSum = changeslowHelper(lines[i], int(lines[i+1][0]))
        print>>outFile, finalCoins
        print>>outFile, finalSum


if __name__ == "__main__": main()
