example1 = 'aaaaaaaaaaaaaaaaaaaab'
example2 = 'eeeeerrrrraaaaaaarrrraaaaaaa'
example3 = 'i like mom'

def task6(s: str) -> int:
    letters = list(s)
    answer = []
    
    if len(letters) == 1:
        return 1

    for i in range(len(letters) - 1):
        add_row = letters[i]

        for j in range(i + 1, len(letters)):
            add_row = add_row + letters[j]

            if add_row == add_row[::-1]:
                answer.append(len(add_row))
    
    if len(answer) >= 1:
        return max(answer)
    else:
        return 1

# Примеры

print(task6(example1))
print(task6(example2))
print(task6(example3))

print(task6(input('Введите строку: ')))