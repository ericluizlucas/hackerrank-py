#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if(s[-2:] == "AM") and s[:2] == "12":
        return "00" + s[2:-2]
    
    elif s[-2:] == "AM":
        return s[:-2]
    
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
    
    else:
        return f"{str(int(s[:2]) + 12)}" + s[2:-2]

if __name__ == '__main__':
    tests = ["07:05:45 AM", "07:05:45 PM", "12:05:45 AM", "12:05:45 PM"]

    for s in tests:
        result = timeConversion(s)
        print(f"original: {s}; converted: {result}")