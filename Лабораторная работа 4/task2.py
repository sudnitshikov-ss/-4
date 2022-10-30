def get_count_char(str_):
    str_ = "".join(str_.split())
    str_ = str_.lower()
    dictionary_ = {}
    for sym in str_:
        if sym.isalpha():
            if sym in dictionary_:
                dictionary_[sym] = dictionary_[sym] + 1
            else:
                dictionary_[sym] = 1

    return dictionary_
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
