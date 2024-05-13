example1 = 'ABBA' # True
example2 = 'hello_kitty'    # False

def task5(s: str) -> bool:
    return True if s == s[::-1] else False

# Примеры

print(task5(example1))
print(task5(example2))

print(task5(input('Введите строку: ')))