"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
words = '«разработка», «администрирование», «protocol», «standard»'.replace("«", "").replace("»", "").split(", ")

for word in words:
    print(word.encode('utf-8').decode('utf-8'))