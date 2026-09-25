# CG, Loop Notes 
import random 
# code that will repeat over and over again 
count = 1 

while count <= 10: 
    print(count) 
    count += 1

goose = random.randint(1,10)
ducks = 1

while True: 
    print("duck") 
    if ducks == goose: 
        break 
    ducks += 1 
print("GOOSE!!!!")

siblings = ["Aprilia", "Rossi"]

print(siblings[1]) 
print(siblings) 
#add to th list 
item = input("what needs to be added to the list:")
siblings.append("Leonardo")
siblings.insert(1,"Carrera")
#remove from list 
print(siblings)
print(siblings.pop(1)) 
print(siblings) 

# For loops 
for number in range(1,11,2): 
    print(number)

for sibling in siblings: 
    print(sibling + " Galata") 