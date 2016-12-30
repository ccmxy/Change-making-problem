import sys
import timeit
import xlwt

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


book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet("Sheet 1")

sheet1.write(0, 0, "n")
sheet1.write(0, 1, "slowchange V1")
sheet1.write(0, 2, "slowchange V2")


V = [1, 2, 3, 7]

V1 = [1, 2, 6, 12, 24, 48, 60]
V2 = [1, 6, 13, 37, 150]


j = 1
for i in range(1, 25):
    setup = "from __main__ import changeslowHelper, V, V1, V2, i"
    sheet1.write(j, 0, i)
    time1 = timeit.timeit("changeslowHelper(V1, i)", setup, number=1)
    sheet1.write(j, 1, time1)
    time2 = timeit.timeit("changeslowHelper(V2, i)", setup, number=1)
    sheet1.write(j, 2, time2)


    j += 1

book.save("question6DataforQ4ChangeSlow.xls")
