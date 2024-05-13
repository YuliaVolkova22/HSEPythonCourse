example1 = 'ABBA'
example2 = 'hello_kitty'
example3 = 'i_love_evol_i'

def task5(s: str) -> bool:
    if s == s[::-1]:
        return True
    else:
        return False

# Примеры

print(task5(example1))
print(task5(example2))
print(task5(example3))

print(task5(input('Введите строку: ')))