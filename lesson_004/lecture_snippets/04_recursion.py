# -*- coding: utf-8 -*-

# Рекурсия - это вызов функцией самой себя

# Рассмотрим на примере факториала
# факториал N - произведение всех целых от 1 до N

# например факториал 9
# 9! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9
# 9! = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
# 9! = 9 * (8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
# 9! = 9 * 8!
# 9! = 9 * factorial(8)

# факториал 2
# 2! = 2 * factorial(1)
# 1! == 1

# в общем случае
# N * factorial(N-1)


def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n=n - 1)
    return n * factorial_n_minus_1


print(factorial(9))


# рекурсия часто используется для обхода деревьев
html_dom = {
    'html': {
        'head': {
            'title': 'Колобок',
        },
        'body': {
            'h2': 'Привет!',
            'div': 'Хочешь, я расскажу тебе сказку?',
            'p': 'Жили-были старик со старухой...',
        }
    }
}


def find_element(tree, element_name):
    if element_name in tree:
        return tree[element_name]
    for key, sub_tree in tree.items():
        if isinstance(sub_tree, dict):
            result = find_element(tree=sub_tree, element_name=element_name)
            if result:
                break
    else:
        result = None
    return result


res = find_element(tree=html_dom, element_name='title')
print(res)
