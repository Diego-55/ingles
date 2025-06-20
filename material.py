class Material:
    def __init__(self, title, submaterials=None):
        self.title = title
        self.submaterials = submaterials if submaterials else []

    # Método recursivo para contar todos los materiales (incluyendo submateriales)
    def count_all_materials(self):
        count = 1  # Cuenta este material
        for sub in self.submaterials:
            if isinstance(sub, Material):
                count += sub.count_all_materials()
        return count

class Book(Material):
    def get_type(self):
        return "Book"

class Video(Material):
    def get_type(self):
        return "Video"

class Dictionary(Material):
    def __init__(self, language, submaterials=None):
        super().__init__(language, submaterials)
        self.language = language

    def get_type(self):
        return "Dictionary"

class AudioMaterial(Material):
    def get_type(self):
        return "Audio"