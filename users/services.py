import random


def generation():
    '''Генерация кода для подтверждения регистрации'''
    code = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    return code