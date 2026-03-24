from unicodedata import category

x = 12
if x > 10:
    print(x > 10)
elif x > 5:
    print(x >= 5 and x <= 10)
else:
    print(x < 10)



a = 5
b = 6
result = 5 == 6
print(result)
print(a != b)
print (a > b)
print (a < b)

bool1 = True
bool2 = False
print (bool1 == bool2)


age = 22
weight = 58
result = age > 21 and weight == 58
print (result)


result = 4 and "w"
print (result)

result = 0 and "w"
print (result)

age = 22
ismarried = False
result = age > 21 or ismarried
print (result)


result = 4 or "w"
print(result)

result = 0 or "w"
print(result)

age = 22
ismarried = False
print(not age > 21)
print(not ismarried)
print (not 4)
print (not 0)


message = "hello world!"
hello = "hello"
print(hello in message)

gold = "gold"
print(gold in message)

message = "hello world!"
hello = "hello"
print(hello not in message)

gold = "gold"
print(gold not in message)


a = 9
b = 7
result = a > b
print(result)

name1 = "kakbsi"
name2 = "kakbsi"
print(name1 == name2)

age = 20
has_ticket = True
result = age > 18 and has_ticket
print(result)

is_student = False
is_worker = True
result = is_student or is_worker
print(result)

is_raining = False
result = (not is_raining)
print(result)

text = "I have a cat"
result = ("cat" in text)
print(result)

age = 25
salary = 1500
result = (age > 18 and salary > 100)
print(result)

x = 5
y = 10
z = 3
if x > y and x > z:
    print("x is a biggest")
elif y > x and y > z:
    print("y is biggest")
else:
    print("z is a biggest")

s1 = "Hello"
s2 = "Hello"
result = s1 == s2
print(result)

score = 85
if score >= 90:
    print("score is greater than 90")
elif 70 <= score <= 90:
    print("score is good than 70-89")
else:
    print("needs to be tightened up")

age = 25
has_ticket = True
if age > 18 and has_ticket:
    print("you can go through")
else:
    print("access denied")


fruits = ["apple", "banana", "orange"]
result = ("apple" in fruits)
print(result)


num = 15
if 1 <= num <= 10 or 20 <= num <= 30:
    print("Yes number {num} is in the range")
else:
    print("No number {num} is not in the range")


category = "A"
if category == "A" or "B":
    print("high priority")
else:
    print("low priority")


age = 14
if 13 <= age <= 17:
    print("teenager")
else:
    print("not teenager")


day = 4
if 1 <= day <= 5:
    print("weekday")
elif 6 <= day <= 7:
    print("day off")
else:
    print("-")


temp = 30
if temp < 0:
    print("cold")
elif 0 <= temp <= 20:
    print("chilly")
else:
    print("hot")


score = 82
if score < 50:
    print ("low score")
elif 50 <= score <= 75:
    print ("mid score")
else:
    print ("high score")












from unicodedata import category

x = 12
if x > 10:
    print(x > 10)
elif x > 5:
    print(x >= 5 and x <= 10)
else:
    print(x < 10)



a = 5
b = 6
result = 5 == 6
print(result)
print(a != b)
print (a > b)
print (a < b)

bool1 = True
bool2 = False
print (bool1 == bool2)


age = 22
weight = 58
result = age > 21 and weight == 58
print (result)


result = 4 and "w"
print (result)

result = 0 and "w"
print (result)

age = 22
ismarried = False
result = age > 21 or ismarried
print (result)


result = 4 or "w"
print(result)

result = 0 or "w"
print(result)

age = 22
ismarried = False
print(not age > 21)
print(not ismarried)
print (not 4)
print (not 0)


message = "hello world!"
hello = "hello"
print(hello in message)

gold = "gold"
print(gold in message)

message = "hello world!"
hello = "hello"
print(hello not in message)

gold = "gold"
print(gold not in message)


a = 9
b = 7
result = a > b
print(result)

name1 = "kakbsi"
name2 = "kakbsi"
print(name1 == name2)

age = 20
has_ticket = True
result = age > 18 and has_ticket
print(result)

is_student = False
is_worker = True
result = is_student or is_worker
print(result)

is_raining = False
result = (not is_raining)
print(result)

text = "I have a cat"
result = ("cat" in text)
print(result)

age = 25
salary = 1500
result = (age > 18 and salary > 100)
print(result)

x = 5
y = 10
z = 3
if x > y and x > z:
    print("x is a biggest")
elif y > x and y > z:
    print("y is biggest")
else:
    print("z is a biggest")

s1 = "Hello"
s2 = "Hello"
result = s1 == s2
print(result)

score = 85
if score >= 90:
    print("score is greater than 90")
elif 70 <= score <= 90:
    print("score is good than 70-89")
else:
    print("needs to be tightened up")

age = 25
has_ticket = True
if age > 18 and has_ticket:
    print("you can go through")
else:
    print("access denied")


fruits = ["apple", "banana", "orange"]
result = ("apple" in fruits)
print(result)


num = 15
if 1 <= num <= 10 or 20 <= num <= 30:
    print("Yes number {num} is in the range")
else:
    print("No number {num} is not in the range")


category = "A"
if category == "A" or "B":
    print("high priority")
else:
    print("low priority")


age = 14
if 13 <= age <= 17:
    print("teenager")
else:
    print("not teenager")


day = 4
if 1 <= day <= 5:
    print("weekday")
elif 6 <= day <= 7:
    print("day off")
else:
    print("-")


temp = 30
if temp < 0:
    print("cold")
elif 0 <= temp <= 20:
    print("chilly")
else:
    print("hot")


score = 82
if score < 50:
    print ("low score")
elif 50 <= score <= 75:
    print ("mid score")
else:
    print ("high score")




