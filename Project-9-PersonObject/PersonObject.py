# Person --> OOP

class Person:
    # Constructor
    def __init__(self, first_name, last_name, age, money):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.money = money 
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def change_last_name(self, new_last_name):
        self.last_name = new_last_name

    @property
    def print_info(self):
        print(self.full_name)
        print(f"{self.age} years old")
        print(f"${self.money}")

man = Person("Abdul", "Bari", 45, 1000000)
man.print_info
print(man.full_name)
man.change_last_name("BRUH")
print(man.full_name)