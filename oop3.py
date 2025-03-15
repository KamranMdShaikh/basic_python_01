class School:
    school_name = "Rangpur Zila School"
    
    def __init__(self, name, age = "12"):
        self.student_name = name
        self.student_age = age


sc1 = School("Rahim")
print(sc1.school_name)
print(sc1.student_name)
print(sc1.student_age)


sc1.school_name = "DRMC, Dhaka"
print(sc1.school_name)
print(sc1.student_name)
sc1 = School( name = "Karim", age = "15")
print(sc1.student_age)