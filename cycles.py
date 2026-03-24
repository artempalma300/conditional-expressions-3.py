number = 10

while number < 5:
    print (f"number = {number}")
    number += 1
else:
    print(f"number = {number}. the cycles is finished")
print ("the program has completed its work")



number = 1

while number < 5:
    print(f"number = {number}")
    number += 1
print ("the program has completed its work")



i = 10
while i >= 1:
    print(f"i = {i}")
    i -= 1
print ("the program has completed its work")



i = 2
while i <= 20:
    print (f"i = {i}")
    i += 2
print ("the program has completed its work")



n = int(input("enter the number: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print(f"sum = {sum}")
print ("the program has completed its work")



i = 1
while i <= 100:
    print (f"i = {i}")
    i += 1
print ("the program has completed its work")


n = int(input("enter the number: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print (f"sum = {sum}")
print (" the program has complete its work")



n = int(input("enter the number: "))
divisor = 2
while divisor <= n // 2:
    if n % divisor == 0:
        print (f"the smallest divisor is:{divisor}")
        break
else:
    print ("the n is prime, no divisors found")



for n in range (4, 10):
    print (n, end=" ")


for n in range (0, 10, 2):
    print (n, end=" ")



message = "hello"
for c in message:
    print(c)
else:
    print(f"last character: {c}. the cycles is completed")
print("the program has completed its work")


i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1


for c1 in "ab":
    for c2 in "ba":
        print(f"{c1}{c2}")



number = 0
while number < 5:
    number += 1
    if number == 3:
        continue
    print (f"number = {number}")


for n in range (9):
    print (n, end=" ")

for number in range (1, 11):
    print (number)


for n in range (0, 22, 2):
    print(n, end=" ")


total = 0
for number in range (1, 11):
    total += number
print(total)


for j in range (1, 11):
    print (f"5 * {j} = {5 * j}")


for n in range (10, 0, -1):
    print (n)


for n in range (1, 11):
    square = n ** 2
    print(square)



word = "Python"
for char in word:
    print(char)


