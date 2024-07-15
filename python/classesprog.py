class student:
    rollno=int(input("Enter the rollno: "))
    name=input("Enter the Name of the Student:")
    marks=int(input("Enter the marks: "))
    print(rollno,name,marks)

    def coder(this):
        print(this.name,"is a good coder")
object=student()
object.coder()
print(student.mro())