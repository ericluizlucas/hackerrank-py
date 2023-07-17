#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesOnHouse = 0
    orangesOnHouse = 0
    for i in apples:
        x = a + i
        if(s <= x <= t):
            applesOnHouse += 1
    for i in oranges:
        x = b + i
        if(s <= x <= t):
            orangesOnHouse += 1
    print(applesOnHouse)
    print(orangesOnHouse)

if __name__ == '__main__':
    s = 7

    t = 10

    a = 4

    b = 12

    m = 3

    n = 3

    apples = [2, 3, -4]

    oranges = [3, -2, -4]

    countApplesAndOranges(s, t, a, b, apples, oranges)
