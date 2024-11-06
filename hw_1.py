class Person:
    def __init__(self,fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        return (f' Меня зовут {self.fullname}, '
               f'мне {self.age}, ' 
               f'я {self.is_married}')



class Student(Person):
    def __init__(self,fullname, age, is_married, **marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def get_average(self):
        average = sum(self.marks.values())/len(self.marks)
        return (f"средняя оценка: {average}")



class Teacher(Person):

    base_salary = 30000

    def __init__(self,fullname, age, is_married,expirience):
        super().__init__(fullname, age, is_married)

        self.expirience = expirience

    def up_of_salary(self):
        if self.expirience > 3:
            Teacher.base_salary += Teacher.base_salary*0.05*(self.expirience-3)
            return(f"Текущая зп с учетом повышения:{Teacher.base_salary}")

        else:
            return("Ваш опыт работы меньше 3 лет")

bakytbek = Teacher("Бакытбек", 21, "не в отношении", 7)
print(bakytbek.introduce_myself())
print(bakytbek.up_of_salary())



def create_students():

    first_st = Student("Влад", 20, "не в отношении",
                       math=5, phylosophy=4, physic=5, geometry=3)
    second_st = Student("Сергей", 20, "не в отношении",
                       math=5, phylosophy=5, physic=4, geometry=5)
    third_st = Student("Антон", 20, "не в отношении",
                       math=5, phylosophy=5, physic=5, geometry=5)
    student_list = [first_st,second_st,third_st]

    return student_list

student_list = create_students()
for student in student_list:
    print(f"{student.introduce_myself()},\n Мои оценки {student.marks}, {student.get_average()}")