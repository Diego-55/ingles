import unittest
from material import Material, Book, Video, Dictionary, AudioMaterial

class TestMaterial(unittest.TestCase):
    def test_material_creation(self):
        m = Material("Material Base")
        self.assertEqual(m.title, "Material Base")
        self.assertEqual(m.submaterials, [])

    def test_count_all_materials(self):
        # Jerarquía: paquete -> libro, video; libro -> diccionario, audio
        audio = AudioMaterial("Audio 1")
        diccionario = Dictionary("Inglés")
        libro = Book("Libro 1", [diccionario, audio])
        video = Video("Video 1")
        paquete = Material("Paquete", [libro, video])
        self.assertEqual(paquete.count_all_materials(), 5)
        self.assertEqual(libro.count_all_materials(), 3)
        self.assertEqual(video.count_all_materials(), 1)
        self.assertEqual(diccionario.count_all_materials(), 1)
        self.assertEqual(audio.count_all_materials(), 1)

if __name__ == "__main__":
    unittest.main()