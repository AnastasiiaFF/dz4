"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.
"""

def create_dict(**kwargs):
    """ Создание словаря из ключевых параметров"""
    result_dict = {}
    for key, value in kwargs.items():
        if value.__hash__ == None:
            value = str(value)
        result_dict[value] = key
    return result_dict


if __name__ == '__main__':
    print(create_dict(key1=1, key2=2, key3=15.6, key4='cat'))