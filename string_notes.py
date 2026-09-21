# CG, string notes 
first_name = "Carrera"
last_name = "Galata"
#concatenation => add two strings together
name= first_name + " " + last_name
print(f"{name} told the class you can\'t drive my car.")

user = input("Please tell me your name:\n").strip().title()

print(f"New user recongized\nWelcome {user}")

sentence = "The quick brown fox jumped over the lazy dog"
print(f"The sentence is {len(sentence)} characters long.")

print(sentence)
print(sentence.replace("dog", "cat"))
print(sentence.replace("dog", name))







