import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(list).reshape(3, 3)
    
    def get_stats(func):
        return [
            func(matrix, axis=0).tolist(),
            func(matrix, axis=1).tolist(),
            func(matrix).tolist() if hasattr(func(matrix), 'tolist') else func(matrix)
        ]
    
    calculations = {
        'mean': get_stats(np.mean),
        'variance': get_stats(np.var),
        'standard deviation': get_stats(np.std),
        'max': get_stats(np.max),
        'min': get_stats(np.min),
        'sum': get_stats(np.sum)
    }
    
    return calculations
