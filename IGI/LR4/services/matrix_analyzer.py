import numpy as np

class MatrixAnalyzer:
    def __init__(self, n, m, low=0, high=100):
        self.matrix = np.random.randint(low, high, size=(n, m))
        self.n = n
        self.m = m
    
    def get_secondary_diagonal(self):
        return np.fliplr(self.matrix).diagonal()
    
    def min_secondary_diagonal(self):
        return np.min(self.get_secondary_diagonal())
    
    def variance_secondary_diagonal(self):
        diag = self.get_secondary_diagonal()
        
        var_numpy = np.var(diag)
        
        mean = np.mean(diag)
        var_formula = np.mean(diag**2) - mean**2
        
        return round(var_numpy, 2), round(var_formula, 2)
    
    def analyze(self):
        analysis = {
            'matrix': self.matrix,
            'secondary_diagonal': self.get_secondary_diagonal(),
            'min_secondary': self.min_secondary_diagonal(),
            'variance': self.variance_secondary_diagonal(),
            'mean': round(np.mean(self.matrix), 2),
            'median': round(np.median(self.matrix), 2),
            'std': round(np.std(self.matrix), 2),
            'correlation': np.corrcoef(self.matrix)
        }
        return analysis