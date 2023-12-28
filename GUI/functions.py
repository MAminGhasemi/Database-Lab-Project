from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QHBoxLayout
import pyodbc

class FunctionPage(QWidget):
    def __init__(self, cursor):
        super(FunctionPage, self).__init__()

        # Set up the function page
        self.setWindowTitle('Functions Page')
        self.setGeometry(200, 200, 500, 300)

        # Store the database cursor
        self.cursor = cursor

        # Create layout
        layout = QVBoxLayout()

        # Create function widgets
        self.create_function_widget('CheckNationalCode', 'National Code:', 'national_code_input', 'Result:', 'national_code_output', layout)
        self.create_function_widget('Function 2', 'Input 2:', 'input2', 'Output 2:', 'output2', layout)
        self.create_function_widget('Function 3', 'Input 3:', 'input3', 'Output 3:', 'output3', layout)

        # Add individual run buttons for each function
        run_button_1 = QPushButton('Run CheckNationalCode', self)
        run_button_1.clicked.connect(self.run_check_national_code)
        layout.addWidget(run_button_1)

        run_button_2 = QPushButton('Run Function 2', self)
        run_button_2.clicked.connect(self.run_function2)
        layout.addWidget(run_button_2)

        run_button_3 = QPushButton('Run Function 3', self)
        run_button_3.clicked.connect(self.run_function3)
        layout.addWidget(run_button_3)

        # Set the layout for the function page
        self.setLayout(layout)

    def create_function_widget(self, function_name, input_label_text, input_name, output_label_text, output_name, layout):
        function_layout = QHBoxLayout()

        input_label = QLabel(input_label_text)
        input_field = QLineEdit(self)

        output_label = QLabel(output_label_text)
        output_field = QTextEdit(self)
        output_field.setReadOnly(True)

        function_layout.addWidget(QLabel(function_name))
        function_layout.addWidget(input_label)
        function_layout.addWidget(input_field)
        function_layout.addWidget(output_label)
        function_layout.addWidget(output_field)

        setattr(self, input_name, input_field)
        setattr(self, output_name, output_field)

        layout.addLayout(function_layout)

    def run_check_national_code(self):
        # Get input and perform CheckNationalCode function
        national_code_text = self.national_code_input.text()
        result = self.check_national_code(national_code_text)
        self.national_code_output.setText(f'Result: {"Valid" if result else "Invalid"}')

    def run_function2(self):
        # Get input and perform Function 2
        input2_text = self.input2.text()
        self.output2.setText(f'Output 2: {self.function2(input2_text)}')

    def run_function3(self):
        # Get input and perform Function 3
        input3_text = self.input3.text()
        self.output3.setText(f'Output 3: {self.function3(input3_text)}')

    def check_national_code(self, national_code):
        # Execute the CheckNationalCode function using the stored cursor
        try:
            self.cursor.execute("SELECT dbo.CheckNationalCode(?) AS Result", national_code)
            result = self.cursor.fetchone().Result
            return result
        except pyodbc.Error as ex:
            print(f"Error: {ex}")
            return False

    def function2(self, input_text):
        # Replace this with your actual function logic for Function 2
        return f'Function 2 result for {input_text}'

    def function3(self, input_text):
        # Replace this with your actual function logic for Function 3
        return f'Function 3 result for {input_text}'