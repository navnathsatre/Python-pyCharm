try:
    userInput = input("Enter any number: ")
    result = 100 / int(userInput)
    print("Result : ", result)
except ValueError:
    print("Please enter only numbers.")
except ZeroDivisionError:
    print("Please enter numbers greater than 0.")
except:
    print("Some exception occurred.")
