import os

print(os.getcwd())

# os.mkdir("test")

if os.path.exists("test"):
    print("Directory already exists")
else:
    os.mkdir("test")