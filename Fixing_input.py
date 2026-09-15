# CG, Fixing inputs 

# When you want a specific input 
while True: 
        color = input("tell me a color that is only one word: ").lower().strip()   
        if color.isnumaric():
            print("Sorry that is a number")
        elif " " in color:
             print("I said one word") 
        else:
             break

print(f"I painted your walls {color}!")

# when you want a number 
while True: 
    try: 
        age = int(input("How old are you: "))
        break 
    except: 
        print("that isn't a number")

print(f"wow you are {age} that is really old!") 
