# Password generator
# Upper, lower, numbers, symbols and varying lengths
import secrets, os , random , string

# pw_length = 13
# print(secrets.token_urlsafe(pw_length)) # No characters

def generate(pw_length):
    chars = string.ascii_letters + string.digits + '~`!@#$%^&*()_-+={[}]|\\:;\"\'<,>.?/'
    random.seed(os.urandom(1024)) # seeding the random number generator with 1024 bytes of random data
    return ''.join(random.choice(chars) for i in range(pw_length))

try:
    pw_length = int(input("Enter password length: "))
    if pw_length <= 0:
        print("Not a valid password length.")
    else:
        print(generate(pw_length))
except ValueError:
    print("Not a number")