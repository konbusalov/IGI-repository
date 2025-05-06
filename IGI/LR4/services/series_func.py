from math import pi, factorial
from statistics import mean, median, mode, variance, stdev
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import cos

class SeriesFunction:
    def __init__(self, x, eps):
        self.x = x
        self.eps = eps
        self.result = 0
        self.n = 0
        self.sequence = []
        self._validate_inputs()
        self._calculate_cos()
        self._calculate_stats()

    def _validate_inputs(self):
        if not -pi <= self.x <= pi:
            raise ValueError("x must be between -π and π (inclusive).")
        if self.eps >= 1:
            raise ValueError("eps must be less than 1.")

    def _calculate_cos(self):
        n = 0
        current_el = ((-1)**n) * ((self.x**(2*n))/factorial((2*n)))
        
        while abs(current_el) > self.eps and n < 500:
            self.result += current_el
            self.sequence.append(current_el)
            n += 1
            current_el = ((-1)**n) * ((self.x**(2*n))/factorial((2*n)))
        
        self.n = n

    def _calculate_stats(self):
        self.sequence_mean = mean(self.sequence)
        self.sequence_median = median(self.sequence)
        self.sequence_mode = mode(self.sequence)
        self.sequence_variance = variance(self.sequence)
        self.sequence_stdev = stdev(self.sequence)

    def plot_series_function(self):
        fig = plt.figure(figsize=(10,6))
        ax = fig.add_subplot()

        x_values = np.arange(len(self.sequence))
        y_values = self.sequence
        ax.plot(x_values, y_values, 'ro', markersize=6, label='Series terms')

        math_x = np.linspace(-3*np.pi, 3*np.pi, 400)
        exact_cos = [cos(x) for x in math_x]
        ax.plot(math_x, exact_cos, 'b-', linewidth=2, label='Exact cos(x)')

        # Customize plot appearance
        plt.title('Cosine Function vs Series Function', fontsize=14)
        plt.xlabel('Term Number / x value', fontsize=12)
        plt.ylabel('Function Value', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.legend(fontsize=12)

        plt.savefig("plot.png")




