#using a loop

string = input("Enter a string: ")

reversed_string = ""

for char in string:
    reversed_string = char + reversed_string  # add current character before 

print("Reversed string:", reversed_string)

