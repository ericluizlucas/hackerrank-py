#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    countMostBreak = 0
    countLeastBreak = 0
    mostPoints = 0
    leastPoints = 0
    for i in range(len(scores)):
        if(i == 0):
            mostPoints = scores[i]
            leastPoints = scores[i]
        elif(scores[i] > mostPoints):
            mostPoints = scores[i]
            countMostBreak += 1
        elif(scores[i] < leastPoints):
            leastPoints = scores[i]
            countLeastBreak += 1
    return [countMostBreak, countLeastBreak]

if __name__ == '__main__':
    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]

    result = breakingRecords(scores)
    print(result)