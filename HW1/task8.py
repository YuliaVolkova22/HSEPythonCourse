from typing import Union, List, Tuple
import numpy as np

class Statistics:
    def __init__(self, data: Union[List[int|float], Tuple[int|float], np.ndarray[int|float]]):
        self.data = data
        
    def calculate_mean(self) -> float | int:
        return np.mean(self)
        
    def calculate_median(self) -> float | int:
        return np.median(self)
        
    def calculate_mode(self) -> float | int:
        mode, count = np.unique(self, return_counts = True)
        max_value = float('-inf')

        for i in range (len(mode)):
            if count[i] == max(count) & mode[i] > max_value:
                max_value = mode[i]
        
        return max_value
    
    def std(self) -> float | int:
        return np.std(self)
    
    def iqr(self) -> float | int:
        return np.percentile(self, 75) - np.percentile(self, 25)
