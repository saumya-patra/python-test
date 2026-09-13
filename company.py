from employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        if isinstance(new_employee, Employee):
            self.employees.append(new_employee)
        else:
            raise ValueError("Only Employee instances can be added.")

    def display_employees(self):
        for emp in self.employees:
            print(f"{emp.fname} {emp.lname}, Salary: {emp.salary}")

    def pay_employees(self):
        for emp in self.employees:
            paycheck = emp.calculate_paycheck()
            print(f"Paying {emp.fname} {emp.lname}: ${paycheck:.2f}")

def main():
    my_company = Company()
    emp1 = Employee("John", "Doe", 52000)
    emp2 = Employee("Jane", "Smith", 60000)

    my_company.add_employee(emp1)
    my_company.add_employee(emp2)

    print(my_company.employees)  # Should print the list of employees
    my_company.display_employees()  # Display employee details
    my_company.pay_employees()  # Pay employees and display paycheck amounts

main ()