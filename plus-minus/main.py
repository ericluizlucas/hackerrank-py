#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

from decimal import Decimal


def plusMinus(arr):
    length = len(arr)
    zerosCount = 0
    positiveCount = 0
    negativeCount = 0

    for i in arr:
        if i == 0:
            zerosCount += 1
        elif i > 0:
            positiveCount += 1
        else:
            negativeCount += 1
    
    positiveProportion = round(Decimal(positiveCount / length), 4)
    negativeProportion = round(Decimal(negativeCount / length), 4)
    zeroProportion = round(Decimal(zerosCount / length), 4)
    print(positiveProportion)
    print(negativeProportion)
    print(zeroProportion)

if __name__ == '__main__':
    arr = [1, 1, 0, -1, -1]

    plusMinus(arr)