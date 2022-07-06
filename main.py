import sys
import datetime
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QInputDialog, QListWidgetItem
import sqlite3
from PyQt5.QtGui import QPixmap


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('index.ui', self)  # Загружаем дизайн
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MuscleIT')

        # 1-ая кнопка Меню
        self.pushButton.clicked.connect(self.exercises)  # Кнопка открытия "Упрпжнения"

        # 2-ая кнопка Меню
        self.pushButton_2.clicked.connect(self.data)  # Кнопка открытия "Упрпжнения"

        # 3-ая кнопка Меню
        self.pushButton_3.clicked.connect(self.programm)  # Кнопка открытия "Программа"

        # 4-ая кнопка Меню
        self.pushButton_4.clicked.connect(self.about_app)  # Кнопка открытия "О приложении"

    def about_app(self):
        #  Закрытие меню и открытие дочернего окна "О приложении"
        self.close()
        self.About_app = About_app()
        self.About_app.show()

    def exercises(self):
        #  Закрытие меню и открытие дочернего окна "О приложении"
        self.close()
        self.exercises = Exercises()
        self.exercises.show()

    def data(self):
        #  Закрытие меню и открытие дочернего окна "О приложении"
        self.close()
        self.data = Data()
        self.data.show()

    def programm(self):
        #  Закрытие меню и открытие дочернего окна "О приложении"
        self.close()
        self.programm = Programm()
        self.programm.show()


class About_app(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('About_App.ui', self)  # Загружаем дизайн
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MuscleIT')

        self.pushButton.clicked.connect(self.menu)  # Кнопка открытия Меню

        #  Текст о приложении
        self.plainTextEdit.insertPlainText('Это приложение, в котором вы можете составлять свою тренировку,'
                                           'смотреть как делать то или иное упражнение, записывать свои физ.'
                                           'данные.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText('Этот проект рассчитан на людей, которые занимаются спортом,ходят в зал.'
                                           ' Но не каждый может составить план тренировок. Для этого и есть это '
                                           'приложение.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText('Во вкладке "упражнения" вы можете посмотреть то или иное упражнение,'
                                           'как его делать и сколько его нужно выполнять.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText('Во вкладке "Данные" вы можете записывать свои данные, которые '
                                           'влияют на составление программы для вас.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText('Во вкладке "Программа тренировки" вы можете посмотреть свою программу '
                                           'тренировок, которая составлена на основе ваших данных и предпочтений,'
                                           'которые были указаны во вкладке "Данные". Без данных, программу тренировки '
                                           ' составить невозможно.')

    def menu(self):
        #  Закрытие открытие дочернего окна "О приложении" и открытие окна
        self.close()
        self.Menu = Menu()
        self.Menu.show()


class Exercises(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Exercises.ui', self)  # Загружаем дизайн
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MuscleIT')

        self.pushButton.clicked.connect(self.menu)  # Кнопка открытия Меню
        self.pushButton_2.clicked.connect(self.run)

    def menu(self):
        #  Закрытие открытие дочернего окна "О приложении" и открытие окна
        self.close()
        self.Menu = Menu()
        self.Menu.show()

    def run(self):
        con = sqlite3.connect('Exersises.db')

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        result = cur.execute("""SELECT Name FROM Exersises""").fetchall()

        # Вывод результатов на экран
        list_of_exersices = list()
        for elem in result:
            list_of_exersices.append(str(elem[0]))
        con.close()
        exersice, ok_pressed = QInputDialog.getItem(
            self, "Выберите упражнение", "Выберите упражнение",
            (tuple(list_of_exersices)), 0, False)
        # изменяем картинку и текст
        if ok_pressed:
            con = sqlite3.connect('Exersises.db')
            cur = con.cursor()
            name_of_image = cur.execute(f"""SELECT image_id FROM Exersises
                        WHERE Name = '{exersice}'""").fetchone()
            pixmap = QPixmap(f'exersices/{name_of_image[0]}')
            self.label_2.setPixmap(pixmap)

            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(exersice)
            self.plainTextEdit.insertPlainText('\n')
            self.plainTextEdit.insertPlainText(' ')
            self.plainTextEdit.insertPlainText('\n')
            text_of_exersice = cur.execute(f"""SELECT text FROM Exersises
                                    WHERE Name = '{exersice}'""").fetchone()
            self.plainTextEdit.insertPlainText(text_of_exersice[0])


class Data(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Data.ui', self)  # Загружаем дизайн
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MuscleIT')
        self.COMPLETION = 1
        self.COUNT_OF_DATA = 0
        self.HEIGHT_RIGHT = False
        self.WEIGHT_RIGHT = False
        self.AGE_RIGHT = False
        self.gender = 'Мужской'

        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()

        self.pushButton.clicked.connect(self.menu)  # Кнопка открытия Меню

        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)

        self.radioButton.setEnabled(False)
        self.radioButton_2.setEnabled(False)
        self.radioButton.setChecked(True)
        self.pushButton_3.hide()

        self.pushButton_2.clicked.connect(self.run)

        con = sqlite3.connect('Data.db')
        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        count_of_data = cur.execute("""SELECT * FROM Data 
                                            """).fetchall()

        # Вывод результатов на экран
        for elem in count_of_data:
            listWidgetItem = QListWidgetItem(f'Дата: {elem[5]}  Рост: {elem[1]}, Вес: {elem[2]}, '
                                             f'Возраст: {elem[3]}, '
                                             f'Пол: {elem[4]}')
            self.listWidget.addItem(listWidgetItem)

        con.close()

    def menu(self):
        #  Закрытие открытие дочернего окна "О приложении" и открытие окна
        self.close()
        self.Menu = Menu()
        self.Menu.show()

    def run(self):
        #  При заполнении кнопка становится Отмена,при обратном Заполнить
        if self.COMPLETION == 0:
            self.pushButton_2.setText('Заполнить')
            self.COMPLETION = 1

            self.lineEdit.setReadOnly(True)
            self.lineEdit_2.setReadOnly(True)
            self.lineEdit_3.setReadOnly(True)

            self.radioButton.setEnabled(False)
            self.radioButton_2.setEnabled(False)
            self.pushButton_3.hide()

            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
        else:
            self.pushButton_2.setText('Отмена')
            self.COMPLETION = 0
            self.lineEdit.setReadOnly(False)
            self.lineEdit_2.setReadOnly(False)
            self.lineEdit_3.setReadOnly(False)
            self.pushButton_3.show()

            self.radioButton.setEnabled(True)
            self.radioButton_2.setEnabled(True)
            self.radioButton.clicked.connect(self.genders)
            self.radioButton_2.clicked.connect(self.genders)
            self.pushButton_3.clicked.connect(self.saving)

    def genders(self):
        if self.sender().text() == 'Мужчина':
            self.gender = 'Мужской'
        else:
            self.gender = "Женский"

    def saving(self):
        #  Проверяем нет ли ошибок в вводе,иначе высвечивается ошибка
        try:
            self.height = int(self.lineEdit.text())
            self.HEIGHT_RIGHT = True
            self.label_5.hide()
        except ValueError:
            self.HEIGHT_RIGHT = False
            self.label_5.show()

        try:
            self.weight = float(self.lineEdit_2.text())
            self.WEIGHT_RIGHT = True
            self.label_6.hide()
        except ValueError:
            self.WEIGHT_RIGHT = False
            self.label_6.show()

        try:
            self.age = int(self.lineEdit_3.text())
            self.AGE_RIGHT = True
            self.label_7.hide()
        except ValueError:
            self.AGE_RIGHT = False
            self.label_7.show()
        #  Если всё верно,то сначала записываем всё в лист ,а потом все данные отправляем в базу данных
        if self.HEIGHT_RIGHT and self.WEIGHT_RIGHT and self.AGE_RIGHT:
            now = datetime.datetime.now()
            listWidgetItem = QListWidgetItem(f'Дата: {str(now)[:10]}  Рост: {self.height}, Вес: {self.weight}, '
                                             f'Возраст: {self.age}, '
                                             f'Пол: {self.gender}')
            self.listWidget.addItem(listWidgetItem)

            con = sqlite3.connect('Data.db')
            count = 1

            # Создание курсора
            cur = con.cursor()

            # Выполнение запроса и получение всех результатов
            count_of_data = cur.execute("""SELECT * FROM Data 
                                    """).fetchall()

            # Вывод результатов на экран
            for elem in count_of_data:
                count += 1

            con.close()

            con = sqlite3.connect('Data.db')
            cur = con.cursor()

            cur.execute(f"INSERT INTO Data VALUES (?, ?, ?, ?, ?, ?)", (count, self.height, self.weight,
                                                                        self.age, self.gender, str(now)[:10]))
            con.commit()
            con.close()


class Programm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Programm.ui', self)  # Загружаем дизайн
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MuscleIT')
        self.COUNT_OF_PROGRAMM = 0

        self.pushButton_5.hide()

        self.pushButton.clicked.connect(self.menu)  # Кнопка открытия Меню
        self.pushButton_2.clicked.connect(self.run3)
        self.pushButton_3.clicked.connect(self.run2)
        self.pushButton_4.clicked.connect(self.run1)
        self.pushButton_5.clicked.connect(self.cancelled)

        self.label_2.hide()

    def cancelled(self):
        #  Если пользователь захотел закрыть окна
        if self.COUNT_OF_PROGRAMM == 1:
            self.n1.close()
            self.n_1.close()
            self.pushButton_5.hide()
        elif self.COUNT_OF_PROGRAMM == 2:
            self.n2.close()
            self.n_2.close()
            self.pushButton_5.hide()
        elif self.COUNT_OF_PROGRAMM == 3:
            self.n3.close()
            self.n_3.close()
            self.pushButton_5.hide()

    def run1(self):
        con = sqlite3.connect('Data.db')
        count = 0

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        height = cur.execute("""SELECT height FROM Data 
                                                                    """).fetchall()

        # Вывод результатов на экран
        for elem in height:
            count += 1

        con.close()
        if count == 0:
            self.label_2.show()
        else:
            self.n1 = Programm_N1()
            self.n1.show()
            self.n_1 = Programm_N_1()
            self.n_1.show()
            self.pushButton_5.show()
            if self.COUNT_OF_PROGRAMM == 2:
                self.n2.close()
                self.n_2.close()
            elif self.COUNT_OF_PROGRAMM == 3:
                self.n3.close()
                self.n_3.close()
            self.COUNT_OF_PROGRAMM = 1
            self.label_2.hide()

    def run2(self):
        con = sqlite3.connect('Data.db')
        count = 0

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        height = cur.execute("""SELECT height FROM Data 
                                                                            """).fetchall()

        # Вывод результатов на экран
        for elem in height:
            count += 1

        con.close()
        if count == 0:
            self.label_2.show()
        else:
            self.n2 = Programm_N2()
            self.n2.show()
            self.n_2 = Programm_N_2()
            self.n_2.show()
            self.pushButton_5.show()
            if self.COUNT_OF_PROGRAMM == 1:
                self.n1.close()
                self.n_1.close()
            elif self.COUNT_OF_PROGRAMM == 3:
                self.n3.close()
                self.n_3.close()
            self.COUNT_OF_PROGRAMM = 2
            self.label_2.hide()

    def run3(self):
        con = sqlite3.connect('Data.db')
        count = 0

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        height = cur.execute("""SELECT height FROM Data 
                                                                            """).fetchall()

        # Вывод результатов на экран
        for elem in height:
            count += 1

        con.close()
        if count == 0:
            self.label_2.show()
        else:
            self.n3 = Programm_N3()
            self.n3.show()
            self.n_3 = Programm_N_3()
            self.n_3.show()
            self.pushButton_5.show()
            if self.COUNT_OF_PROGRAMM == 2:
                self.n2.close()
                self.n_2.close()
            elif self.COUNT_OF_PROGRAMM == 1:
                self.n1.close()
                self.n_1.close()
            self.COUNT_OF_PROGRAMM = 3
            self.label_2.hide()

    def menu(self):
        #  Закрытие открытие дочернего окна "О приложении" и открытие окна
        self.close()
        self.Menu = Menu()
        self.Menu.show()
        #  Сделанно потму, что пользователь может забыть нажать на кнопку закрыть .
        if self.COUNT_OF_PROGRAMM == 1:
            self.n1.close()
            self.n_1.close()
            self.pushButton_5.hide()
        elif self.COUNT_OF_PROGRAMM == 2:
            self.n2.close()
            self.n_2.close()
            self.pushButton_5.hide()
        elif self.COUNT_OF_PROGRAMM == 3:
            self.n3.close()
            self.n_3.close()
            self.pushButton_5.hide()


#  После этого идёт повторяющийся код для программ тренировок
class Programm_N1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('lost_ex.ui', self)  # Загружаем дизайн
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MuscleIT')
        self.setGeometry(649, 375, 420, 650)
        self.how_much = 0

        con = sqlite3.connect('Data.db')
        count = -1

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        weight = cur.execute("""SELECT weight FROM Data 
                                            """).fetchall()

        # Вывод результатов на экран
        for elem in weight:
            count += 1

        con.close()
        #  Чтобы подрегулировать программу под каждого
        if int(weight[count][0]) > 70:
            self.how_much = 1
        elif int(weight[count][0]) < 48:
            self.how_much = -1
        # Текст...
        self.plainTextEdit.insertPlainText('Вот какие упражнения надо делать,чтобы похудеть(всего есть 3 тренировки'
                                           ' в неделю и вы можете сами решить в какой день что делать):')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText('(1)Первая тренировка:')
        self.plainTextEdit.insertPlainText('\n')

        con = sqlite3.connect('Exersises.db')

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        result = cur.execute("""SELECT name FROM Exersises""").fetchall()

        con.close()
        # Ещё текст...
        self.plainTextEdit.insertPlainText(f'                              1){result[3][0]}'
                                           f' (Выполнять {2 + self.how_much} раза)')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              2){result[6][0]} '
                                           f'(Выполнять {2 + self.how_much} раза)')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              3){result[0][0]} '
                                           f'(Выполнять {2 + self.how_much} раза)')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              4){result[4][0]} '
                                           f'(Выполнять {1 + self.how_much} раза)')

        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')

        self.plainTextEdit.insertPlainText('(2)Вторая тренировка:')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              1){result[0][0]} '
                                           f'(Выполнять {2 + self.how_much} раза)')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              2){result[1][0]} '
                                           f'(Выполнять {1 + self.how_much} раза)')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              3){result[9][0]} '
                                           f'(Выполнять {1 + self.how_much} раза)')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              4){result[5][0]} '
                                           f'(Выполнять {2 + self.how_much} раза)')
        # Ещё текст...
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')

        self.plainTextEdit.insertPlainText('(3)Третья тренировка:')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              1){result[5][0]} '
                                           f'(Выполнять {1 + self.how_much} раза)')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              2){result[6][0]} '
                                           f'(Выполнять {3 + self.how_much} раза)')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              3){result[2][0]} '
                                           f'(Выполнять {1 + self.how_much} раза)')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              4){result[3][0]} '
                                           f'(Выполнять {3 + self.how_much} раза)')


class Programm_N2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('hold_ex.ui', self)  # Загружаем дизайн
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MuscleIT')
        self.setGeometry(647, 375, 420, 650)
        self.how_much = 0

        con = sqlite3.connect('Data.db')
        count = -1

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        weight = cur.execute("""SELECT weight FROM Data 
                                                    """).fetchall()

        # Вывод результатов на экран
        for elem in weight:
            count += 1

        con.close()
        #  Чтобы подрегулировать программу под каждого
        if int(weight[count][0]) > 70:
            self.how_much = 1
        elif int(weight[count][0]) < 48:
            self.how_much = -1

        self.plainTextEdit.insertPlainText('Вот какие упражнения надо делать,чтобы похудеть(всего есть 3 тренировки'
                                           ' в неделю и вы можете сами решить в какой день что делать):')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText('(1)Первая тренировка:')
        self.plainTextEdit.insertPlainText('\n')

        con = sqlite3.connect('Exersises.db')

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        result = cur.execute("""SELECT name FROM Exersises""").fetchall()

        con.close()

        self.plainTextEdit.insertPlainText(f'                              1){result[3][0]} '
                                           f'(Выполнять {3 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              2){result[6][0]} '
                                           f'(Выполнять {2 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              3){result[0][0]} '
                                           f'(Выполнять {3 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              4){result[4][0]} '
                                           f'(Выполнять {2 + self.how_much} раз(а))')

        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')

        self.plainTextEdit.insertPlainText('(2)Вторая тренировка:')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              1){result[0][0]} '
                                           f'(Выполнять {3 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              2){result[1][0]} '
                                           f'(Выполнять {2 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              3){result[9][0]} '
                                           f'(Выполнять {2 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              4){result[5][0]} '
                                           f'(Выполнять {3 + self.how_much} раз(а))')

        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')

        self.plainTextEdit.insertPlainText('(3)Третья тренировка:')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              1){result[5][0]} '
                                           f'(Выполнять {2 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              2){result[6][0]} '
                                           f'(Выполнять {4 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              3){result[2][0]} '
                                           f'(Выполнять {2 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              4){result[3][0]} '
                                           f'(Выполнять {4 + self.how_much} раз(а))')


class Programm_N3(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gain_ex.ui', self)  # Загружаем дизайн
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MuscleIT')
        self.setGeometry(647, 375, 420, 650)
        self.how_much = 0

        con = sqlite3.connect('Data.db')
        count = -1

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        weight = cur.execute("""SELECT weight FROM Data 
                                                    """).fetchall()

        # Вывод результатов на экран
        for elem in weight:
            count += 1

        con.close()
        #  Чтобы подрегулировать программу под каждого
        if int(weight[count][0]) > 70:
            self.how_much = 1
        elif int(weight[count][0]) < 48:
            self.how_much = -1

        self.plainTextEdit.insertPlainText('Вот какие упражнения надо делать,чтобы похудеть(всего есть 3 тренировки'
                                           ' в неделю и вы можете сами решить в какой день что делать):')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText('(1)Первая тренировка:')
        self.plainTextEdit.insertPlainText('\n')

        con = sqlite3.connect('Exersises.db')

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        result = cur.execute("""SELECT name FROM Exersises""").fetchall()

        con.close()

        self.plainTextEdit.insertPlainText(f'                              1){result[3][0]} '
                                           f'(Выполнять {4 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              2){result[6][0]} '
                                           f'(Выполнять {3 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              3){result[0][0]} '
                                           f'(Выполнять {3 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              4){result[4][0]} '
                                           f'(Выполнять {4 + self.how_much} раз(а))')

        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')

        self.plainTextEdit.insertPlainText('(2)Вторая тренировка:')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              1){result[0][0]} '
                                           f'(Выполнять {3 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              2){result[1][0]} '
                                           f'(Выполнять {3 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              3){result[9][0]} '
                                           f'(Выполнять {2 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              4){result[5][0]} '
                                           f'(Выполнять {1 + self.how_much} раз(а))')

        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')

        self.plainTextEdit.insertPlainText('(3)Третья тренировка:')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              1){result[5][0]} '
                                           f'(Выполнять {1 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              2){result[6][0]} '
                                           f'(Выполнять {4 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              3){result[2][0]} '
                                           f'(Выполнять {4 + self.how_much} раз(а))')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              4){result[3][0]} '
                                           f'(Выполнять {4 + self.how_much} раз(а))')


class Programm_N_1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('lost_text.ui', self)  # Загружаем дизайн
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MuscleIT')
        self.setGeometry(1487, 375, 420, 650)
        self.how_much = 1

        con = sqlite3.connect('Data.db')
        count = -1

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        height = cur.execute("""SELECT height FROM Data 
                                                            """).fetchall()

        # Вывод результатов на экран
        for elem in height:
            count += 1

        con.close()
        #  Чтобы подрегулировать программу под каждого
        if int(height[count][0]) > 180:
            self.how_much = 1.2
        elif int(height[count][0]) < 150:
            self.how_much = 0.8

        self.plainTextEdit.insertPlainText('Вот чем нужно питаться при похудении(Повторять дан'
                                           'ный рацион каждые 3 дня):')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')

        con = sqlite3.connect('Food.db')

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        result = cur.execute("""SELECT name FROM Food
                                WHERE type=1""").fetchall()

        # Вывод результатов на экран

        result2 = cur.execute("""SELECT count FROM Food
                                WHERE type=1""").fetchall()

        con.close()

        self.plainTextEdit.insertPlainText('1)Первый день:')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[0][0]}  '
                                           f'{result2[0][0]} шт.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[1][0]}  '
                                           f'{float(result2[1][0]) * self.how_much} грамм. x3')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[2][0]}  '
                                           f'{float(result2[2][0]) * self.how_much} грамм. x2')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[3][0]}  '
                                           f'{float(result2[3][0]) * self.how_much} грамм.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[4][0]}  '
                                           f'{float(result2[4][0]) * self.how_much} л.')

        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')

        self.plainTextEdit.insertPlainText('2)Второй день:')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[0][0]}  '
                                           f'{result2[0][0]} шт. x2')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[5][0]}  '
                                           f'{float(result2[5][0]) * self.how_much} грамм. x3')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[2][0]}  '
                                           f'{float(result2[2][0]) * self.how_much} грамм. x2')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[3][0]}  '
                                           f'{float(result2[3][0]) * self.how_much} грамм.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[6][0]}  '
                                           f'{result2[6][0]} шт.')

        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')

        self.plainTextEdit.insertPlainText('3)Третий день:')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[0][0]}  '
                                           f'{result2[0][0]} шт.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[1][0]}  '
                                           f'{float(result2[1][0]) * self.how_much} грамм. x3')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[2][0]}  '
                                           f'{float(result2[2][0]) * self.how_much} грамм. x2')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[3][0]}  '
                                           f'{float(result2[3][0]) * self.how_much} грамм.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[7][0]}  '
                                           f'{float(result2[7][0]) * self.how_much} л.')


class Programm_N_2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('hold_text.ui', self)  # Загружаем дизайн
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MuscleIT')
        self.setGeometry(1487, 375, 420, 650)
        self.how_much = 1

        con = sqlite3.connect('Data.db')
        count = -1

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        height = cur.execute("""SELECT height FROM Data 
                                                                    """).fetchall()

        # Вывод результатов на экран
        for elem in height:
            count += 1

        con.close()
        #  Чтобы подрегулировать программу под каждого
        if int(height[count][0]) > 180:
            self.how_much = 1.2
        elif int(height[count][0]) < 150:
            self.how_much = 0.8

        self.plainTextEdit.insertPlainText('Вот чем нужно питаться при похудении(Повторять дан'
                                           'ный рацион каждые 3 дня):')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')

        con = sqlite3.connect('Food.db')

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        result = cur.execute("""SELECT name FROM Food
                                                WHERE type=2""").fetchall()

        # Вывод результатов на экран

        result2 = cur.execute("""SELECT count FROM Food
                                                WHERE type=2""").fetchall()

        con.close()

        self.plainTextEdit.insertPlainText('1)Первый день:')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[0][0]}  '
                                           f'{float(result2[0][0]) * self.how_much} грамм.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[1][0]}  '
                                           f'{float(result2[1][0]) * self.how_much} грамм. x2')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[2][0]}  '
                                           f'{float(result2[2][0]) * self.how_much} грамм.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[4][0]}  '
                                           f'{float(result2[4][0]) * self.how_much} грамм. x2')

        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')

        self.plainTextEdit.insertPlainText('2)Второй день:')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[0][0]}  '
                                           f'{float(result2[0][0]) * self.how_much} грамм.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[3][0]}  '
                                           f'{float(result2[3][0]) * self.how_much} грамм. x2')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[2][0]}  '
                                           f'{float(result2[2][0]) * self.how_much} грамм.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[5][0]}  '
                                           f'{float(result2[5][0]) * self.how_much} грамм. x2')

        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')

        self.plainTextEdit.insertPlainText('3)Третий день:')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[0][0]}  '
                                           f'{float(result2[0][0]) * self.how_much} грамм.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[1][0]}  '
                                           f'{float(result2[1][0]) * self.how_much} грамм. x2')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[2][0]}  '
                                           f'{float(result2[2][0]) * self.how_much} грамм.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[4][0]}  '
                                           f'{float(result2[4][0]) * self.how_much} грамм. x2')


class Programm_N_3(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gain_text.ui', self)  # Загружаем дизайн
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MuscleIT')
        self.setGeometry(1487, 375, 420, 650)
        self.how_much = 1

        con = sqlite3.connect('Data.db')
        count = -1

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        height = cur.execute("""SELECT height FROM Data 
                                                                    """).fetchall()

        # Вывод результатов на экран
        for elem in height:
            count += 1

        con.close()
        #  Чтобы подрегулировать программу под каждого
        if int(height[count][0]) > 180:
            self.how_much = 1.2
        elif int(height[count][0]) < 150:
            self.how_much = 0.8

        self.plainTextEdit.insertPlainText('Вот чем нужно питаться при похудении(Повторять дан'
                                           'ный рацион каждые 3 дня):')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')

        con = sqlite3.connect('Food.db')

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        result = cur.execute("""SELECT name FROM Food
                                                        WHERE type=3""").fetchall()

        # Вывод результатов на экран

        result2 = cur.execute("""SELECT count FROM Food
                                                        WHERE type=3""").fetchall()

        con.close()

        self.plainTextEdit.insertPlainText('1)Первый день:')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[0][0]}  '
                                           f'{float(result2[0][0]) * self.how_much} грамм.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[1][0]}  '
                                           f'{float(result2[1][0]) * self.how_much} грамм. x2')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[2][0]}  '
                                           f'{float(result2[2][0]) * self.how_much} грамм.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[4][0]}  '
                                           f'{result2[4][0]} шт ')

        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')

        self.plainTextEdit.insertPlainText('2)Второй день:')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[0][0]}  '
                                           f'{float(result2[0][0]) * self.how_much} грамм.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[3][0]}  '
                                           f'{float(result2[3][0]) * self.how_much} грамм. x2')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[2][0]}  '
                                           f'{float(result2[2][0]) * self.how_much} грамм.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[5][0]}  '
                                           f'{float(result2[5][0]) * self.how_much} грамм. x2')

        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')

        self.plainTextEdit.insertPlainText('3)Третий день:')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(' ')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[0][0]}  '
                                           f'{float(result2[0][0]) * self.how_much} грамм.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[1][0]}  '
                                           f'{float(result2[1][0]) * self.how_much} грамм. x2')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[2][0]}  '
                                           f'{float(result2[2][0]) * self.how_much} грамм.')
        self.plainTextEdit.insertPlainText('\n')
        self.plainTextEdit.insertPlainText(f'                              {result[4][0]}  '
                                           f'{result2[4][0]} шт x2')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec_())
