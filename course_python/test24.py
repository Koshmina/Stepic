class Calculate:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def sum(self):
        return self.x + self.y


#sa = Calculate(12, 3)
print(Calculate(12, 3).sum())
