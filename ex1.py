from random import randint
list_lenght = int(input("enter list lenght: "))
list_n = [randint(1, 100) for _ in range(list_lenght)]

print(list_n)
x = int(input("enter desired element: "))
print(f"element: {x}")
min_difference = 100
count = 0
for i in list_n:
    if i == x:
        count +=1
    else:
        difference = ((x - i)**2)**0.5
        if difference < min_difference:
            min_difference = difference
            number = i

print(f"element {x} occurs {count} times" if count >0 else f"the closest element is: {number}")

#print(f"element {x} occurs {count} times" if count >0 else f"there isn't {x} in massiv")