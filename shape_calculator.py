import math
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def __str__(self):
        return f'Rectangle(width={self.w}, height={self.h})'

    def set_width(self, w):
        self.w = w

    def set_height(self, h):
        self.h = h

    def get_area(self):
        area = self.w * self.h
        return area

    def get_perimeter(self):
        p = 2 * (self.w + self.h)
        return p

    def get_diagonal(self):
        d = (self.w ** 2 + self.h ** 2) ** 0.5
        return d

    def get_picture(self):
        if self.w > 50 or self.h > 50:
            return "Too big for picture."
        picture=''
        line=self.w * '*'
        for x in range(self.h):
            picture += line + '\n'
        return picture

    def get_amount_inside(self, shape):
        x_ax = math.floor(self.w /shape.w)
        y_ax = math.floor(self.h /shape.h)
        return x_ax * y_ax


class Square(Rectangle):
    def __init__(self, x):
        self.w = x
        self.h = x
    
    def __str__(self):
        return f'Square(side={self.w})'

    def set_side(self, x):
        self.w = x
        self.h = x
    
    def set_width(self, x):
        self.w = x
        self.h = x

    def set_height(self, x):
        self.w = x
        self.h = x
