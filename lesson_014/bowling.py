class WrongSymbolsError(Exception):
    pass

class WrongGameLengthError(Exception):
    pass


def check_game_result(game_result):
    symbols = ['Х', '/', '-']
    result = game_result
    for symbol in symbols:
        result = result.replace(symbol, '')

    if result:
        if not result.isdigit():
            raise WrongSymbolsError('Ошибка! Введен неверный символ. (допустимы только "цифры, Х, /, -")')
        elif len(game_result.replace('Х', '')) % 2 == 1:
            raise WrongGameLengthError('Введены не полные результаты')


def get_score(game_result):
    error = check_game_result(game_result)
    if error:
        return f'Ошибка: <{error}>'
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
    return result


if __name__ == '__main__':
    try:
        print(get_score(game_result='Х1231231/555574964355'))
    except WrongGameLengthError as exc:
        print(exc)
    except WrongSymbolsError as exc:
        print(exc)
    except BaseException as exc:
        print(f'Непредвиденная ошибка {exc}')