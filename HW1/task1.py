from typing import List

example1 = [12, 213, 4, 1, 2123, 511, 51]
example2 = [1, -10, 24, -28]
example3 = [1, 2, -3]

def task1(l: List[int]) -> List[int]:
    l.sort()
    
    if l[0] * l[1] >= l[-1] * l[-2]:
        return [l[0], l[1]]
    else:
        return [l[-1], l[-2]]

# Примеры

print(task1(example1))
print(task1(example2))
print(task1(example3))