"""
   list ---> based on sequence
   mutable data
   can hold different data from datatypes

"""
"1- to define list"
l =[]
mylist= list([])
print(l , mylist)
myl = ['Ahmed', True, 'iti', 3.14, mylist, 'python', 'cloud',34,56]
print(myl)
"1- get no of elements "
print(len(myl))
"2-access list elements using index --> start from zero"
print(myl[2])
print(myl[2:6])
print(myl[-1])
print(myl[::])
print(myl[::-1])
"""3- list concat, interpolation"""
l = ['terraform', 'jenkins','node js']
l2 = ['admin2', 'admin3', 'GCP', 'docker',99, 'iti', 'iti', 'iti']
l3 = l + l2
print(l3)
"""4- extend a list """
l.extend(l2) # modify l itself
print(l)
"""5- modifying operations-=-> mutable """
# l[5]='Google cloud platform'
# print(l)
print(l[7])
l[7]='Nada'
# l[50]='Google cloud platform' #  list assignment index out of range
# print(l)

"""6- append element to the list  """
l.append('noha')
print(l)

""" 7- insert element in the list """
l.insert(4, [5,'iti'])
print(l)

l[4].append('added value')
print(l)

ll = []
l.append(ll)
print(l)
l[-1].append('Sherif')
print(l)
print(l[4][2])

"""8- pop element from the list """
popped_elemnt = l.pop()
print(popped_elemnt)
""" 9- pop element at certain index"""
popped_elemnt = l.pop(4)
print(popped_elemnt)
""" 10- remove element from the list """
print(l)
l.remove('iti')  # remove first occurrence of the element
print(l)

"""11- remove all elements from the list """
# l.clear()
'12 check if the element exists in the list '
print('iti' in l)
#
'13-count not of occurrence of element in the list '
print(l.count('iti'))
'14- get index of element in the list'
print(l.index('iti'))
'15- loop over the list '
for element in l:
    print(f"element = {element}")

"""16- sort list --->list elememts must be from same type """
""" comparing in python ---> compared parts must be from the same type """
# l = [334,45,6,39,-845,89347]
# # l.sort()  # sort list itself
# # print(l)
# l.sort(reverse=True)  # sort list itself
# print(l)
# l = ['noha', 'Ahmed', 'ali', 'test']
# l.sort()
# print(l)
"17- reverse the list -"
l = ['ahmed', True, 34,45.4]
l.reverse()
print(l)

"""18- cast string to a list """
name ='noha'
name =list(name)
print(name)

"19- min , max list "
x = [5,66,77]
print(min(x))

"""20- split string """
sentense = 'My name is noha'
sentense = sentense.split(' ')
print(sentense)







