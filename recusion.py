def recursion(n):
    if n==0 or n==1:
        return 1
    else:
        return n* recursion(n-1)
while True:
    try:
        n=int(input("Enter the number between (1-100) to find factorial of:"))
        if n<0:
            print("Negative numbers don't have a factorial")
        elif n<=100:
            print(f"The factorial of {n} is:",recursion(n))
            print("-------------------------------------------------------------")
        else:
            print("To avoid stack overflow you can enter value between 1-100")
            break
        b=input("Would you like to continue? yes/no:")
        if b=="no":
            print("Exit is done")
            break
        elif b=="yes":
            continue
        else:
            print("You should enter either a yes or no")
            break
            
        
    except ValueError:
        print("Only positive integers factorials are accepted,Strings does not have a concept named factorial")
        break
