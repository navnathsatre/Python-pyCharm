
# pyPickleRead.py
import pickle

fh = open("TeamList", "rb")

contents = pickle.load(fh)

fh.close()

print("Contents: ",contents)
print("Type of Contents: ", type(contents))

# Serialization - Deserialization
# Marshal - Unmarshal
# COM - DCOM