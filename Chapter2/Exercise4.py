class Student:
    def __init__(self, id, name, gender, math, physics, chemist):
        self.id = id
        self.name = name
        self.gender = gender
        self.math = math
        self.physics = physics
        self.chemist = chemist
        self.average = (self.math + self.physics + self.chemist) / 3
    
    def __str__(self):
        return f"{self.id} | {self.name} | {self.gender} | {self.math} | {self.physics} | {self.chemist} | {self.average}"

if __name__ == "__main__":
    n = int(input("Enter the number of student: "))
    student = []
    print("ID,Name,Gender,Math,Physics,Chemist")
    for i in range(1, n+1):
        temp = input(f'Student {i}: ')
        info = temp.split(',')
        full = Student(int(info[0]), info[1], info[2], int(info[3]), int(info[4]), int(info[5]))
        student.append(full)
    
    print("\n List of students with average point")
    for i in range(0, n):
        print(f"> {student[i]}")