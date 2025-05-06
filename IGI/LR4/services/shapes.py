from abc import ABC, abstractmethod
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle
import numpy as np

class Shape(ABC):
    @abstractmethod
    def area():
        pass

class ShapeColor:
    def __init__(self, color):
        self._color = color
    
    def get_color(self):
        return self._color
    
    def set_color(self, value):
        self._color = value

    color = property(get_color, set_color)

class Hexagon(Shape):
    def __init__(self, length, color):
        self._length = length
        self._color = ShapeColor(color)
        self._shape_name = "Hexagon"
        
    @property 
    def length(self):
        return self._length
    
    @property 
    def color(self):
        return self._color.get_color()
    
    @property
    def shape_name(self): 
        return self._shape_name
    
    def area(self):
        return ((3 * sqrt(3))/2) * self._length**2
    
    def get_info(self):
        return (
            "Shape Parameters:\n"
            "Type: {type}\n"
            "Side Length: {length:.2f}\n"
            "Color: {color}\n"
            "Area: {area:.2f}"
        ).format(
            type=self.shape_name,
            length=self.length,
            color=self.color,
            area=self.area()
        )
    
class DrawerMixin:
    def setup_axes(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal')
        self.ax.set_xlim(0, 20)
        self.ax.set_ylim(0, 20)
        
    def save_to_file(self, filename):
        self.fig.savefig(filename)
        print(f"Drawing saved to {filename}")
        
    def show(self):
        plt.show()

class HexagonDrawer(DrawerMixin):
    def __init__(self):
        self.setup_axes()
        
    def draw_hexagon(self, hexagon, label):
        radius = hexagon.length  
        angles = np.linspace(0, 2*np.pi, 7)[:-1]  
        x = 10 + radius * np.cos(angles)
        y = 10 + radius * np.sin(angles)
        
        hex_patch = Polygon(np.column_stack([x, y]), 
                          closed=True, 
                          facecolor=hexagon.color, 
                          edgecolor='black')
        self.ax.add_patch(hex_patch)
        self.ax.text(10, 10, label, ha='center', va='center', fontsize=12)



