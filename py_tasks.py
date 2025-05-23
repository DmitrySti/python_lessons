#  ЗАДАЧНИК ПО Python https://code.mu/ru/python/tasker/stager/
# переменные для задач
number = 218956   # число
number1 = 5466   # число 
string = 'Шла Саша по шоссе и сосала сушку!' # строка
strings = [
    "http://example.com",
    "https://google.com",
    "home.html",
    "ftp://files.net",
    "HTTP://case.insensitive.test",
    "profile.html",
    "just a text",
    "http:/malformed.url",
    "catalog.html",
    "http://another.valid.site",
    "mailto:user@example.com",
    "index.html",
    "http://",
    "docs.html",
    "http://yandex.ru",
    "news.html",
    "about.html",
    "services.html"
]
numbers_string = '12, 34, 56'
last_char_of_string = string[-1] # [-1] первый символ с конца строки, [0] - первый символ с начала строки
word1 = "Лето"
word2 = "Соска"
last_char_of_word1 = word1[-1]
digits_list = [1, 2, 3, 4, 5, 6]   # список
digits_list1 = [1, 2, -3, 4, -5]
digits_list2 = [1, 2, -3, 4, 5, 11]
numbers_list = [47, -83, 12, 91, -5, -42, 76, 33, -19, 88, -61, 0, 54, -27, 3]
digits_range1 = range(1, 101)
digits_range2 = range(-100, 1) 
digits_range3 = range(101, 0, -1)
digits_range4 = range(0, 101, 2)    
date = '2025-12-31'                           
date_dict = {'year' : '2025','month': '12','day'  : '31', } # словарь
digits_dict ={'a': 1, 'b': 2, 'c': 3, 'd': 4, }
digits_tuple = (1, 2, 3, 4, 5, 6) # кортеж
float_numbers_list = [
    -47.2837164923851,
    83.1598743264892,
    -12.9176543210987,
    91.0483726159432,
    5.3398765421987,
    -42.765432198765,
    76.2246891357924,
    -33.987654321098,
    19.456789123456,
    -88.012345678901,
    61.278945612378,
    -0.543219876543,
    54.398765432109,
    27.123456789012,
    -3.857412369874
]
    # УРОВЕНЬ 1.1


    # №1
    # Дано число. Проверьте, отрицательное оно или нет. Выведите об этом информацию в консоль.
print(' УРОВЕНЬ 1.1')
print(' Задача №1.1.1')
print('Число', str(number), '- положительное!') if number > 0 else print('Число', str(number), '- отрицательное!')
print('')


    # №2
    # Дана строка. Выведите в консоль длину этой строки.
print(' Задача №1.1.2')
print('Колличесвто символов в строке:', '"'+ string + '"', '- ', len(string))
print('')


    # №3
    # Дана строка. Выведите в консоль последний символ строки.
print(' Задача №1.1.3')
print('Последний символ в строке:', last_char_of_string)
print('')


    # №4
    # Дано число. Проверьте, четное оно или нет.
print(' Задача №1.1.4')
is_even_number = True if number % 2 == 0 else False
print('Число', number, 'чётное!') if is_even_number == True else print('Число', number, 'Не чётное!')
print('')


    # №5
    #  Даны два слова. Проверьте, что первые буквы этих слов совпадают.
print(' Задача №1.1.5')
print('Первые буквы в словах', word1, 'и', word2, 'совпадают!' if word1[0] == word2[0] else 'Первые буквы в словах', word1, 'и', word2, 'не совпадают!')
print('')


    # №6
    # Дано слово. Получите его последнюю букву. Если слово заканчивается на мягкий знак, то получите предпоследнюю букву.
print(' Задача №1.1.6')
 
if word1[-1] == 'ь':
    last_char_of_word1 = word1[-1]
    print('Последняя буква в слове', word1, '-', last_char_of_word1) 
else:
    last_char_of_word1 = word1[-2]
    print('Последняя буква в слове', word1, '-', last_char_of_word1)
print('')


    # УРОВЕНЬ 1.2


    # №1
    # Дано число. Выведите в консоль первую цифру этого числа.
print(' УРОВЕНЬ 1.2')
print(' Задача №1.2.1')
first_digit_of_number = int(str(number)[0])   # преобразовываю число в текст, получаю первый символ, преобразовываю его обратно в число
print('Первая цифра числа', number, '-', first_digit_of_number)
print('')


    # №2
    # Дано число. Выведите в консоль последнюю цифру этого числа.
print(' Задача №1.2.2')
last_digit_of_number = int(str(number)[-1])   # преобразовываю число в текст, получаю первый символ, преобразовываю его обратно в число
print('Последняя цифра числа', number, '-', last_digit_of_number)
print('')


    # №3
    # Дано число. Выведите в консоль сумму первой и последней цифры этого числа.
print(' Задача №1.2.3')
sum_of_digits = first_digit_of_number + last_digit_of_number
print('Сумма первой и последней цифер числа', number, '-', sum_of_digits)
print('')


    # №4
    # Дано число. Выведите количество цифр в этом числе.
print(' Задача №1.2.4')
amount_of_digits = len(str(number)) # преобразовываю число в строку и получаю длину строки
print('Количество цифр в числе', number, '-', amount_of_digits)
print('')


    # №5
    # Даны два числа. Проверьте, что первые цифры этих чисел совпадают.
print(' Задача №1.2.5')
digits_match = True if int(str(number)[0]) == int(str(number1)[0]) else False
print('Первые цифры чисел', number, 'и', number1, 'НЕ совпадают!') if digits_match == False else print('Первые цифры чисел', number, 'и', number1, 'совпадают!')
print('')


    # №6
    # Дан список:
    # [1, 2, 3, 4, 5, 6]
    # Получите из него следующий срез:
    # [1, 2, 3]
print(' Задача №1.2.6')
print('Полный список:', digits_list)
print('Первые три элемента из списка:', digits_list[:3]) # первые три элемента из списка 
print('Элементы из списка с 2 по 5:', digits_list[2:5]) # элементы из списка с 2 по 5
print('Элементы из списка с шагом через 1:', digits_list[::2]) # элементы из списка с шагом через 1
print('')


    # УРОВЕНЬ 1.3


    # №1
    # Дана строка. Если в этой строке более одного символа, выведите в консоль предпоследний символ этой строки.
print(' УРОВЕНЬ 1.3')
print(' Задача №1.3.1')
if len(string) > 1:
    print('Предпоследний символ строки:', '"' + string + '"','-', string[-2] )
print('')


    # №2
    # Даны два целых числа. Проверьте, что первое число без остатка делится на второе.
print(' Задача №1.3.2')
remains = number % number1
print('Число', number, 'делится на число', number1, 'без остатка!') if remains == 0 else print('Число', number, 'НЕ делится на число', number1, 'без остатка! Остаток:', remains )
print('')


    # №3
    # Дана некоторая строка, получите список ее символов
print(' Задача №1.3.3')
print('Список символов строки: ', list(string))
print('')


    # №4
    # Дан список: [1, 2, 3, 4, 5, 6]. Получите из него следующий срез: [3, 4, 5].
print(' Задача №1.3.4')
print('Полный список:', digits_list)
print('Первые три элемента из списка:', digits_list[:3]) # первые три элемента из списка 
print('Элементы из списка с 2 по 5:', digits_list[2:5]) # элементы из списка с 2 по 5( 5 не включается)
print('Элементы из списка с шагом через 1:', digits_list[::2]) # элементы из списка с шагом через 1
print('')


    # №5 Дан словарь с датой:

    # {
    # 	'year' : '2025',
    # 	'month': '12',
    # 	'day'  : '31',
    # }
    # Из элементов этого словаря соберите дату в следующем формате:

    # '2025-12-31'
print(' Задача №1.3.5')
print(date_dict['day']+'.'+date_dict['month']+'.'+date_dict['year']) #формат dd.mm.yyyy
print(date_dict['year']+'-'+date_dict['month']+'-'+date_dict['day']) #формат yyyy-mm-dd
print('')



    # УРОВЕНЬ 1.4


    # №1 
    # Выведите в консоль все целые числа от 1 до 100.
print(' УРОВЕНЬ 1.4')
print(' Задача №1.4.1')
for i in digits_range1:
    print(i, end=' ') # вывожу в строку, для удобности отображения
print('')


    # №2 
    # Выведите в консоль все целые числа от -100 до 1.
print(' Задача №1.4.2')
for i in digits_range2:
    print(i, end=' ') # вывожу в строку, для удобности отображения
print('')


    # №3 
    # Выведите в консоль все целые числа от 100 до 1.
print(' Задача №1.4.3')
for i in digits_range3:
    print(i, end=' ') # вывожу в строку, для удобности отображения
print('')


    # №4 
    # Выведите в консоль все четныe целые числа из промежутка от 1 до 100.
print(' Задача №1.4.4')
for i in digits_range1:
    if i % 2 == 0:
        print(i, end=' ') # вывожу в строку, для удобности отображения
print('')


    # №5 
    # Выведите в консоль все числа кратные 3 из промежутка от 1 до 100.
print(' Задача №1.4.5')
for i in digits_range1:
    if i % 3 == 0:
        print(i, end=' ') # вывожу в строку, для удобности отображения
print('')


    # №6
    # Дан список:
    # [1, 2, 3, 4, 5, 6]
    # Получите из него два последних элемента:
    # [5, 6]
print(' Задача №1.4.6')
print('Полный список:', digits_list)
print('Последние два элемента из списка:', digits_list[4:]) # последние два элемента из списка 
print('')


    # №7
    # Дана некоторая строка:
    # 'abcdeabc'
    # Получите сет ее символов:
    # {'a', 'b', 'c', 'd', 'e'}
print(' Задача №1.4.7')
print('Полная строка:', '"' + string + '"')
print('Сет(Уникальные символы) из строки:', set(string))  
print('')



    # УРОВЕНЬ 1.5


    # №1 Найдите сумму всех целых чисел от 1 до 100.
print(' УРОВЕНЬ 1.5')
print(' Задача №1.5.1')
sum_number = 0
for i in digits_range1:
    sum_number += i
print ('Сумма всех целых чисел от 1 до 100 =', sum_number)
print('')


    # №2 Найдите сумму всех целых четных чисел от 1 до 100.
print(' Задача №1.5.2')
sum_even = 0
for i in digits_range4:
    sum_even += i
print ('Сумма всех целых четных чисел от 1 до 100 =', sum_even)
print('')


    # №3 Найдите сумму всех целых нечетных чисел от 1 до 100.
print(' Задача №1.5.3')
sum_odd = 0
for i in digits_range1:
    if i % 2 != 0:
        sum_odd += i
print ('Сумма всех целых НЕчетных чисел от 1 до 100 =', sum_odd)
print('')


    # №4 Даны два целых числа. Найдите остаток от деления первого числа на второе.
print(' Задача №1.5.4')
remains = number % number1
print('Остаток от деления', number, 'на', number1, 'равен', remains)
print('')


    # №5
    # Дан список:
    # [1, 2, 3, 4, 5, 6]
    # Получите из него каждый второй элемент:
    # [1, 3, 5]
print(' Задача №1.5.5')
print('Полный список:', digits_list)
print('Первые три элемента из списка:', digits_list[:3]) # первые три элемента из списка (список[:stop]) / (список[start:]) - от указанного элемента до последнего
print('Элементы из списка с 2 по 5:', digits_list[2:5]) # элементы из списка с 2 по 5( 5 не включается) (список[start:stop])
print('Элементы из списка с шагом через 1:', digits_list[::2]) # элементы из списка с шагом через 1 (список[start:stop:step])
print('')
    
    
    
    #УРОВЕНЬ 1.6


    # №1
    # Дан список с числами:
    # [1, 2, 3, 4, 5, 6]
    # Найдите сумму элементов этого списка.
print(' УРОВЕНЬ 1.6')
print(' Задача №1.6.1')
sum_number = 0
for i in digits_list:
    sum_number += i
print('Полный список:', digits_list)
print('Сумма элементов этого списка =',sum_number)
print('')


    # №2
    # Дан список с числами:
    # [1, 2, 3, 4, 5, 6]
    # Найдите сумму квадратов элементов этого списка.
print(' Задача №1.6.2')
sum_number = 0
sum_number_full = 0
print('Полный список:', digits_list)
for i in digits_list:
    sum_number = i
    sum_number_sq = sum_number**2
    sum_number_full += sum_number_sq
    print(sum_number_sq)
print('Сумма квадратов элементов этого списка =',sum_number_full)
print('')


    # №3
    # Дан список с числами:
    # [1, 2, 3, 4, 5, 6]
    # Найдите сумму квадратных корней элементов этого списка.
print(' Задача №1.6.3')
sum_number = 0
sum_number_full = 0
print('Полный список:', digits_list)
for i in digits_list:
    sum_number = i
    sum_number_sq = sum_number**0.5
    sum_number_full += sum_number_sq
    print(sum_number_sq)
print('Сумма квадратных корней элементов этого списка =',sum_number_full)
print('')


    # №4
    # Дан список с числами:
    # [1, 2, -3, 4, -5]
    # Найдите сумму положительных элементов этого списка.
print(' Задача №1.6.4')
sum_number = 0
print('Полный список:', digits_list1)
for i in digits_list1:
    if i > 0:
        sum_number += i
print('Сумма положительных элементов этого списка =', sum_number)
print('')


    # №5
    # Дан список с числами:
    # [1, 2, -3, 4, 5, 11]
    # Найдите сумму положительных элементов этого списка.
print(' Задача №1.6.5')
sum_number = 0
print('Полный список:', digits_list2)
for i in digits_list2:
    if 10 >= i > 0:
        sum_number += i
print('Сумма положительных элементов этого списка =', sum_number)
print('')


    # №6
    # Дана некоторая строка:
    # Переберите и выведите в консоль по очереди все символы с конца строки.
print(' Задача №1.6.6')
print('Полная строка:', '"' + string + '"')
string_list = list(string)
reversed_string_list = list(string)[::-1]
print(string_list)
print(reversed_string_list)
print('')



    # УРОВЕНЬ 1.7


    # №1
    # Дан словарь:
    # {
    #     'a': 1,
    #     'b': 2,
    #     'c': 3, 
    #     'd': 4,
    # }
    # Найдите сумму элементов этого словаря.
print(' УРОВЕНЬ 1.7')
print(' Задача №1.7.1')
#result = digits_dict['a'] + digits_dict['b'] + digits_dict['c'] + digits_dict['d']         # мой способ, правильный, но неоптимизированный
result = 0
for i in digits_dict.values():                                                           # у словарей есть метод .values(), он выводит значения по очереди, как в списках
    result += i                                                                         # а есть метод .key(), он выводит ключ, без присвоенного ему значения
print('Сумма всех элементов словаря равна ', result)
print('')


    # №2
    # Дан словарь:
    # {
    #     'a': 1,
    #     'b': 2,
    #     'c': 3, 
    #     'd': 4,
    # }
    # Найдите сумму квадратов этого словаря.
print(' Задача №1.7.2')
result = 0
result_sq = 0
full_result = 0
for i in digits_dict.values():
    result = i                                                           
    result_sq = result ** 2 
    full_result += result_sq 
    print(result_sq)                                                                      
print('Сумма всех квадратов словаря равна ', full_result)
print('')


    # №3
    # Дана строка. Получите список букв этой строки.
print(' Задача №1.7.3')
print('Полная строка:', '"' + string + '"')
print('Сет(Уникальные символы) из строки:', set(string))
print('Cписок уникальных букв этой строки: ', list(set(string)))
print('')


    # №4
    # Дано число. Получите список цифр этого числа.
print(' Задача №1.7.4')
numbers = [int(d) for d in str(number)]    # [] - это метод list comprehension, посимвольно преобразовывает строчный символ, например: '2' в цифру 2
print('Полное число:', '"' + str(number) + '"')
print('Cписок цифр этого числа: ', numbers)
print('')


    # №5
    # Дано некоторое число
    # Переверните его:
print(' Задача №1.7.5')
numbers = [int(d) for d in str(number)[::-1]]
print('Полное число:', '"' + str(number) + '"')
print('Перевернутый список цифр этого числа :' , numbers)
print('')


    # №6
    # Дано некоторое число
    # Найдите сумму цифр этого числа:
print(' Задача №1.7.6')
numbers = [int(d) for d in str(number)]
print('Полное число:', '"' + str(number) + '"')
print('Список цифр этого числа : ', numbers)
num = 0
sum_num = 0
for num in numbers:
    num += num
    sum_num += num
    print(num)
print('Сумма цифр этого числа : ', sum_num)
print('')

    # УРОВЕНЬ 1.8


    # №1
    # Дан кортеж с числами:
    # (1, 2, 3, 4, 5)
    # Найдите сумму элементов этого кортежа.
print(' УРОВЕНЬ 1.8')
print(' Задача №1.8.1')
print('Кортеж:', digits_tuple)
sum_num = 0
for num in digits_tuple:
    sum_num += num
    print(num)
print('Сумма цифр этого кортежа : ', sum_num)
print('')


    # №2
    # Дан список с числами:
    # Увеличьте каждое число из списка на 10 процентов.
print(' Задача №1.8.2')
print('Список чисел:', digits_list)
sum_num = 0
for num in digits_list:
    sum_num = num * 1.1
    print(f'Число {num}, увеличенное на 10% = {sum_num:.2f}')    # f самый современный способ форматирования строки вывода! нужно использовать его. Переменные в него передаются в {} таких скобках.
print('')


    # №3
    # Дана строка. Получите первых три символа этой строки
print(' Задача №1.8.3')
print(f'Первые три символа строки "{string}" это - {list(string[0:3])}')
print('')



    # УРОВЕНЬ 1.9


    # №1
    # # Дана строка. Получите три последних символа этой строки
print(' Задача №1.9.1')
print(f'Последние три символа строки "{string}" это - {list(string[-3:])}')
print('')


    # №2
    # Дан словарь с числами, величьте каждое число из словаря в 2 раза
print(' Задача №1.9.2')
multip_num = 0
for key, value in digits_dict.items():
    multip_num = value * 2
    print(f'Для ключа {key} число {value}, увеличенное в 2 раза = {multip_num}')
print('')



    # УРОВЕНЬ 1.10


    # №1
    # # Дана строка. Получите каждый второй символ этой строки
print(' Задача №1.10.1')
print(f'Каждый второй символ строки "{string}" это - {list(string[::2])}')
print('')


    # №2
    # Дано некоторое число. Выведите в консоль все его символы с конца.
print(' Задача №1.10.2')
numbers = [int(d) for d in str(number)]    # [] - это метод list comprehension, посимвольно преобразовывает строчный символ, например: '2' в цифру 2
print(f'Полное число: {str(number)}')
print('Cписок цифр этого числа: ', numbers[::-1])
print('')



    # УРОВЕНЬ 2.1


    # №1 Дан список со строками. Оставьте в этом списке только те строки, которые начинаются на http://.
print('УРОВЕНЬ 2.1')
print(' Задача №2.1.1 (моё решение)')                     # решение НЕ верное, выводит лишние строки(не могу понять почему)
http_strings = strings.copy()  
start_string = 'http://'                                                    # метод .copy() создает копию списка strings в переменной http_strings, без этого метода - 
i = 0                                                                               # переменная http_strings будет ссылаться на список strings и изменения будут происходить в нем
print('Список всех строк: ', *http_strings, '', sep = '\n')        # sep = '\n' - переход на новую строку в конце каждой строки, * - все строки списка
for current_string in http_strings:
    if current_string[:7] != start_string:
        del http_strings[i]
        i += 1
    if current_string[:7] == start_string:
        i += 1
print('Строки начинающиеся на http:// : ',*http_strings, sep = '\n')
print('')
print(' Задача №2.1.1 (deepseek gpt решение)')     # верное и короткое решение. ВЫВОД - нужно использовать list_comprehension
print('Список всех строк: ', *strings, '', sep = '\n')                                                       
http_strings = [current_string for current_string in strings if current_string.startswith('http://')]         # list_comprehension
print('Строки начинающиеся на http:// : ',*http_strings, sep = '\n')
print('')


    # №2 Дана некоторая строка. Найдите позицию первой буквы 'c' в строке.
print(' Задача №2.1.2')
item_to_find = 'с'
print(string) 
print(f'Позиция первого символа "{item_to_find}" : \n{string.find(item_to_find)} - по логике Python c отсчетом от 0 \n{string.find(item_to_find)+1} - по порядку')
print(f'{string.lower().find(item_to_find)} - без учёта регистра "c" "C" по логике Python c отсчетом от 0')
print(f'{string.lower().find(item_to_find)+1} - без учёта регистра "c" "C" по порядку')
print('')


    # №3 Дан список. Удалите из него элементы с заданным значением.
print(' Задача №2.1.3')
print(f'Дан список: {digits_list} \nНужно удалить из него 3 элемент по порядку.')
shorted_digits_list = digits_list.copy()
del shorted_digits_list[2]
print(f'Новый список: {shorted_digits_list}')
print('')


    # №4 Выведите в консоль все числа в промежутке от 10 до 1000, сумма первой и второй цифры которых равна пяти.
print(' Задача №2.1.4')
x = range(10, 1001)
for i in x:
    sum_c = int(str(i)[0]) + int(str(i)[1])
    if sum_c == 5:
        print(f'Сумма первых двух цифр числа {i} = {sum_c}')
print('')


    # №5 Дана некоторая строка. Очистите ее от дублей символов.
print(' Задача №2.1.5')
unic_symbols_of_string = ''.join(set(string.lower())) 
unic_symbols_of_string1 = ''.join(set(string))

unic_symbols_of_string2 = ''
for i in string:
    if i not in unic_symbols_of_string2:
        unic_symbols_of_string2 += i 

unic_symbols_of_string3 = ''
for i in string:
    if i.lower() not in unic_symbols_of_string3.lower():
        unic_symbols_of_string3 += i.lower()

print(f'Уникальные символы из строки "{string}" : \n{unic_symbols_of_string} - без учета регистра и не по порядку.')
print(f'{unic_symbols_of_string1} - с учётом регистра и не по порядку.')
print(f'{unic_symbols_of_string2} - с учётом регистра и по порядку.')
print(f'{unic_symbols_of_string3} - без учета регистра и по порядку.')
print('')


    # УРОВЕНЬ 2.2


    # №1 Дан список с числами. Подсчитайте количество отрицательных чисел в этом списке.
print(' УРОВЕНЬ 2.2')
print(' Задача №2.2.1')
neg_num = 0
for i in numbers_list:
    if i < 0:
        neg_num += 1
print(f'Список чисел: {numbers_list}\nОтрицательных чисел в нем: {neg_num}')
print('')



    # №2 Дан список с числами. Оставьте в нем только положительные числа.
print(' Задача №2.2.2')
numbers_list_copy = [pos for pos in numbers_list if pos > 0 ]

print(f'Список чисел: {numbers_list}\nСписок без отрицательных чисел: {numbers_list_copy}')
print('')


    # №3 Дана строка. Удалите предпоследний символ из этой строки.
print(' Задача №2.2.3')
def cutting_string():      #если вдруг переменные еще понадобятся
    cutted_string = list(string)
    space = ' '
    del cutted_string[-2]
    cutted_string = ''.join(cutted_string) # ''.join() складывает элементы списка в строку
    print(f'Строка:{space*29}"{string}"\nСтрока без предпосленднего символа: "{cutted_string}"')
cutting_string()
print('')



    #№4 Дан список со строками. Оставьте в этом списке только те строки, которые заканчиваются на .html.
print(' Задача №2.2.4')   
def filter_html():
    filtered_strings = [string for string in strings if string.endswith('.html')]
    print('Список всех строк: ', *strings, '', sep = '\n')
    print('Список строк заканчивающихся на ".html" : ', *filtered_strings, '', sep = '\n')
filter_html()
print('')



    # №5 Дан список с дробями. Округлите эти дроби до одного знака в дробной части.
print(' Задача №2.2.5')
print('Список дробей: ', *float_numbers_list, '', sep = '\n')
def rounding():
    float_numbers_list_copy = float_numbers_list.copy()
    rounded_list = [round(i, 1) for i in float_numbers_list_copy]
    print('Список округленных дробей: ', *rounded_list, '', sep = '\n')
rounding()



    # №6 Дан словарь. Получите список его значений: [1, 2, 3, 4]
print(' Задача №2.2.6')
def dict_to_list():
    digits_dict_list = [value for value in digits_dict.values()]
    print(f'Словарь : {digits_dict}')
    print(f'Список значений из словаря : {digits_dict_list}')
dict_to_list()



# УРОВЕНЬ 2.3


    # №1 Даны два слова. Проверьте, что последняя буква первого слова совпадает с первой буквой второго слова.
print(' УРОВЕНЬ 2.3')
print(' Задача №2.3.1')
def words_eq():
    eq = True if word1[0] == word2[0] else False
    print(f'Первые буквы в словах {word1} и {word2} совпадают!') if eq == True else print(f'Первые буквы в словах {word1} и {word2} НЕ совпадают!')
words_eq()
print()



    # №2 Дана некоторая строка. Найдите позицию третьего буквы 'c' в строке.
print(' Задача №2.3.2')
def simbol_find(text, simbol):                                      # создаем функцию с 2мя переменными: строкой и искомым символом
    first_simbol = text.find(simbol)                                # ищем первое вхождения символа в строку
    if first_simbol == -1:                                          # если найдено первый раз - возвращает -1
        return -1
    second_simbol = text.find(simbol, first_simbol + 1)             # ищем второе вхождения символа в строку (индекс первого вхождения +1)
    if second_simbol == -1:                                         # если найдено второй раз - возвращает -1
        return -1
    third_simbol = text.find(simbol, second_simbol + 1)             # ищем третье вхождения символа в строку (индекс второго вхождения +1)
    return third_simbol                                             # если найдено третий раз - возвращает уже искомый индекс
print(f'Третья буква "с" в строке: "{string}" попадается на : {simbol_find(string, "с")} позиции!\n')



    # №3 Даны числа, разделенные запятыми: '12,34,56'. Найдите сумму этих чисел.
print(' Задача №2.3.3')
def summing_numbers_in_string():
    numbers = sum( [int(x) for x in numbers_string.split(',')] ) #list comprehencion с разделением элементов по ',' и переводом их в число
    print(f'Сумма чисел в строке {numbers_string} = {numbers}')
summing_numbers_in_string()
print('')



    # №4 Дана дата в следующем формате:

        # '2025-12-31'
        # Преобразуйте эту дату в следующий словарь:

        # {
        #     'year' : '2025',
        #     'month': '12',
        #     'day'  : '31',
        # }

print(' Задача №2.3.4')
def date_to_dict():
    year, month, day = date.split('-')  # разделяю строку на переменные по порядку через '-'
    date_to_dict = {
        'year' : year,
        'month' : month,
        'day' : day 
    }     
    print(date_to_dict, '\n')
date_to_dict()



    # №5 Дан словарь. Получите сет его значений.
print(' Задача №2.3.5')
def dict_values_set():
    dict_values_set = set(digits_dict.values())
    print(dict_values_set, '\n')
dict_values_set()



    # УРОВЕНЬ 2.4
    # №1 Дана некоторая строка с буквами и цифрами. Получите позицию первой цифры в этой строке.
print(' УРОВЕНЬ 2.4')
print(' Задача №2.4.1')
def first_digit_of_str():
    s = 'x1a2b3c4d'
    for i, d in enumerate(s): # enumerate()  создает список пар из символов строки s - (0, x), (1, 1), (2,a), (3,2), (4, b) и т.д
        if d.isdigit():
            print(f'Позиция первой цифры в строке: "{s}" - {i}', '\n')
            break
first_digit_of_str()



    # №2 Дано число. Выведите в консоль количество четных цифр в этом числе.
print(' Задача №2.4.2')
def count_even_digits():
    count = 0
    number_list = [int(k) for k in str(number)]
    for i in number_list:
        if i % 2 == 0:
            count += 1
    print(number, count, '\n') 
count_even_digits()



    # №3 Дан словарь:
    # {
    # 	'a': 1,
    # 	'b': 2,
    # 	'c': 3, 
    # 	'd': 4,
    # }
    # Получите список его ключей:
    # ['a', 'b', 'c', 'd']
print(' Задача №2.4.3')
def dict_keys_set():
    dict_keys_set = list(digits_dict.keys())
    print(dict_keys_set, '\n')
dict_keys_set()



    # №4 Дана некоторая строка.Переведите в верхний регистр все нечетные буквы этой строки.
print(' Задача №2.4.4')
def upper_odd_chars():
    print(string)
    new_string = ''.join(char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(string))
    print(new_string, '\n')
upper_odd_chars() 



    # №5 Дана некоторая строка со словами. Сделайте заглавным первый символ каждого слова в этой строке.
print(' Задача №2.4.5')
def upper_words_first_symbol():
    print(string)
    new_string = string.title()    #делает все слова с залавной буквы, встроенная функция python
    print(new_string, '\n')
upper_words_first_symbol()



    # №6 Дана дата в следующем формате:
    #   '2025-12-31'
    #   Преобразуйте эту дату в следующий кортеж:
    #   ('31', '12', '2025')
print(' Задача №2.4.6')
def date_to_tuple():
    print(date)
    date_tuple = tuple(date.split('-'))[::-1] 
    print(date_tuple, '\n')
date_to_tuple()



    # УРОВЕНЬ 2.5
    # №1 Дана некоторая строка, например, вот такая:
    # '023m0df0dfg0'
    # Получите сет позиций всех нулей в этой в строке.
print(' УРОВЕНЬ 2.5')
print(' Задача №2.5.1')
def find_zeroes_positions_set():
    any_string = '023m0df0dfg0'
    zeroes_positions_set = {i for i, char in enumerate(any_string) if char == '0'}
    print(zeroes_positions_set, '\n')
find_zeroes_positions_set()



    # №2 Дана некоторая строка. Удалите из этой строки каждый третий символ.
print(' Задача №2.5.2')
def delete_every_third_simbol():
    print(string)
    new_string = ''.join([char for i, char in enumerate(string)  if (i+1) % 3 != 0])
    print(new_string, '\n')
delete_every_third_simbol()

#1233
print('test')