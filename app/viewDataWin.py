from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QMessageBox, QHBoxLayout
from PyQt6.QtGui import QIcon


class ViewDataWin(QWidget):
    def __init__(self):
        super().__init__()

        self.data = [
            {'id': 1, 'name': 'Фигурка Iron Man', 'status': 'В наличии'},
            {'id': 2, 'name': 'Шампунь "Жумайсынба"', 'status': 'Отсутствует'},
            {'id': 3, 'name': 'Шильдик на машину "Honda"', 'status': 'В наличии'}
        ]
        self.initUI()
        self.load_data()

    def initUI(self):
        self.setWindowTitle("База Данных")
        self.setWindowIcon(QIcon('resources/zov.ico'))
        self.setGeometry(100, 100, 1000, 500)
        self.table = QTableWidget()
        self.add = QPushButton("Добавить")
        self.del_entry = QPushButton("Удалить")
        self.edit_entry = QPushButton("Изменить")
        self.back_button = QPushButton("Выйти")
        main_l = QVBoxLayout()
        h_l1 = QHBoxLayout()
        main_l.addWidget(self.table)
        h_l1.addWidget(self.add)
        h_l1.addWidget(self.edit_entry)
        h_l1.addWidget(self.del_entry)
        h_l1.addWidget(self.back_button)
        main_l.addLayout(h_l1)
        self.setLayout(main_l)

        self.add.clicked.connect(self.add_entry)
        self.back_button.clicked.connect(self.back)
        self.edit_entry.clicked.connect(self.edit_order)
        self.del_entry.clicked.connect(self.delete_order)

    def add_entry(self):
        pass

    def load_data(self):
        users = self.data
        self.table.setColumnCount(3)  # Исправлено количество колонок
        self.table.setHorizontalHeaderLabels(['ID Товара', 'Название товара', 'Статус товара'])
        self.table.setRowCount(len(users))
        for row_idx, user in enumerate(users):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(user['id'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(str(user['name'])))
            self.table.setItem(row_idx, 2, QTableWidgetItem(str(user['status'])))

    def delete_order(self):
        pass

    def back(self):
        self.close()

    def edit_order(self):
        pass