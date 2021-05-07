import re

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __repr__(self):
        if self.width != self.height:
            return f'Rectangle(width={self.width}, height={self.height})'
        else:
            return f'Square(side={self.width})'
            
    def set_width(self, num):
        self.width = num
    
    def set_height(self, num):
        self.height = num
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            w = self.width * '*'
            pict = ''
            for i in range(self.height):
                pict += w + '\n'
            return pict
        
    def get_amount_inside(self, shape):
        # Find all numbers in the shape description string 
        s = re.findall(r"(\d+)", repr(shape))
        if len(s) > 1:
            width = int(s[0])
            height = int(s[1])
        else:
            width = int(s[0])
            height = int(s[0])
        
        if self.width < width and self.height < height:
            fit = 0
        if self.width == width and self.height < height:
            fit = 0
        if self.width < width and self.height == height: 
            fit = 0
        if self.width == width and self.height == height:
            fit = 1
        if self.width == width and self.height > height:
            fit = self.height // height
        if self.width > width and self.height == height: 
            fit = self.width // width
        if self.width > width and self.height > height:
            fit = (self.width // width) * (self.height // height)
        return fit
        
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        
    def set_side(self, length):
        self.width = length
        self.height = length
        
    def set_width(self, length):
        return self.set_side(length)
    
    def set_height(self, length):
        return self.set_side(length)