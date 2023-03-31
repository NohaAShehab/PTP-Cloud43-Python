print("---------- welcome to helper module , copyrights reserved to cloud43@iti")

name = 'Ahmed'

def askforInt(message):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print("--- invalid number please enter it again ---")

# age= askforInt("please enter your age: ")
# print(age)
