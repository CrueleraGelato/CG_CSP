# CG, reading and writing to files notes

with open('CG_CSP\CG_CSP\practice.txt',"r+") as file:       
    content = file.read()
    print(content)
    word = content.find("Rhysand")
    length = len("Rysand")
    content += " Carrera+Rhysand"
    file.write(content)

with open("CG_CSP\CG_CSP\practice.txt", "a") as file: 
    file.write("hello")

