""" lexical scope --> access variable """
"1- global"
# name = 'Noha'  # globally --> can be accessed any where in the script
#
# print(name)

"2- print / read global variable value from inside the function "
# name = 'Ahmed'
#
# def sayHello():
#     print(f"Hello {name}")
#
# sayHello()

""" 3- modify global variable from inside the function """
#
# name = 'Ali'
#
# def modifyname():
#     name= 'Mohamed'  # create new local variable
#     print(name)
#
# print("--------------- after the function ----------")
# modifyname()
# # print(name)


# l = []

# def append_to_list():
#     l=[]
#     item = input("please enter element : ")
#     l.append(item)
#
# append_to_list()
# append_to_list()
# append_to_list()
# print(l)


""""""""""""""""""
# name = 'Ahmed'
# newval=name[2].upper()
# print(name)
# print(newval)
# name+='Ahmed'  # name=name+'Ahmed'  # reassign
# print(name)
#
#
# l= []
# l.append("trret")
# print(l)
# l.append('noha')
# print(l)
# print(l.sort())
# # print(l)
# print(sorted(l))

""" """
# name = 'Ali'

# def modifyname():
#     name= 'Mohamed'  # create new local variable  can be accessed only inside the function
#     print(name)
#
# modifyname()
# print(name)
""" modify global variable from inside a function """
#
# name = 'Ali'
#
# def modifyname():
#     global name
#     name='Mohamed'
#     print(name)
#
# modifyname()
# print(name)



""" example """
#
# port = 3306
#
#
# def connect_to_mysql():
#     global port
#     try:
#         connection = input('please enter values')
#         connection = int(connection)+port
#     except:
#
#         port = 3308
#
# connect_to_mysql()
# print(port)


#
# no_of_calls = 0
#
# def connect_to_db():
#     global no_of_calls
#     print("--- connection is being established to the database ")
#     no_of_calls+=1
#     print(f"this is the {no_of_calls} th call of the function ")
#
#
# connect_to_db()
# connect_to_db()


"""------------------------define function inside a function --------------------------------"""

# def outerfunction():
#     course ='python'  # local variable
#     print(f"from the outer function course= {course}")
#     """ local variable can be accessed anywhere in the function or inner function """
#     def innerfunction():
#         print(f"from the inner function course= {course}")
#
#     innerfunction()
#
#
# outerfunction()
"""  """
# def outerfunction():
#
#     def innerfunction():
#         course = 'python'  # new local variable for the innerfunction
#         print(f"from the inner function course= {course}")
#
#     innerfunction()
#     print(f"from the outer function course= {course}")
#
# outerfunction()
""" modify local variable from inner function """

# def outerfunction():
#     course = 'python'
#     def innerfunction():
#         course = 'Terraform'  # new local variable for the innerfunction
#         print(f"from the inner function course= {course}")
#
#     innerfunction()
#     print(f"from the outer function course= {course}")
#
# outerfunction()


"""  """
# def outerfunction():
#     course = 'python'
#     def innerfunction():
#         nonlocal course
#         course = 'Terraform'  # new local variable for the innerfunction
#         print(f"from the inner function course= {course}")
#
#     innerfunction()
#     print(f"from the outer function course= {course}")
#
# outerfunction()

""""""
name = 'Ahmed'

def outerfunction():
    course = 'python'
    def innerfunction():
        nonlocal course
        global name
        course = 'Terraform'  # new local variable for the innerfunction
        print(f"from the inner function course= {course}")
        name = 'Ali'

    innerfunction()
    print(f"from the outer function course= {course}")

outerfunction()
print(name)


































