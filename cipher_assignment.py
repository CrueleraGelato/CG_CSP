# CG, Cipher assignment 
choice = input("Would you like to encrypt or decrypt a message?").strip()
message = input("Enter your message:").strip()
shift = int(input("Enter shift amount:").strip())


def caesar_shift(message,shift):
   result = ""
   for char in message:
       if char.isupper():
                   result += chr((ord(char)- ord ("A") + shift)% 26 + ord("A"))
       elif char.islower():
                   result += chr((ord(char)- ord ("a") + shift)% 26 + ord("a"))
       else:
               result += char
   return result


if choice == "E":
   result = caesar_shift(message, shift)
   print(f"Your encrypted message is: {result}")


elif choice == "D":
   result = caesar_shift(message, -shift)
   print(f"Your decrypted message is: {result}")








