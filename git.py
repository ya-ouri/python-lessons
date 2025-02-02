#1.	Результаты переписи населения (фамилия, имя и год рождения) хранятся в файле Perepis.txt.
#а) Выведите фамилии и подсчитайте общее число жителей, родившихся раньше 1978 года.
#б) Выведите данные людей (ФИО и год рождения), родившихся в указанном пользователем диапазоне лет.
import codecs

count = 0


with codecs.open('perepis.txt', 'r', "utf_8_sig") as f:
    for i in f:
        #a
        if i.split(' ')[6].split(".")[2].strip('\r\n') < '1978':
            count += 1
            print(i.split(' ')[0])

print(count)
        #b
min = input('min')
max = input('max')

with codecs.open('perepis.txt', 'r', "utf_8_sig") as f:
    for i in f:
        if min < i.split(' ')[6].split(".")[2].strip('\r\n') < max:
            print(i.split(' ')[0] , i.split(' ')[6].split(".")[2].strip('\r\n'))

