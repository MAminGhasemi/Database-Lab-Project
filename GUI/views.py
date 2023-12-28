import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout, QLabel


class ViewsPage(QWidget):
    def __init__(self):
        super(ViewsPage, self).__init__()

        # Set up the views page
        self.setWindowTitle('Views Page')
        self.setGeometry(200, 200, 600, 400)

        # Create layout
        self.layout = QVBoxLayout()

        # Create view tables
        self.create_view_table('View 1', [['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3']])
        self.create_view_table('View 2', [['X1', 'Y1', 'Z1'], ['X2', 'Y2', 'Z2'], ['X3', 'Y3', 'Z3']])
        self.create_view_table('View 3', [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])

        # Set the layout for the views page
        self.setLayout(self.layout)

    def set_cursor(self,cursor):
        self.cursor = cursor

    def create_view_table(self, view_name, data):
        view_layout = QHBoxLayout()
        table = QTableWidget(self)
        table.setRowCount(len(data))
        table.setColumnCount(len(data[0]))

        for i, row in enumerate(data):
            for j, item in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(item)))

        table.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])

        view_layout.addWidget(table)
        view_layout.addWidget(QLabel(view_name))

        self.layout.addLayout(view_layout)