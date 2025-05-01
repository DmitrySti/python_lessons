year = int(input('Введите год, на который хотите получить календарь: '))
months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

def is_leap_year(year):        # Функция, вычисляющая, високосный ли год.
    if year % 4 != 0:
        is_leap = False
    else:
        is_leap = True

    if year % 100 == 0:
        is_leap = False
    if year % 400 == 0:
        is_leap = True
    return is_leap


def get_duration(year_value, month_index):        # Функция, вычисляющая количество дней в месяце.
    if month_index in [3, 5, 8, 10]:
        duration = 30
    elif month_index == 1:
        duration = 29 if is_leap_year(year_value) else 28
    else:
        duration = 31

    return duration


def print_days(days_in_month, start_day):          # Функция, печатающая даты месяца.
    print('   ' * start_day, end='')
    for day in range(1, days_in_month + 1):
        if day < 10:
            print(day, end='  ')
        else:
            print(day, end=' ')
        if (day + start_day) % 7 == 0:
            print()
    if (days_in_month + start_day) % 7 != 0:
        print()


def print_header(year_value, month_index):      # Функция, печатающая шапку месяца.
    print(months[month_index], year_value)
    print('Пн Вт Ср Чт Пт Сб Вс')


def get_starting_day(year):       # Функция, вычисляющая день недели, который приходится на 1 января:
    d = 1
    m = 13
    y = year - 1
    h = (d + (13 * (m + 1)) // 5 + y + (y // 4) - (y // 100) + (y // 400)) % 7
    return (h + 5) % 7


def adjust_start_day(start_day, days_in_month):          # Функция, вычисляющая день недели,
    result = (start_day + days_in_month) % 7             # на который выпадет первое число следующего месяца:
    return result


def print_calendar(year):            # Финальная функция, выводящая календарь 
    start_day = get_starting_day(year)

    for month_number in range(12):
        print_header(year, month_number)
        duration = get_duration(year, month_number)
        print_days(duration, start_day)

        start_day = adjust_start_day(start_day, duration)
        print()

print_calendar(year)
input()