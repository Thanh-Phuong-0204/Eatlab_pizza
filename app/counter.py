class PizzaCounter:
    def __init__(self):
        self.total = 0

    def update(self, new_count):
        self.total = new_count

    def get_total(self):
        return self.total