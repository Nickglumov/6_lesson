def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return any(not char.isdigit() and not char.isalpha() for char in password)


def rating_password(password):
    checks = [
        (is_very_long, 2),
        (has_digit, 2),
        (has_upper_letters, 2),
        (has_lower_letters, 2),
        (has_symbols, 2),
    ]
    score = 0
    for check_func, points in checks:
        if check_func(password):
            score += points
    return score
    

def main():
    password = input("Введите пароль: ")
    score = rating_password(password)
    print("Рейтинг пароля:", score)


if __name__ == "__main__":
    main()
