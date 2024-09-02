#6
for i in range(1, 6): #using of loop
    print(i)

#7
count = 5
while count > 0:
    print(count)
    count -= 1

#8
total = 0 
for num in range(1, 11): #using for loop
    total += num
print(f"The sum of the number from 1 to 10 is: {total}")

#9
fruits = ["apple","banana","cherry"]
for fruit in fruits: # for loop to name the fruits
    print(fruit)

#10
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i*j}")
    print()