# 1.Написать ФиО студента
# 2.Пройти экзамен
# 3.Результаты экзамена
# 4.Уровень знание студентов
# 5.Список студентов
# 6.Завершить программу

class Student:
    def __init__(self, name):
        self.name = name
        self.exam_score = None
        
    def pass_exam(self, score):
        self.exam_score = score
        
    def get_level(self):
        if self.exam_score == 8:
            return "Профессионал"
        if self.exam_score == 7:
            return "Сигмейший"
        if self.exam_score == 6:
            return "Превосходно"
        if self.exam_score == 5:
            return "Отлично"
        if self.exam_score == 4:
            return "Нормально"
        if self.exam_score == 3:
            return "Удевлетворительно"
        if self.exam_score == 2:
            return "Плохо"
        if self.exam_score == 1:
            return "Ужасно"
        if self.exam_score == 0:
            return "Отказ"
        
class Exam:
    def __init__(self):
        self.questions = [
            """1.Что делает функция len() в Python?
A. Выводит длину объекта
B. Умножает два числа
C. Создает список
D. Удаляет объект""",
            """2.Какой из этих операторов используется для возведения в степень?
A. *
B. **
C. ^
D. //""",
            """3.Как обозначается цикл в Python?
A. for
B. while
C. оба варианта
D. никакой из них""",
            """4.Какой тип данных используется для хранения истинности (логики)?
A. int
B. str
C. float
D. bool""",
            """5.Что делает метод append() у списков?
A. Добавляет элемент в конец списка
B. Удаляет элемент из списка
C. Создает новый список
D. Сортирует список""",
            """6.Что возвращает функция input()?
A. Число
B. Строку
C. Список
D. Кортеж""",
            """7.Как обозначается комментарий в Python?
A. //
B. #
C. /* */
D. <--""",
            """8.Какой модуль используется для работы с математическими операциями в Python?
A. os
B. math
C. sys
D. random"""
        ]
        self.answers = ["A", "B", "C", "D", "A", "B", "B", "B"]
        
    def start_exam(self):
        print("\nЭкзамен начинается!")
        score = 0
        for i, question in enumerate(self.questions):
            print("\n" + question)
            user_answer = input("Ваш ответ (A, B, C, D): ").strip().upper()
            if user_answer == self.answers[i]:
                score += 1
        print(f"\nВы набрали {score}/{len(self.questions)} баллов.")
        return score
        
        
class StudentList:
    def __init__(self):
        self.students = []
        self.exam = Exam()
        
    def add_student(self):
        name = input("Введите ФИО студента: ")
        self.students.append(Student(name))
        print(f"Студент {name} добавлен.")
        
    def pass_exam(self):
        if not self.students:
            print("Еще некого нету в группе!")
            return
        
        print("Выберите студента для экзамена:")
        for idx, student in enumerate(self.students, 1):
            print(f"{idx}. {student.name}")
        
        index = int(input("Введите номер студента: ")) - 1
        if 0 <= index < len(self.students):
            student = self.students[index]
            score = self.exam.start_exam()
            student.pass_exam(score)
            print(f"Экзамен завершен! {student.name} набрал {score}/8.")
        else:
            print("Неверный выбор студента.")
            
    def show_results(self):
        print("\nРезультаты экзаменов:")
        for student in self.students:
            if student.exam_score is not None:
                print(f"{student.name}: {student.exam_score}/8 ({student.get_level()})")
                    
    def list_students(self):
        if not self.students:
            print("Студенты не добавлены.")
        for student in self.students:
            print(f"{student.name}: {student.exam_score}")
            
    def menu(self):
        while True:
            print("\nМеню:")
            print("1. Добавить студента")
            print("2. Пройти экзамен")
            print("3. Результаты экзамена")
            print("4. Список студентов")
            print("5. Выход")
            choice = input("Выберите действие: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.pass_exam()
            elif choice == "3":
                self.show_results()
            elif choice == "4":
                self.list_students()
            elif choice == "5":
                break
            else:
                print("Неверный выбор.")


student_list = StudentList()
student_list.menu()








# class Car:
#     def __init__(self, model, year, speed, color):
#         self.model = model
#         self.year = year
#         self.speed = 0
#         self.color = color
        
#     def start(self):
#         print(f"Машина {self.model},{self.year}, {self.color}, {self.speed} запущена.")
        
# main = Car(model= 'Audi', year= 2023, speed= 0, color= 'black')
# main.start()

# class Electrocar(Car):
  
#     def start(self):
#         print(f"Электромашина {self.model}, {self.year}, {self.color}, {self.speed} запущена.")
        
# main = Electrocar(model= 'Tesla', year= 2023, speed= 0, color= 'black')
# main.start()







