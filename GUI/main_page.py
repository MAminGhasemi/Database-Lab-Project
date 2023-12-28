import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from functions import FunctionPage
from views import ViewsPage
from stored_procedures import ProcedurePage

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the main window
        self.setWindowTitle('Database Operations')
        self.setGeometry(100, 100, 400, 200)

        # Create layout
        layout = QVBoxLayout()

        # Create buttons with icons
        functions_button = self.create_button('Functions', 'icons/functions.png', self.show_functions)
        views_button = self.create_button('Views', 'icons/views.png', self.show_views)
        procedures_button = self.create_button('Procedures', 'icons/procedures.png', self.show_procedures)

        # Add buttons to layout
        layout.addWidget(functions_button)
        layout.addWidget(views_button)
        layout.addWidget(procedures_button)

        # Set the layout for the main window
        self.setLayout(layout)

    def create_button(self, text, icon_path, on_click):
        button = QPushButton(text, self)
        button.setIcon(QIcon(icon_path))
        button.clicked.connect(on_click)
        button.setStyleSheet(
            """
            QPushButton {
                font-size: 14px;
                padding: 8px;
                margin: 5px;
                border: 2px solid #4CAF50;
                border-radius: 8px;
                color: white;
                background-color: #4CAF50;
            }
            
            QPushButton:hover {
                background-color: #45a049;
            }
            """
        )
        return button

    def show_functions(self):
        print("Functions button clicked")
        self.function_page = FunctionPage()
        self.function_page.show()

    def show_views(self):
        print("Views button clicked")
        self.function_page = ViewsPage()
        self.function_page.show()

    def show_procedures(self):
        print("Procedures button clicked")
        self.procedure_page = ProcedurePage()
        self.procedure_page.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())