#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

import math


def gradingStudents(grades):
    resp = []
    for i in grades:
        if(i >= 38):
            if(i % 5 > 2):
                print(f"before {i}")
                i = math.ceil(i/5) * 5
        resp.append(i)
    return resp

if __name__ == '__main__':
    grades = [73, 67, 38, 33]

    result = gradingStudents(grades)
    
    for i in result:
        print(i)