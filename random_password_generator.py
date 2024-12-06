import random
import string

def password_generator(lenght):

    chracters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(chracters) for i in range(length))
    return password

length = int(input("Enter the length of password you want: "))

password = password_generator(length)   

print(f"Generated password: {password}")   # print the generated password to the console.




     
    