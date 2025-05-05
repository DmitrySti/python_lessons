import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_my_calendar_interface import Ui_MainWindow  # Импортируем сгенерированный класс

class MyWindow(QMainWindow, Ui_MainWindow):  # Наследуемся от обоих классов
    def __init__(self):
        super().__init__()  # Инициализируем QMainWindow
        self.setupUi(self)  # Загружаем интерфейс из Ui_MainWindow

        # Теперь все виджеты доступны через self:
        self.pushButton.clicked.connect(self.on_button_click)

    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

    def is_leap_year(self, year):        # Функция, вычисляющая, високосный ли год.
            if year % 4 != 0:
                is_leap = False
            else:
                is_leap = True

            if year % 100 == 0:
                is_leap = False
            if year % 400 == 0:
                is_leap = True
            return is_leap


    def get_duration(self, year_value, month_index):        # Функция, вычисляющая количество дней в месяце.
            if month_index in [3, 5, 8, 10]:
                duration = 30
            elif month_index == 1:
                duration = 29 if self.is_leap_year(year_value) else 28
            else:
                duration = 31

            return duration


    def print_days(self, days_in_month, start_day):          # Функция, печатающая даты месяца.
            print('   ' * start_day, end='')
            self.textEdit.insertPlainText('   ' * start_day)
            for day in range(1, days_in_month + 1):
                if day < 10:
                    print(day, end='  ')
                    self.textEdit.insertPlainText(f"{day}  ")
                else:
                    print(day, end=' ')
                    self.textEdit.insertPlainText(f"{day} ")
                if (day + start_day) % 7 == 0:
                    print()
                    self.textEdit.append("")
            if (days_in_month + start_day) % 7 != 0:
                print()
                self.textEdit.append("")
            self.textEdit.insertPlainText(f'{"_"*20}\n')


    def print_header(self, year_value, month_index):      # Функция, печатающая шапку месяца.
            print(self.months[month_index], year_value)
            self.textEdit.insertPlainText(f'\n{self.months[month_index]} {year_value}')
            print('Пн Вт Ср Чт Пт Сб Вс')
            self.textEdit.insertPlainText('\nПн Вт Ср Чт Пт Сб Вс\n')


    def get_starting_day(self, year):       # Функция, вычисляющая день недели, который приходится на 1 января:
            d = 1
            m = 13
            y = year - 1
            h = (d + (13 * (m + 1)) // 5 + y + (y // 4) - (y // 100) + (y // 400)) % 7
            return (h + 5) % 7


    def adjust_start_day(self, start_day, days_in_month):          # Функция, вычисляющая день недели,
            result = (start_day + days_in_month) % 7             # на который выпадет первое число следующего месяца:
            return result


    def print_calendar(self, year):            # Финальная функция, выводящая календарь 
            start_day = self.get_starting_day(year)

            for month_number in range(12):
                self.print_header(year, month_number)
                duration = self.get_duration(year, month_number)
                self.print_days(duration, start_day)

                start_day = self.adjust_start_day(start_day, duration)
                print()


    def on_button_click(self):
        year = int(self.year_edit.text())
        self.print_calendar(year)


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()


    
