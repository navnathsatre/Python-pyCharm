# kwargs ==> Dictionary

def printStudentDetails(**kwargs):
    print("kwargs: ", kwargs)
    print("type(kwargs) : ", type(kwargs))
    print("id(kwargs): ", id(kwargs))
    # print("Student Details: Name: {}, Age: {}, Marks: {}, Stream: {}".format(
    #     kwargs['name'], kwargs['age'], kwargs['marks'], kwargs['stream']
    # ))


# printStudentDetails(name="Mary", age=15, marks=500, stream="CSE")

d = {"name": "John", "stream": "ECE", "age": 17, 'marks': 700}
print("id(d): ", id(d))
printStudentDetails(**d)
