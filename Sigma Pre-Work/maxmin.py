import json


def maxmin(list):
    '''
    Takes a list of integers and iterates through it to find the maximum and minimum values.
    max and min variables assigned to first item in list allows handling of -ve values
    Returns list [minimum, maximum]
    '''
    try:
        max = list[0]
        min = list[0]
        for int in list:
            if int > max:
                max = int
            elif int < min:
                min = int
    except (TypeError):
        print("All list items must be integers.")
    return [min, max]


def string2list(string):
    '''Takes list formatted string and returns the list'''
    try:
        return json.loads(string)
    except:
        print("Invalid entry, example entry: [5, 4, 3, 1]")


# print(maxmin([2, 4, 1, 0, 2, -1]))
input = string2list(input("Enter list [x, y, z]: "))
print(maxmin(input))
