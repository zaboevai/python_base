from random import randint as rnd

_hidden_numbers = []


def generate_number():
    number = []
    for i in range(4):
        if i == 0:
            number.append(rnd(1, 9))
        else:
            number.append(rnd(0, 9))
    return number


def make_number():
    _hidden_numbers.clear()
    _hidden_numbers.extend(generate_number())
    return _hidden_numbers


def check_number(number):
    result = {'bulls': 0, 'cows': 0}
    chk_numbers = []

    for char in map(int, number):
        chk_numbers.append(char)

    for pos, hidden_number in enumerate(_hidden_numbers):
        for chk_pos, number in enumerate(chk_numbers):
            if hidden_number == number:
                if pos == chk_pos:
                    result['bulls'] += 1
                    continue
                else:
                    result['cows'] += 1

    return result


if __name__ == '__main__':
    make_number()
    bull, cow = check_number('1234')
    print(bull, cow)
