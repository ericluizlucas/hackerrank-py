def diagonalDifference(arr):
    length = len(arr)
    primaryDiagSum = 0
    secondaryDiagSum = 0
    for i in range(length):
        primaryDiagSum += arr[i][i]
        secondaryDiagSum += arr[i][length - 1 - i]
    return abs(primaryDiagSum - secondaryDiagSum)

if __name__ == '__main__':
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    result = diagonalDifference(arr)
    print(result)