def printStudentDetails(name, age, marks, stream):
    print("Student Details")
    print("Name: {}, Age: {}, Marks: {}, Stream: {}".format(
        name, age, marks, stream
    ))


printStudentDetails("Mary", 15, 500, "CSE")
d = {"name": "John", "stream": "ECE", "age": 17, 'marks': 700}
printStudentDetails(**d)
#printStudentDetails(*d) # NOT a correct way

