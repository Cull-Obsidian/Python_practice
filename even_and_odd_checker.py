num = int(input("Enter a Number: "))

def checker(num):
    if num % 2 == 0:
        return(f"The Number you Provided is Even")
    elif num % 2 != 0:
        return(f"The Number your Provided is Odd")
    else:
        return(f"The Number is invalid")
    
def checker4(num):
    if num % 4 == 0:
        print("Congrats! Your number is also divisible by 4")
    else:
        pass
    
print(checker(num))
checker4(num)
