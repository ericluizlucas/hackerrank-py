#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    candles.sort()
    maxHeight = candles[len(candles)-1]
    countTallest = 0
    for i in candles:
        if(i == maxHeight):
            countTallest += 1
    return countTallest

if __name__ == '__main__':
    candles = [3, 2, 1, 3]

    result = birthdayCakeCandles(candles)
    print(result)
