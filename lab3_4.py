import re
import sys


# Задание №4
def is_correct_mobile_phone_number_ru(number):
    pattern = r'^(8|\+7)[\-\s]?(?:\(\d{3}\)|\d{3})[\-\s]?\d{3}[\-\s]?\d{2}[\-\s]?\d{2}$'
    return re.match(pattern, number) is not None


def main():
    input_string = sys.stdin.readline().strip()
    if is_correct_mobile_phone_number_ru(input_string):
        print("YES")
    else:
        print("NO")


# Задание №3
def test_is_correct_mobile_phone_number_ru():
    test_numbers = [
        '8(916)123-45-67',
        '+7 926 123-45-67',
        '89161234567',
        '+7(495)1234567',
        
    ]
    expected_results = [True, True, True, True]

    for number, expected in zip(test_numbers, expected_results):
        if is_correct_mobile_phone_number_ru(number) != expected:
            print("NO")
            return
    print("YES")


if __name__ == "__main__":
    # Выполнение теста
    test_is_correct_mobile_phone_number_ru()

    # Выполнение основной программы
    main()
