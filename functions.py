""" 1- define function """

# def testfun():
#     pass
#
#
# res = testfun()  # return None object- --> falsy values
# testfun()

# def testfun():
#     return
#
#
# res = testfun()  # return None object- --> falsy values
# testfun()

""" 2- function """

# def sayHello():
#     print('Hello world')
#
#
# x = sayHello()

""" function that accepts data """

# def get_fullname(fname, lname):
#     fullname= fname + lname
#     print(fullname)
#
#
# get_fullname('Noha', 'Shehab')

""" function returns with datA """

# def get_fullname(fname, lname):
#     fullname= fname + lname
#     print(fullname)
#     return fullname
#
#
# myfullname=get_fullname('Noha', 'Shehab')
# def get_fullname(fname, lname):
#     fullname= fname + lname
#     print(fullname)
#     return fname, lname, fullname  # tuple
#
#
# myfullname=get_fullname('Noha', 'Shehab')
# print(myfullname)

""" functions with default arguments """

# def sumnums(num1, num2=0):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(res)
#
#
# sumnums(205,45)
# sumnums(445)

# def sumnums(num2=0, num1=9):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(res)
#
#
# sumnums(205,45)
# sumnums(445)

""" functions and restrict input """


# def sumnums(num1, num2):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(res)
#
#
# sumnums(205,45)
# sumnums('Ahmed', 'Ali')
# sumnums('Ahmed', 10)


# def sumnums(num1: int, num2: int):  # function --> way of documentation
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(res)
#
#
# sumnums(205, 45)
# sumnums('Ahmed', 'Ali')
# sumnums('Ahmed', 10)

""" manual validation """

# num = input("please enter number : ")  # always return with string
# print(num, type(num))
# print(isinstance(num, int))
# print(num.isdigit())
""" check value in the string """
# if num.isdigit():
#     num = int(num)


#
# print(isinstance('ahmed', int))  # check the value from the given type
# def sumnums(num1: int, num2: int):
#     if isinstance(num1, int) and isinstance(num2,int):
#         print(f"num1={num1}, num2={num2}")
#         res = num1 + num2
#         print(res)
#     else:
#         print("=== not valid input ")
#
#
# sumnums(205, 45)
# sumnums('Ahmed', 'Ali')
# sumnums('Ahmed', 10)

""" functions with unknown number of arguments """

def askforstudents(*students):  # function accept zero or more argument. ---> *
    print(students) # tuple ?


askforstudents('Ahmed','Mohamed', 'abanoub', 'Gehad', 'Hager')
askforstudents()
askforstudents('noha')

# print("Ahmed", 'Ali', sep=' __||__ ', end='####')
# print('Noha')


""" functions with unknow keyword-arguments"""

# def introduceyourself(**info):  ## ** --> represent zero or more keyword arguments
#     print(info)
#
#
# introduceyourself(name='noha', work='iti', age=30, food ='kiwi')
# introduceyourself(fname='ahmed', lanme='mohamed')
# introduceyourself()
# introduceyourself(fullname='hager essam')
# introduceyourself('noha')

""" example """


# def introduceyourself(name, **info):  ## ** --> represent zero or more keyword arguments
#     print(info)
# #
# #
# introduceyourself(name='noha', work='iti', age=30, food ='kiwi')
# introduceyourself('',fname='ahmed', lanme='mohamed')
# introduceyourself("fdf")
# introduceyourself(fullname='hager essam')
# introduceyourself('noha')

""" example """

# def calculator(opertion, *args):
#     res = 0
#     if opertion=='+':
#         for item in args:
#             res += item
#
#     print(res)
#
# calculator('+',4,6,78,34)

"""  ====> """
# l = [3,4,56,545]
# l.sort(reverse=True)


# temp = 'My name is {username}, I lives in {usercity}  {0}'
#
# print(temp.format('cloud', username='ahmed', usercity='cairo'))























