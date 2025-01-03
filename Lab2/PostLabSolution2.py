file = open("Members")
lines = 0
inputs = []

content = file.read() 
colist = content.split("\n") #splits the text file of the condition "Enter key" a list

for i in colist:
    lines+=1
    inputs.append(i) #the string are then appended to the list
    
print("The numbers of lines in the code:", lines)
print("The words", inputs)

while True:
    print(f"The file contains {lines} lines.")
    try:
        line_number = int(input("Enter a line number (0 to quit): "))

        if line_number == 0:
            print("Exiting the program.")
            break
        elif 1 <= line_number <= lines:
            print(f"Line {line_number}: {inputs[line_number - 1]}")
        else:
            print(f"Please enter a number between 1 and {lines}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
