class Student:
    def __init__(self, name, math, lite):
        self.name = name
        self.math = math
        self.literature = lite
        self.average = (self.math + self.literature) / 2
    
    def classification(self):
        if self.average >= 9:
            return 'xuat sac'
        elif self.average >= 8:
            return 'gioi'
        elif self.average >= 6.5:
            return 'kha'
        elif self.average >= 5:
            return 'trung binh'
        elif self.average >= 3.5:
            return 'yeu'
        elif (self.average >= 0) & (self.average <3.5):
            return 'kem'
        else:
            return 'wrong input'
        
if __name__ == "__main__":
    name = input('Ten hoc sinh: ')
    math = int(input('Diem toan: '))
    lite = int(input('Diem van: '))

    student = Student(name, math, lite)
    print(f"Diem trung binh cua {student.name} la {student.average} - Xep loai {student.classification()}")

    