#File Input/Output in Python
#read file.txt
#open file.txt in read mode
file = open("file.txt", "r")
#read the file
content = file.read()
#close the file 
file.close()
#display the content of the file
print(content)
#write file.txt
#open file.txt in write mode
file = open("file.txt", "w")
#write to the file
file.write("This is a new line.\n")
#close the file
file.close()
#read file.txt
#open file.txt in read mode
file = open("file.txt", "r")
#read the file
content = file.read()
#close the file
file.close()
#display the content of the file
print(content)