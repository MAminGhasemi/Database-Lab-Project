import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QHBoxLayout


class FunctionPage(QWidget):
    def __init__(self):
        super(FunctionPage, self).__init__()

        # Set up the function page
        self.setWindowTitle('Functions Page')
        self.setGeometry(200, 200, 500, 300)

        # Create layout
        layout = QVBoxLayout()

        # Create function widgets
        self.create_function_widget('Function 1', 'Input 1:', 'input1', 'Output 1:', 'output1', layout)
        self.create_function_widget('Function 2', 'Input 2:', 'input2', 'Output 2:', 'output2', layout)
        self.create_function_widget('Function 3', 'Input 3:', 'input3', 'Output 3:', 'output3', layout)

        # Add a run button
        run_button = QPushButton('Run', self)
        run_button.clicked.connect(self.run_functions)
        layout.addWidget(run_button)

        # Set the layout for the function page
        self.setLayout(layout)

    def set_cursor(self,cursor):
        self.cursor = cursor

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

    def run_functions(self):
        # Get inputs and perform functions
        input1_text = self.input1.text()
        self.output1.setText(f'Output 1: {self.function1(input1_text)}')

        input2_text = self.input2.text()
        self.output2.setText(f'Output 2: {self.function2(input2_text)}')

        input3_text = self.input3.text()
        self.output3.setText(f'Output 3: {self.function3(input3_text)}')

    def function1(self, input_text):
        # Replace this with your actual function logic
        return f'Function 1 result for {input_text}'

    def function2(self, input_text):
        # Replace this with your actual function logic
        return f'Function 2 result for {input_text}'

    def function3(self, input_text):
        # Replace this with your actual function logic
        return f'Function 3 result for {input_text}'
