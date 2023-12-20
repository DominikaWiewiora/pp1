class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __repr__(self):
        if self.age >= 18:
            return f"{self.surname.upper()}{self.name[0].upper()}{self.seniority}"
        else:
            return f"{self.surname.lower()}{self.name[0].lower()}{self.seniority}"


employee1 = C("Anna", "May", 17, 7)
print(repr(employee1)) 

employee2 = C("George", "Brown", 21, 4)
print(repr(employee2)) 
