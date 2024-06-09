import re
import sys

# Задание №6
def strip_punctuation_ru(data):
    punctuation_pattern = r"[!\"#$%&'()*+,-./:;<=>?@\[\\\]^_`{|}~«»]"
    stripped_text = re.sub(punctuation_pattern, " ", data)
    return " ".join(stripped_text.split())

def main():
    input_string = sys.stdin.readline().strip()
    print(strip_punctuation_ru(input_string))

# Задание №5
def test_strip_punctuation_ru():
    test_data = [
        
        '«Пример» со знаками "препинания"',
        'Точка. Запятая, восклицательный! знак?',
        'Скобки (круглые) и [квадратные]',
        'Много знаков: !@#$%^&*()_+{}:"<>?'
    ]
    expected_results = [
        
        'Пример со знаками препинания',
        'Точка Запятая восклицательный знак',
        'Скобки круглые и квадратные',
        'Много знаков'
    ]

    for data, expected in zip(test_data, expected_results):
        if strip_punctuation_ru(data) != expected:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    # Выполнение теста
    test_strip_punctuation_ru()
    
    # Выполнение основной программы
    main()
