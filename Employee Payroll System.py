import csv
from tabulate import tabulate

class Employee:
    def __init__(self, emp_id, name, salary, deductions=0, bonuses=0):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.deductions = deductions
        self.bonuses = bonuses

    def calculate_pay(self):
        net_pay = self.salary + self.bonuses - self.deductions
        return net_pay

class PayrollSystem:
    def __init__(self):
        self.employees = []
        self.load_employees()

    def load_employees(self):
        try:
            with open('employees.csv', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    emp_id, name, salary, deductions, bonuses = map(str.strip, row)
                    self.employees.append(Employee(int(emp_id), name, float(salary), float(deductions), float(bonuses)))
        except FileNotFoundError:
            pass

    def save_employees(self):
        with open('employees.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Employee ID", "Name", "Salary", "Deductions", "Bonuses"])
            for employee in self.employees:
                writer.writerow([employee.emp_id, employee.name, employee.salary, employee.deductions, employee.bonuses])

    def add_employee(self):
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Employee Salary: "))
        deductions = float(input("Enter Deductions (if any): "))
        bonuses = float(input("Enter Bonuses (if any): "))
        
        employee = Employee(emp_id, name, salary, deductions, bonuses)
        self.employees.append(employee)
        self.save_employees()

    def update_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                name = input("Enter new Employee Name (press Enter to skip): ")
                salary = float(input("Enter new Employee Salary (press Enter to skip): ") or employee.salary)
                deductions = float(input("Enter new Deductions (press Enter to skip): ") or employee.deductions)
                bonuses = float(input("Enter new Bonuses (press Enter to skip): ") or employee.bonuses)
                
                employee.name = name
                employee.salary = salary
                employee.deductions = deductions
                employee.bonuses = bonuses
                self.save_employees()
                break
        else:
            print("Employee not found!")

    def print_employees(self):
        if not self.employees:
            print("No employees found.")
        else:
            employee_data = [
                ["Employee ID", "Name", "Salary", "Deductions", "Bonuses", "Net Pay"]
            ]
            for employee in self.employees:
                employee_data.append([employee.emp_id, employee.name, employee.salary, employee.deductions,
                                      employee.bonuses, employee.calculate_pay()])
            print(tabulate(employee_data, headers="firstrow", tablefmt="fancy_grid"))

# Example usage
payroll_system = PayrollSystem()

while True:
    print("\nOptions:")
    print("1. Add Employee")
    print("2. Print Employees")
    print("3. Update Employee")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        payroll_system.add_employee()
    elif choice == "2":
        payroll_system.print_employees()
    elif choice == "3":
        emp_id = int(input("Enter Employee ID to update: "))
        payroll_system.update_employee(emp_id)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
