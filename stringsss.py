"""
    string is immutable datatype ===> cannot not be changed after creation

"""

iti = 'information Technology institute'
"1- get no of chars "
print(len(iti))
"2-access string parts using index --> start from zero"
print(iti[2])
print(iti[2:7])
print(iti[-1])
print(iti[::])
print(iti[::-1])
"""3- string concat, interpolation"""
# fname ='noha '
# midname='abdelhady '
# lname= 'shehab'
# fullname= fname + midname + midname+ lname
# print(fullname)
# fullname= fname + midname*2 + lname
# print(fullname)
"""4- string format """
# temp = "My name is {0} I am studying at {1} track."
# print(temp.format('noha', 'cloud'))  # return new string
# print(temp.format('radwa', 'Cloud'))
# print(temp.format("cloud", 'Abanoub'))
temp = "My name is {username} I am studying at {usertrack} track."
print(temp)
# print(temp.format(usertrack="cloud",username= 'Abanoub'))
""" f-format string"""
# username='noha'
# usertrack='Cloud'
# temp = f"My name is {username} I am studying at {usertrack} track."
# print(temp)

"""5- string operations"""
# name = 'noha abdelhady shehab'
# l = name.lower()  # this return with new string
# print(l)
# print(name.upper())
# u =name.upper()
# print(name.capitalize())
# print(name.title())

"""6-strip string"""
# message = "               Nice to meet you                "
# print(len(message))

# newmessage= message.strip()  # remove spaces from the beginning and the end of the string
# print(newmessage, len(newmessage))

# newmessage= message.lstrip()  # remove spaces from the beginning  of the string
# print(newmessage, len(newmessage))

# newmessage= message.rstrip()  # remove spaces from the end  of the string
# print(newmessage, len(newmessage))

# message = "#            Nice to meet you               $"
# print(message)
# print(message.strip('#'))
# print(message.lstrip('# Aum$'))

"""7- examine string content"""

message = 'helloworld'
print(message.isalpha()) # Return True if the string is an alphabetic string, False otherwise. A string is alphabetic if a
num = '19.99'
print(num.isdigit())
print(num.islower())
num='                                '
print(num.isspace())



'check if the char exists in the string '
print('o' in 'NOHA')

'count not of occurrence of char in the string '
print('iti'.count('i'))
'get index of char in the string'
print('iti'.index('i'))
'loop over the string '
for char in 'information tech.':
    print(f"char = {char}")

"""9- replace string """
message = 'My name is noha I love python' ## replace o with @
print(message.replace('o', '@',1))

"328947958712"




# z = 4 + 5j # complex
#
# c = complex(4, 5)

a, b, c, d = 10, 66.66, 76.3, 100.54
# print(round(b))
# round(c)
# print(min(a, b, c, d))
# max(a, b, c, d)

print('nohaaaa   '.strip().upper())