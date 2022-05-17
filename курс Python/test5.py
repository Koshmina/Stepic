from test24 import Calculate

class Figure:
    def __init__(self, color):
        self.color = color


    def color(self):
        return self.color


    def color(self, c):
        self.color = c


class Rectangle(Figure,Calculate):
    def __init__(self, width, height, color, x, y):
      #  super().__init__(color)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    def width(self):
        return self.width


    def width(self, w):
        if w > 0:
            self.width = w
        else:
            raise ValueError


    def height(self):
        return self.height


    def height(self, h):
        if h > 0:
            self.height = h
        else:
            raise ValueError

    def area(self):
        return self.width * self.height

rect=Rectangle(12,16,'red',1,3)
rect.sum()
print(rect.sum())