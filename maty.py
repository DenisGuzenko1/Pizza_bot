import json

ar = []  # создаем пустой список

with open('maty.txt', encoding='utf-8') as r:  # открываем для чтения текстовый документ
    for i in r:                                # проходимся построчно по файлу
        n = i.lower().split('\n')[0]  # делаем нижн регистр, разбив строк на списки, с разделит \n, берем 1 символ слова
        if n != '':                 # проверяем, что этот символ не пустой
            ar.append(n)  # добавили н
with open('maty.json', 'w', encoding='utf-8') as e:  # открываем джейсо файл для записи
    json.dump(ar, e)  # фунцция dump позволяет записать данные в файл, передаем список из слов и объект чтения
