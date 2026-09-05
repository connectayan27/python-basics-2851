n = 100
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    next_val = a + b
    a, b = b, next_val



class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

# Create a Student object
s1 = Student("Rahul", 100, 87.5)

# Print details
print("Name:", s1.name)
print("Roll:", s1.roll)
print("Marks:", s1.marks)
