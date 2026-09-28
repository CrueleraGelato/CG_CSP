# CG, number information 
number = 0 
for number in range (1,21):  
    if number % 2 == 0: 
        print(f"{number} is even")
        if number % 5 == 0: 
            print(f" {number} is divisable by 5")
        else: 
            print(f"{number} is not divisable by 5")
    else: 
        print(f"{number} is odd")
        if number % 5 == 0: 
            print(f"{number} is divisable by 5")
        else: 
            print(f"{number} is not divisable by 5")

    
        
    


