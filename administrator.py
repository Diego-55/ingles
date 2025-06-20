from person import Person

class Administrator(Person):
    def __init__(self, name, email, admin_id, subordinates=None):
        super().__init__(name, email)
        self.admin_id = admin_id
        self.subordinates = subordinates if subordinates else []

    def get_role(self):
        return "Administrator"

    # Método recursivo para contar todos los subordinados (directos e indirectos)
    def count_all_subordinates(self):
        count = len(self.subordinates)
        for sub in self.subordinates:
            if isinstance(sub, Administrator):
                count += sub.count_all_subordinates()
        return count