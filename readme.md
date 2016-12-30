# Dynamic ('changedp'), greedy ('greedyChange') and divide and conquer ('slowchange') implementations of the [change-making problem](https://en.wikipedia.org/wiki/Change-making_problem).

##Step 1: Testing changedp and greedyChange:

Run:

`python greedyAndChangedp.py`

When prompted, enter the name of whatever any .txt file that exists in the directory and which contains data like that in Coin1.txt. You will then find another file in that directory called [inputFileName]change.txt, which contains the output.

Here is an example:

$ `python greedyAndChangeDp.py `
Enter a filename: `Coin1.txt`
$ `cat Coin1change.txt `

  Algorithm changedp: [0, 0, 0, 1, 1] 2         
  Alorithm greedy: [0, 0, 0, 1, 1] 2         

  Algorithm changedp: [0, 0, 3, 0] 3      
  Alorithm greedy: [3, 1, 0, 1] 5        


  Algorithm changedp: [0, 0, 0, 1, 7] 8       
  Alorithm greedy: [0, 0, 0, 1, 7] 8            


Each of the arrays represents the number of coins of each denomination that were used
 (based on their position in the original input array) and the number at the end
 represents the number of coins used.  

##Step 2: Testing changeslow:

You can only use low values for n and A for this one, so we have provided a sample
.txt file that changeslow can handle.

Run it with `python changeslow.py`


As with above, you will be prompted to enter the name of a file. Enter CoinSlow.txt. When the program is done you will find another file in that directory called CoinSlowchange.txt, which contains the output.

Example:

$ `python changeslow.py `
Enter a filename: `CoinSlow.txt`
$ `cat CoinSlowchange.txt`

  Algorithm changeslow:
  [1, 1, 3]
  5
  [0, 0, 1, 1, 0]
  2
  [7, 1, 0, 0]
  8
