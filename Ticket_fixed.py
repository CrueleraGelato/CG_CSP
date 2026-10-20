# CG, Ticked fixed 

age = int(input("Enter your age: "))
matinee = input("Is this a matinee? (yes/no): ").lower()

if age < 5:
    price = 0
elif age < 12:
    price = 8
elif age < 65:
    price = 12
elif age < 65:
    price = 12
elif 12 < age < 65:  
    price = 9
if not isinstance(age, int):
    print("That is not a number try again")

if price == -3: 
    price = 0 
if matinee == "yes":
    price = price - 3

print(f"Ticket price: ${price}")