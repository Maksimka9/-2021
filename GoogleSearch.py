from bs4 import BeautifulSoup
import io
import urllib.request
import os
import shutil
try:
    from googlesearch import search
except ImportError:
    print('Библиотеки нет')

strings = list()
FileName = 'Поисковые запросы.txt'
with io.open(FileName, encoding='utf-8') as file:  # Подключение Файла с запросами
    for line in file:
        strings.append(line)

strings = [line.rstrip() for line in strings]  # Удаление пробелов



for i in strings:
    query = i
    try:
        #shutil.rmtree(query)
        os.mkdir(query)
        print("\n" + "Запрос: " + query + "\n")
    except:
        print("\n" + "Запрос: " + query + "\n")
        for k in range(1, 20):
            try:
                os.mkdir(query + " " + str(k))
                break
            except:
                k+=1

    j = 0
    for Searchlink in search(query, tld='co.in', num=5, stop=5, pause=0):
        try:
            webURL = urllib.request.urlopen(Searchlink)



            soup = BeautifulSoup(webURL, 'html.parser')

            directory = os.path.abspath(FileName).replace(FileName,'')
            while j < 5:
                j += 1
                FullDirectory = directory + query + '\\' + str(j) + '.txt'
                break

            if str(webURL.getcode()) == "200":
                print("Соединение с ресурсом №" + str(j) + " установлено")

            my_file = open(FullDirectory, "w", encoding='utf-8')
            my_file.write(str(soup.get_text()))
            print("Текст сохранен \n")
        except:
            print("Не удалось установить соединение с сайтом \n")