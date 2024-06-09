import sys


# Задание №2
def is_palindrome(data):
    return data == data[::-1]


def main():
    input_string = sys.stdin.readline().strip()
    if is_palindrome(input_string):
        print("YES")
    else:
        print("NO")


# Задание №1
def test_is_palindrome():
    test_cases = ["казак", "hello", "", "питон", "манекенам", "математика", "шабаш"]
    results = [True, False, True, False, True, False, True]

    for i, test_case in enumerate(test_cases):
        if is_palindrome(test_case) != results[i]:
            print("NO")
            return
    print("YES")


if __name__ == "__main__":
    # Выполнение теста
    test_is_palindrome()

    # Выполнение основной программы
    main()
