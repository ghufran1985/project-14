class Student:
    def __init__(self, name, grade, favorite_subject):
        self.name = name
        self.grade = grade
        self.favorite_subject = favorite_subject

    def get_introduction(self):
        return (f"Name: {self.name}, Grade: {self.grade}, Favorite Subject: {self.favorite_subject}\n")

class ClassMonitor:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_or_update_student(self, student):
        with open(self.file_path, 'a') as file:
            file.write(student.get_introduction())

if __name__ == "__main__":
    student1 = Student("Alice", 8, "Math")
    student2 = Student("Bob", 8, "Science")

    monitor = ClassMonitor("students.txt")
    monitor.add_or_update_student(student1)
    monitor.add_or_update_student(student2)