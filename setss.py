

"""non primitive datatype can hold different values from different data types
    --> datatype ---> remove duplicates in values
    --> unordered datatype
    --> items are added randomly --> no index
    --> set is mutable
"""

"1- define a set "
mys = set()
s = {"Ahmed", 'Mohamed',335, 'iti', True , 'iti', 'noha'}
print(s)

"2- get len "
print(len(s))

"3- add element to the set"
s.add('added element')
print(s)

"""4- pop element in the set """
popped_element = s.pop()
print(popped_element)
print(s)

"""5- remove the element """
# s.remove('Ahmed')
# print(s)

""" 6- check if element exists or not """
print('ahmed' in s)

""" 7- loop over the set """
for element in s:
    print(element)

""" update set """
courses ={"terraform", 'jenkins', 'docker', 'python'}
developmentcourse = {"python", 'node', 'java'}
courses.update(developmentcourse)
print(courses)


""" sets   """
# s = {"Ahmed", 'Mohamed',335, 'iti', True , 'iti', 'noha', ('Gamal', 'Sherif')}
# print(s)
# s = {"Ahmed", 'Mohamed',335, 'iti', True , 'iti', 'noha', {'Gamal', 'Sherif'}}
# print(s)
# s = {"Ahmed", 'Mohamed',335, 'iti', True , 'iti', 'noha', ['Gamal', 'Sherif']}
# print(s)
# s = {"Ahmed", 'Mohamed',335, 'iti', True , 'iti', 'noha', {'name':'Gamal'}}
# print(s)