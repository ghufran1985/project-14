file = open("codingal.txt","r")
counter = 0

content = file.read()
coList = content.split("\n")

for i in coList:
    if i:
        counter += 1

print(f"this is the no of lines in the file : {counter}")