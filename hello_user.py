# CG, hello user

while True:
    name = input("Tell me your name: ").title().strip()         
    if name.isnumeric(): 
        print("sorry that is not a name") 
    else: 
        break
print(f"Hello {name}, that is a beautiful name")
    