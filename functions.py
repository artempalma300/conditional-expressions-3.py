def say_hello(): print("hello")
def say_goodbye(): print("goodbye")

say_hello()
say_goodbye()


def print_messages():
    def say_hello(): print("hello")
    def say_goodbye(): print("goodbye")

    say_hello()
    say_goodbye()

print_messages()



def my_fn(a, b):
    a = a + 1
    c = a + b
    return c
res = my_fn (10, 3)
print (res)


def say_hello():
    print("hello")

say_hello()
say_hello()
say_hello()


def say_name():
    print("my name is Artem")

say_name()



def print_numbers():
    print("1 2 3 4 5")

print_numbers()


def square():
    result = 4 * 4
    print(result)

square()



def repeat_message():
    print("Python is cool")

repeat_message()
repeat_message()
repeat_message()
repeat_message()
repeat_message()


def main():
    say_hello()
    say_goodbye()

main()


def say_morning():
    print("good morning")

def say_evening():
    print("good evening")

def main():
    say_morning()
    say_evening()

main()


def messages():
    say_hello()
    say_goodbye()

messages()




def menu():
    print("1. Start")
    print("2. Settings")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        start()
    elif choice == "2":
        settings()
    elif choice == "3":
        exit_program()
    else:
        print("Invalid choice, please try again")


def start():
    print("getting started")

def settings():
    print("setting up")

def exit_program():
    print("exiting program")

menu()




def hello():
    print("hello")

def bye():
    print("bye")

def main():
    print("welcome")
    hello()
    bye()

if __name__ == "__main__":
    main()

