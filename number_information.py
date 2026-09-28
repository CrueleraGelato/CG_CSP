# CG, number information 
number = 0 
for number in range (1,21): 
    print(number) 
    if number % 2 == 0: 
        print(f"this number is even")
        number = 1
        if number / 5 == 0: 
            print(f"this number is divisable by 5")
        else: 
            print(f"this number is not divisable by 5")
    else: 
        print(f"this number is odd")
        if number % 5 == 0: 
            print(f"this number is divisable by 5")
        else: 
            print(f"this number is not divisable by 5")

    
        
    


