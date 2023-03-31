

def askforInt(message):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print("--- invalid number please enter it again ---")

def askforString(message):
    while True:
        val = input(message)
        if val.isalpha():
            return val
        print("--- invalid number please enter it again ---")
