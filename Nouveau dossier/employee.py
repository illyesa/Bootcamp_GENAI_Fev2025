class Employee:
    number_employees = 0
    def __init__(self, firstname, lastname, age, job, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary
        Employee.number_employees += 1

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"

    def happy_birthday(self):
        self.age += 1
        return self.age

    def get_promotion(self, promotion_amount):
        self.salary += promotion_amount

    def show_info(self):
        print(f"Name: {self.get_fullname()}, Age: {self.age}, Job: {self.job}, Salary: {self.salary}")

# Creating Employee objects
lea = Employee("Lea", "Smith", 30, "Developer", 25000)
david = Employee("David", "Schartz", 20, "Project Manager", 20000)

# Displaying their attributes
lea.show_info()
david.show_info()

# Calling methods
print(lea.get_fullname())
print(david.happy_birthday())
david.get_promotion(5000)
david.show_info()

class Developer(Employee):
    def __init__(self, firstname, lastname, age, job="Developer", salary=15000):
        super().__init__(firstname, lastname, age, job, salary)
        self.coding_skills = []

    def add_skills(self, *skills):
        self.coding_skills.extend(skills)

    def coding(self):
        print(f"{self.get_fullname()} knows {', '.join(self.coding_skills) if self.coding_skills else 'no programming languages yet'}.")

    def coding_with_partner(self, other_developer):
        print(f"{self.get_fullname()} and {other_developer.get_fullname()} know {', '.join(set(self.coding_skills + other_developer.coding_skills))}.")

    def get_promotion(self, promotion_amount):
        self.salary *= promotion_amount

# Creating Developer objects
tom = Developer("Tom", "Cruiz", 30)
angelina = Developer("Angelina", "Jolie", 23)

tom.show_info()
angelina.show_info()

# Adding skills
tom.add_skills("Python", "JavaScript")
angelina.add_skills("Java", "C++")

tom.coding()
angelina.coding()

tom.coding_with_partner(angelina)

tom.get_promotion(2)
tom.show_info()

class Manager(Employee):
    def __init__(self, firstname, lastname, age, job="Manager", salary=15000):
        super().__init__(firstname, lastname, age, job, salary)
        self.employees = []

    def add_new_employee(self, new_employee):
        self.employees.append(new_employee)

    def show_employees(self):
        print(f"{self.get_fullname()} manages: {', '.join([emp.get_fullname() for emp in self.employees])}")

# Creating Manager object
brad = Manager("Brad", "Pitt", 50)
brad.show_info()

# Adding employees under the manager
brad.add_new_employee(lea)
brad.add_new_employee(david)

brad.show_employees()
print(Employee.number_employees)

#pip install pandas
