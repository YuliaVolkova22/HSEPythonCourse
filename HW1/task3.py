from typing import List

example1 = [-213, 0, 51, 22, 95, 4214, 223]
example2 = [-12, -11, -5, -404, -72]
example3 = [1, 2, 9, 10, 12]

def task3(l: List[int]) -> bool:
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            continue
        else:
            return 'False'
        
    return 'True'

# Примеры
 
print(task3(example1))
print(task3(example2))
print(task3(example3))
