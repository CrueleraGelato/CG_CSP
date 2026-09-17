# CG, your budget

income = float(input("What is your monthly income?"))

rent = float(input("How much is your monthly morgage?"))

utilities = float(input("What is your monthly utilities?"))

groceries = float(input("What is your monthly money spent on groceries?"))

transportation = float(input("What is your monthly transportation cost?"))

savings = float((income/10))  

spending = float()

print(f"Your rent is {rent} and that is {int(rent/income*100)} of your income") 

print(f"Your utilities is {utilities} and that is {int(utilities/income*100)} of your income") 

print(f"Your groceries is {groceries} and that is {int(groceries/income*100)} of your income") 

print(f"Your transportation is {transportation} and that is {int(transportation/income*100)} of your income") 
 
print(f"You should save {savings} that is 10% of your income") 


    




