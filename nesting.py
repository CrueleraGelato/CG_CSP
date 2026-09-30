# CG, Nesting notes
csp = ["Carrera", "Alex", "Gabe", "Elsie", "Ivan", "Masen", "William", "Selena", "Kristan", "Ainsley"]
if len(csp) > 0: 
    for student in csp: 
        print("Checking in {student}")
else: 
    print(f"There is no one in this class")

while True: 
    username = input("What is your username: ").strip() 
    password = input("What is your password: ").strip() 

    if username == "Larose4" and password == "password": 
        print("welcome to the program")
    else: 
        print("Those credentials are incorrect.")

