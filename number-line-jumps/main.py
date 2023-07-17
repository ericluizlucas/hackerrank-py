#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    possible = False
    if(v1 < v2): return "NO"
    while(possible == False and x1 <= 100000000):
        x1 = x1 + v1
        x2 = x2 + v2
        if(x1 == x2): possible = True
    if(possible == True):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    x1 = 0

    v1 = 2

    x2 = 5

    v2 = 3

    result = kangaroo(x1, v1, x2, v2)
    
    print(result)