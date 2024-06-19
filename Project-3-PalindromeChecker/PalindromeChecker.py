# Palindrome checker
def isPalindrome(string):
    reversed_string = string [::-1] # read the string backwards
    if reversed_string == string:
        print("\"{}\" IS a palindrome".format(string))
    else:
        print("\"{}\" IS NOT a palindrome".format(string))

to_check = str(input("Enter a phrase to check if it is a palindrome: ")) # Convert to a string - ensures phrases and int can be checked
isPalindrome(to_check)