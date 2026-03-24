try:
    number = int(input("enter the number: "))
    print("entered number: ", number)
except:
    print("the transformation was unsuccessful")
print("completion of the program")



try:
    number = int(input("enter the number: "))
    print("entered number: ", number)
except:
    print("the transformation was unsuccessful")
finally:
    print("block try completed execution")
print("completion of the program")




try:
    number = int(input("enter the number: "))
    print("entered number: ", number)
except:
    print("error")



try:
    num1  = int(input("enter the number: "))
    num2 = int(input("enter the second number: "))
    result = num1 / num2
    print(f"result is:  {result}")
except ValueError:
    print("error: enter the number")
except ZeroDivisionError:
    print("error: division by zero")



try:
    number = int(input("enter the number: "))
    result = 100 / number
    print(f"result is: {result}")
except ValueError:
    print("error: enter the number")
except ZeroDivisionError:
    print("error: division by zero")



def get_element_by_index():
    numbers = [10, 20, 30]
    try:
        index = int(input("enter the index: "))
        element = numbers[index]
        print(f"element on the position {index}: {element}")
    except ValueError:
        print("error: not a number entered")
    except IndexError:
        print("error: index is not in range")
get_element_by_index()