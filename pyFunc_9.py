# Args

def printPlayerDetails(name, age, team):
    print("Player Details:")
    print("Name: {}, Age: {}, Team: {}".format(name, age, team))


printPlayerDetails("Virat", 33, "RCB")

msd = ("MS Dhoni", 37, "CSK")
printPlayerDetails(msd[0], msd[1], msd[2])

printPlayerDetails(*msd)

# Packing & Unpacking
# Args