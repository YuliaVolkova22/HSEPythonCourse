from collections import Counter

example1 = 'money'
example2 = 'honey_aaaaabbbbbaaaaa'
example3 = 'i like grandmom aaaaaaaaaaaaa'
    
def task7(s: str) -> int:
    chars_count = Counter(s)
    length = 0
    has_odd = False

    for count in chars_count.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            has_odd = True

    if has_odd:
        length += 1

    return length

# Примеры

print(task7(example1))
print(task7(example2))
print(task7(example3))

print(task7(input('Введите строку: ')))