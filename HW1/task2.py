from typing import List

example1 = [123, 32, 23, 98, 1]
example2 = [-23, -51, -8, -10]
example3 = [123, 414, -42, -2, 123, 0]
 
def task2(l: List[int]) -> List[int]:
    l.sort(reverse = True)
    max_positive = l[0] * l[1] * l[2]
    max_mix = l[0] * l[-1] * l[-2]

    if max_positive > max_mix:
        return [l[0], l[1], l[2]]
    else:
        return [l[0], l[-1], l[-2]]
    
# Примеры

print(task2(example1))
print(task2(example2))
print(task2(example3))