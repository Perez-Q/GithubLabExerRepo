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
