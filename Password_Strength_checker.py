# CG, Password strength checker 
password = input("What is your password?").strip()

character = "false"

Uppercase = "False"

lowercase = "False" 

number = "False" 

symbol = "false" 

length = len(password)

if len(password) >= 8: 
    length = True 
print(f"At least 8 characters: {length}")

for letter in password: 
    if Uppercase.isupper(): 
         Uppercase = True 
print(f"Your passwords Uppercase: {Uppercase}")

for letter in password: 
    if lowercase.islower():
         lowercase = True 
print(f"Your passwords Lowercase: {lowercase}")

for letter in password: 
    if number.isnumeric():
         number = True 
print(f"Your passwords Number: {number}")

if letter in ("!@#$%^&*()_+={}[]|:;"'<.,>)
         lowercase = True 
print(f"Your passwords Lowercase: {lowercase}")







