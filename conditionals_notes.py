# CG, Conditonals notes 

military_time = 900

if military_time <600: 
    print("It is to early why are you awake")      
elif military_time < 900: 
    print("Good Morning!")
elif military_time < 1200: 
    print("Good morning you should be at school") 
elif military_time < 1700:
    print("Good afternoon") 
else: 
    print("Good evening")

# nesting conditionals 
day = "saturday" 
time = 900 

if time > 900 and time < 1600:
    if day != "saturday" or day != "sunday":
        print("you should be at school") 
    else: 
        if time > 1200: 
            print("Good afternoon") 
        else: 
            print("Good Morning") 
else: 
    print("You are not required to be at school") 
