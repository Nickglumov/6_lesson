password = input('Введите пароль: ')
print(password)

def is_very_long(password):
    return len(password) > 12

def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def has_upper_letters(password):
    for letter in password:
        if letter.isupper():
            return True
    return False

def has_lower_letters(password):
    for letter in password:
        if letter.islower():
            return True
    return False

def has_symbols(password):
    for char in password:
        if not char.isdigit() and not char.isalpha():
            return True
    return False

checks = [
    (is_very_long, 2),
    (has_digit, 2),
    (has_upper_letters, 2),
    (has_lower_letters, 2),
    (has_symbols, 2),
]

def rating_password(password):
    score = 0
    for check_func, points in checks:
        if check_func(password):
            score += points
    return score

score = rating_password(password)
print("Рейтинг пароля:", score)