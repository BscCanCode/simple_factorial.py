import sys
def recursion(n):
    if n==0 or n==1:
        return 1
    else:
        return n* recursion(n-1)

try:
    n=int(input("Enter the number to factorial of:"))
    if n<0:
        print("Negative numbers don't have factorial!")
    else:
        print(f"The factorial of {n} is:",recursion(n))
except ValueError:
    print("Only Positive integers have factorial,not strings or negative number")
    sys.exit()
