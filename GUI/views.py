import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout, QLabel
import pyodbc

class ViewPage(QWidget):
    def __init__(self, cursor):
        super(ViewPage, self).__init__()

        # Set up the views page
        self.setWindowTitle('Views Page')
        self.setGeometry(200, 200, 600, 400)

        # Store the database cursor
        self.cursor = cursor

        # Create layout
        self.layout = QVBoxLayout()

        # Create view tables
        self.create_view_table('User_Profile_View', self.execute_view('User_Profile_View'))
        self.create_view_table('Product_Details_View', self.execute_view('Product_Details_View'))
        self.create_view_table('User_Message_History_View', self.execute_view('User_Message_History_View'))

        # Set the layout for the views page
        self.setLayout(self.layout)

    def create_view_table(self, view_name, data):
        view_layout = QHBoxLayout()
        table = QTableWidget(self)
        table.setRowCount(len(data))
        table.setColumnCount(len(data[0]))

        for i, row in enumerate(data):
            for j, item in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(item)))

        table.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])  # Adjust column labels as needed

        view_layout.addWidget(table)
        view_layout.addWidget(QLabel(view_name))

        self.layout.addLayout(view_layout)

    def execute_view(self, view_name):
        try:
            self.cursor.execute(f"SELECT * FROM {view_name}")
            result = self.cursor.fetchall()
            return result
        except pyodbc.Error as ex:
            print(f"Error: {ex}")
            return []

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ViewPage()  # Provide the cursor when you instantiate ViewPage
    window.show()
    sys.exit(app.exec_())
