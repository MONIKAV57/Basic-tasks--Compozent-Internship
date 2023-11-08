import string
import random
import secrets

print("---RANDOM PASSWORD GENERATOR---\n")

letters=string.ascii_letters
digits=string.digits
special_chars=string.punctuation
selection_list=letters+digits+special_chars

passwordLen=10

password=''
for i in range(passwordLen):
    password+=''.join(secrets.choice(selection_list))
print("Your Random Password Generated Is :\n",password)
