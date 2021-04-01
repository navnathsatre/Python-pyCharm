fh = open("FileExample.txt") # default mode is read mode

strContents = fh.read()

fh.close()

print("File Content: ", strContents)
print("Type of strContents: ", type(strContents))