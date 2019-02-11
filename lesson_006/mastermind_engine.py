from random import randint as rnd

_numbers = []


def generate_number():
    number = []
    for i in range(4):
        if i == 0:
            number.append(rnd(1, 9))
        else:
            number.append(rnd(0, 9))
    return number


def make_number():
    _numbers.clear()
    _numbers.extend(generate_number())
    return _numbers


def check_number(chk_number):
    result = {'bulls': 0, 'cows': 0}
    chk_numbers = []

    for char in map(int, chk_number):
        chk_numbers.append(char)

    for pos, number in enumerate(_numbers):
        for chk_pos, chk_number in enumerate(chk_numbers):
            if number == chk_number:
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
