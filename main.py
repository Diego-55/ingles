from abc import ABC, abstractmethod

# Clases abstractas (ejemplo)
class PersonBase(ABC):
    @abstractmethod
    def get_role(self):
        pass

class CourseBase(ABC):
    @abstractmethod
    def add_session(self, session):
        pass

class AttendanceBase(ABC):
    @abstractmethod
    def mark(self, student, present: bool):
        pass

class PaymentBase(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class NotificationBase(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass

# Clases concretas (implementaciones)
class Student(PersonBase):
    def __init__(self, name, email, student_id):
        self.name = name
        self.email = email
        self.student_id = student_id
    def get_role(self):
        return "Student"

class Teacher(PersonBase):
    def __init__(self, name, email, teacher_id):
        self.name = name
        self.email = email
        self.teacher_id = teacher_id
    def get_role(self):
        return "Teacher"

class Administrator(PersonBase):
    def __init__(self, name, email, admin_id):
        self.name = name
        self.email = email
        self.admin_id = admin_id
    def get_role(self):
        return "Administrator"

class Course(CourseBase):
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.sessions = []
    def add_session(self, session):
        self.sessions.append(session)

class Attendance(AttendanceBase):
    def __init__(self):
        self.records = {}
    def mark(self, student, present: bool):
        self.records[student] = present

class Payment(PaymentBase):
    def __init__(self, amount, paid):
        self.amount = amount
        self.paid = paid
    def pay(self, amount):
        self.amount += amount
        self.paid = True

class EmailNotification(NotificationBase):
    def notify(self, message: str):
        return f"Email enviado: {message}"

# Ejemplo de uso en main
def main():
    # Crear personas
    student = Student("Ana", "ana@mail.com", "S001")
    teacher = Teacher("Luis", "luis@mail.com", "T001")
    admin = Administrator("Eva", "eva@mail.com", "A001")

    # Crear curso y sesión
    course = Course("Inglés Básico", "A1")
    session = "Saludos y presentaciones"
    course.add_session(session)

    # Marcar asistencia
    attendance = Attendance()
    attendance.mark(student, True)

    # Realizar pago
    payment = Payment(150.0, True)

    # Enviar notificación
    notification = EmailNotification()
    message = notification.notify(f"Bienvenido al curso {course.name}, {student.name}!")

    # Mostrar información
    print(f"Estudiante: {student.name}, Email: {student.email}")
    print(f"Curso: {course.name}, Nivel: {course.level}")
    print(f"Sesi\u00f3n: {session}")
    print(f"Asistencia marcada: {attendance.records[student]}")
    print(f"Pago realizado: {payment.paid}, Monto: {payment.amount}")
    print(message)

if __name__ == "__main__":
    main()