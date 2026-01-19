a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# print numbers that are less than 5
for i in a:
    if i < 5:
        print(i)
    else:
        pass
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
b = []
for i in a:
    if i < 5:
        b.append(i)
    else:
        pass
    
print(b)


# ask for a number and return the list of numbers that are less than that number
num = int(input("Enter Number: "))
c = []
for i in a:
    if num > i:
        c.append(i)
    else:
        pass

print(c)