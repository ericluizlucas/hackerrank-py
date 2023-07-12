# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    sum = 0
    for i in ar:
        sum += i
    return sum

if __name__ == '__main__':
    ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

    result = aVeryBigSum(ar)
    print(result)