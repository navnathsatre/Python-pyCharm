import numberword


print("__name__ value for this file: ", __name__)
print("__name__ value for numberword: ", numberword.__name__)

usrInput = input("Enter any number:")
numberword.printNumberToWord(int(usrInput))