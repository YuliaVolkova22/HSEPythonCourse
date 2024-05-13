example1 = 'ааааааааааааббббафафафафцу'
example2 = 'ыфвфвызвцфвейыв'
example3 = 'лала-лэнд'

def task4(s: str) -> int:
    vowels = list(set('ауoыэяюёие'))
    
    letters = list(set(s))
    count = 0

    for letter in letters:
        if letter in vowels:
            count += 1
    
    return count

# Примеры

print(task4(example1))
print(task4(example2))
print(task4(example3))

print(task4(input('Введите строку: ')))