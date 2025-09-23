class Employee:
    def __init__(self, id, name, department, salary, bonus):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary
        self.bonus = bonus
        self.net_sal = salary + bonus

class Company:
    def __init__(self):
        self.employee = []

    def add_employee(self, new_employee):
        self.employee.append(new_employee)

    def all_net_sal(self):
        total = 0
        for emp in self.employee:
            total += emp.net_sal 
        return total
    
    def lowest_sal(self):
        min_salary = min(emp.salary for emp in self.employee)
        emp_list = []
        for emp in self.employee:
            if emp.salary == min_salary:
                emp_list.append(emp.name)
        return emp_list
    
    def bonus_morethan_1200(self):
        count = 0
        for emp in self.employee:
            if emp.bonus >= 1200000:
                count+=1
        return count

    def print_sorted_employees(self):
        sorted_emps = sorted(
            self.employee,
            key=lambda emp: (emp.department, -emp.id)
        )
        print("- Danh sach nhan vien sap xep theo phong ban: ")
        for emp in sorted_emps:
            print(f"> {emp.department} - ID: {emp.id} - Name: {emp.name} - Salary={emp.salary} - Net={emp.net_sal}")

if __name__ == "__main__":
    # make a list of information in a company
    company = Company()
    
    company.add_employee(Employee(1, "Quang", "HR", 10000000, 5000000))
    company.add_employee(Employee(2, "Bach", "IT", 6000000, 1400000))
    company.add_employee(Employee(3, "Cuong", "Finance", 5500000, 700000))
    company.add_employee(Employee(4, "Dan", "Marketing", 5200000, 600000))
    company.add_employee(Employee(5, "Phat", "Automatic", 4500000, 400000))
    company.add_employee(Employee(6, "Phi", "IT", 6800000, 185000))
    company.add_employee(Employee(7, "Trung", "Sales", 4500000, 500000))
    company.add_employee(Employee(8, "Phuc", "IT", 7300000, 2000000))
    company.add_employee(Employee(9, "Thu", "Finance", 9200000, 4000000))

    # question a: sum of all employees' net salary
    print(f"- Tong luong cong ty: {company.all_net_sal()}\n")

    # question b: list of employees' lowest salary
    print(f"- Nhan vien co luong co ban thap nhat: {company.lowest_sal()}\n")

    # question c: number of employees who has bonus more than 1200000
    print(f"- So luong nhan vien co thuong nhieu hon 1200000: {company.bonus_morethan_1200()}\n")
    
    # question d: print the list of employees ordered by department and -name
    company.print_sorted_employees()
