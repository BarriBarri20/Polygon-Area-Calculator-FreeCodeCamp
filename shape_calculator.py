
class Rectangle : 
    def __init__(self, width, height) : 
        self.width = width
        self.height = height
    def set_width(self, width):
        self.width = width
    def set_height(self, height) : 
        self.height = height
    def get_area(self) :
        return self.width * self.height
    def get_perimeter(self) : 
        return 2 * self.width + 2 * self.height
    def get_diagonal(self) :
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self) :
        if self.width > 50 or self.height > 50 : 
            return "Too big for picture."
        s = ""
        for i in range(self.height) : 
            s += "*" * self.width + "\n"
        return s
    def __repr__(self) :
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    def get_amount_inside(self, other) : 
        return (self.width // other.width) * (self.height // other.height)
class Square(Rectangle) : 
    def __init__(self, side):
        super().__init__(side, side)
    def set_side(self, side) : 
        self.height = side
        self.width = side
    def __repr__(self):
        return "Square(side=" + str(self.width) + ")"

