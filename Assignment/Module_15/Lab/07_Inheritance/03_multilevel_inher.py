class studnet:
    def get_student(self):
        self.name = input("Enter the student name:")
        self.roll = int(input("Enter the student roll number:"))

class mark:
    def get_marks(self):
        self.m1 = int(input("Enter the marks of subject 1:"))
        self.m2 = int(input("Enter the makrs of sunject 2:"))

class result(studnet,mark):
    def display(self):
        total = self.m1 + self.m2
        print("\nStudnet name:",self.name)
        print("Roll Number:",self.roll)
        print("Total marks:",total)

r = result()

r.get_student()
r.get_marks()
r.display()