
""" unlabeled data """
# info = ['noha',30 , 'iti', 'cairo']

# print(info)

""" datatype - -> labeled data 
    
    dict ---> comma seperated key:value pair
    
    doesn't allow key duplication  
    from python 3.7 000> dict is sorted datatype 
    dict is mutable 
"""
"""1- define a dict """
d = {
    "name":'noha', 'track':'cloud', 'age':30, 'name':'Noha Shehab'}

print(d)

"2- get len "
print(len(d))


""" 3- access element using key"""
print(d['name'])
d['name']='Ahmed'
print(d)
d['city']='Cairo' ### if key doesn't exists will add it
print(d)

"""4- loop over the dict """

# for item in d:  # ---> item --> represent key
#     print(item)

# for item in d:  # ---> item --> represent key
#     print(item, d[item])

"""5- check item exists in the dict  """
print('Ahmed' in d )  # in check if the value exists in the keys


"""6- get dict keys"""
d_keys =d.keys()  # keys in dict_keys object --> can be casting to list or tuple
print(d_keys)
d_keys = list(d_keys)

"""6- get dict values"""
d_values =d.values()  # keys in d_values object --> can be casting to list or tuple
print(d_values)
d_values = list(d_values)

"""7- get dict item"""
d_items =d.items()  # keys in dict_items object --> can be casting to list or tuple
print(d_items)
d_items = list(d_items)

for key, value in d.items():
    print(f"key={key}, value = {value}")


"8- update dict "

info= {
    "name":"Ahmed",
    "track":'cloud'
}
track_info = {
    "intake":43,
    'branch':"smart",
    'name':"Radwa"
}

info.update(track_info)
print(info)


"""9- clear dict """
info.clear()
""" 10- pop value from the dict """
# popped_element = d.pop('name')
# print(popped_element)

"""11- delete element from dict """
# del d['track']

""" cast dict to list """

# d_list = list(d)
# print(d_list)

d_list =list( d.items())
print(d_list)