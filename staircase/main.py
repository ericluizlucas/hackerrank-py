#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(n):
        line = ""
        for j in range(n):
            if(j >= n-i-1):
                line += "#"
            else:
                line += " "
        print(line)

if __name__ == '__main__':
    n = 4

    staircase(n)
