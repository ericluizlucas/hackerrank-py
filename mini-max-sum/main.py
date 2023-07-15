#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    maxSum = 0
    minSum = 0
    for i in range(len(arr)):
        if(i != 0):
            maxSum += arr[i]
        if(i < len(arr)-1):
            minSum += arr[i]
    print(f"{minSum} {maxSum}")

if __name__ == '__main__':

    arr = [9, 7, 5, 3, 1]

    miniMaxSum(arr)
