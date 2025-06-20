class Course:
    def __init__(self, name, subcourses=None):
        self.name = name
        self.subcourses = subcourses if subcourses else []

    # Método recursivo para contar todos los subcursos
    def count_all_subcourses(self):
        count = len(self.subcourses)
        for sub in self.subcourses:
            if isinstance(sub, Course):
                count += sub.count_all_subcourses()
        return count