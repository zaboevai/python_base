def check_game_result(game_result):
    symbols = ['Х', '/', '-']
    result = game_result
    for symbol in symbols:
        result = result.replace(symbol, '')

    if not result.isdigit():
        return 'Недопустимый символ'
    elif len(game_result.replace('Х', '')) % 2 == 1:
        return 'Введены не полные результаты'


def get_score(game_result):
    error = check_game_result(game_result)
    if error:
        print(f'Ошибка: <{error}>')
    else:
        result = 0
        frame = 0
        is_first_strike, is_second_strike = True, False
        first_strike_score = 0
        second_strike_score = 0

        for score in game_result:
            if is_first_strike:
                if score == 'Х':
                    first_strike_score = 20
                    frame += 1
                elif score.isdigit():
                    first_strike_score = int(score)
                    is_first_strike, is_second_strike = False, True
                elif score == '-':
                    is_first_strike, is_second_strike = False, True
                    continue
                result += first_strike_score
            elif is_second_strike:
                if score == '/':
                    result -= first_strike_score
                    first_strike_score = 0
                    second_strike_score = 15
                elif score.isdigit():
                    second_strike_score = int(score)
                elif score == '-':
                    second_strike_score = 0
                is_first_strike, is_second_strike = True, False
                result += second_strike_score
                frame += 1

        print('Бросков=', frame, ', очков=', result)


if __name__ == '__main__':
    get_score(game_result='Х4/34--ХХ1231231212')
