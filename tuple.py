"""
   tuple ---> based on sequence
   immutable data  --> once created cannot be change
   can hold different data from datatypes

"""
"1- to define tuple"
t =()
mytuple= tuple([])
print(t , mytuple)
myt = ('Ahmed', True, 'iti', 3.14, mytuple, 'python', 'cloud',34,56)
print(myt)
"1- get no of elements "
print(len(myt))
"2-access tuple elements using index --> start from zero"
print(myt[2])
print(myt[2:6])
print(myt[-1])
print(myt[::])
print(myt[::-1])
"""3- tuple concat"""
t= ('terraform', 'jenkins','node js')
t2 = ('admin2', 'admin3', 'GCP', 'docker',99, 'iti', 'iti', 'iti')
t3 = t + t2
print(t3)


'4- check if the element exists in the tuple '
print('iti' in t2)
# #
'5-count not of occurrence of element in the tuple '
print(t2.count('iti'))
'6- get index of element in the tuple'
print(t2.index('iti'))
'7- loop over the tuple '
for element in t2:
    print(f"element = {element}")

#
"""8- cast string to a tuple """
name ='noha'
name =tuple(name)
print(name)
#
"9- min , max tuple "
x = (5,66,77)
print(min(x))
#

"10 - tuple of one item "
students = ('Radwa',)
print(students, type(students))

'11-cast list to tuple or vise versa'

# l = [4,5,6,True, 'Abanoub', 32.34]
# t = tuple(l)
# print(t)
#
# myl = list(t)

""" generate list of numbers from 0 --> """

# r = range(10)
# r= range(0,11, 2)
r =range(100, 0,-10)
print(r) # iterable object


for i in r:
    print(f"i={i}")


l = list(r)
print(l)


""" ask user to enter something """
num = input('please enter num: ')  # always returns with string
print(num, type(num))