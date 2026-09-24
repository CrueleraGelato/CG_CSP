# CG, Password strength checker 
password = input("What is your password?").strip()

character = "False"

Uppercase = "False"

lowercase = "False" 

number = "False" 

symbol = "false" 

length = len(password)

rules_met = True 

symbols = "!@#$%^&*()"

if len(password) >= 8: 
    length = True 
print(f"At least 8 characters: {length}")

for letter in password: 
    if letter.isupper(): 
         Uppercase = True 
print(f"Your passwords Uppercase: {Uppercase}")

for letter in password: 
    if letter.islower():
         lowercase = True 
print(f"Your passwords Lowercase: {lowercase}")

for letter in password: 
    if letter.isnumeric():
         number = True 
print(f"Your passwords Number: {number}")

if letter in symbols:
         symbols = True 
print(f"Your password has symbols: {symbols}")

if length is True: 
     requirement_met=1

if Uppercase: 
     rules_met+= 1 
if lowercase: 
     rules_met+=1 

     
     

     


     
     



     









