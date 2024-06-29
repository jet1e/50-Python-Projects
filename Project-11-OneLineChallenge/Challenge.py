# Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.
# For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].
# USING A SINGLE LINE OF CODE IN FUNCTION
# Source: https://stackoverflow.com/questions/3590165/how-can-i-convert-each-item-in-the-list-to-string-for-the-purpose-of-joining-th

def convert(l):
    return [str(x) for x in l] # Converts current element x, to a string. The for loop iterates through the list element. "[]" will create a new list to be returned

print(convert([1, 2, 3, 4]))