file_read = open('test.txt',"r")
print("file is in read mode....")
print(file_read.read())
file_read.close()

file_write = open('test.txt',"w")
file_write.write("file is in write mode.... \n")
file_write.write(" hi i am phython . i am very old")

# file_write.close()

file_write = open("test.txt","r")
print(file_write.read())

file_append = open("test.txt","a")
file_append.write("\n file is in append mode....")
file_append.write("\n hi i am phython . i am very old")
file_append.close()