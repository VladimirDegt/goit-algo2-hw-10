# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

def create_schedule(subjects, teachers):
    subjects = set(subjects)
    remaining_subjects = subjects.copy()
    selected_teachers = []

    while remaining_subjects and teachers:
        best_teacher = None
        max_covered = set()
        min_age = float('inf')

        for teacher in teachers:
            covered = teacher.can_teach_subjects & remaining_subjects
            if len(covered) > len(max_covered) or (len(covered) == len(max_covered) and teacher.age < min_age):
                best_teacher = teacher
                max_covered = covered
                min_age = teacher.age

        if not best_teacher:
            return None

        best_teacher.assigned_subjects = max_covered
        selected_teachers.append(best_teacher)
        remaining_subjects -= max_covered
        teachers.remove(best_teacher)

    if remaining_subjects:
        return None

    return selected_teachers

if __name__ == "__main__":
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}

    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {"Інформатика", "Математика"}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {"Фізика", "Інформатика"}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"})
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")