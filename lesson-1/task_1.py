"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""
words = '«разработка», «сокет», «декоратор»'.replace("«", "").replace("»", "").split(", ")

for word in words:
    print(type(word), word)

word_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
word_2 = '\u0441\u043e\u043a\u0435\u0442'
word_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

words_uni = [word_1, word_2, word_3]

for word in words_uni:
    print(type(word), word)
