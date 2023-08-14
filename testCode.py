

mySentence = 'loves  the color'
color_list = ['red','blue','teal','black','green','pink']

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{0} {1} {2}".format(name,mySentence,i)
        lst.append(msg)
    return lst



def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print('You need to provide your name')
        elif name == 'Sally':
            print('Sally you dont use this')
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()

import random

def random_number():
    print(random.randrange(1,123))

random_number()


name_list = ['John', 'Tom', 'Haley', 'Maddie', 'Tim', 'Jim']
firstSentence = 'is my friend'

def name_function():
    bst = []
    for i in name_list:
        frnd = "{} {}".format(i, firstSentence)
        bst.append(frnd)
    return bst

bst = name_function()

# Using count() method
name_to_count = 'Jim'
count_jim = bst.count("{} {}".format(name_to_count, firstSentence))
print("Count of '{}': {}".format(name_to_count, count_jim))

# Using sort() method
bst.sort()
print("Sorted list:")
for i in bst:
    print(i)



square = lambda x: x * x
print(square(3))



def format_string(string, data):
    try:
        formatted_string = string.format(**data)
        return formatted_string
    except KeyError as e:
        missing_key = str(e).strip("'")
        raise KeyError(f"Key '{missing_key}' not found in the data dictionary.")
    except Exception as e:
        raise Exception("An error occurred while formatting the string: " + str(e))

# Example usage:
template = "Hello {name}, you are {age} years old and your favorite color is {color}."
data = {"name": "John", "age": 30, "color": "blue"}

formatted_result = format_string(template, data)
print(formatted_result)



def getSum(num1,num2):
    answer = num1 + num2
    print("The anwser is {}.".format(answer))

myAdd = getSum
myAdd(2,4)

