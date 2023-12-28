import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QHBoxLayout


class ProcedurePage(QWidget):
    def __init__(self):
        super(ProcedurePage, self).__init__()

        # Set up the procedure page
        self.setWindowTitle('Procedures Page')
        self.setGeometry(200, 200, 500, 300)

        # Create layout
        layout = QVBoxLayout()

        # Create procedure widgets
        self.create_procedure_widget('Procedure 1', 'Input 1:', 'input1', 'Output 1:', 'output1', layout)
        self.create_procedure_widget('Procedure 2', 'Input 2:', 'input2', 'Output 2:', 'output2', layout)
        self.create_procedure_widget('Procedure 3', 'Input 3:', 'input3', 'Output 3:', 'output3', layout)

        # Add a run button
        run_button = QPushButton('Run', self)
        run_button.clicked.connect(self.run_procedures)
        layout.addWidget(run_button)

        # Set the layout for the procedure page
        self.setLayout(layout)

    def create_procedure_widget(self, procedure_name, input_label_text, input_name, output_label_text, output_name, layout):
        procedure_layout = QHBoxLayout()

        input_label = QLabel(input_label_text)
        input_field = QLineEdit(self)

        output_label = QLabel(output_label_text)
        output_field = QTextEdit(self)
        output_field.setReadOnly(True)

        procedure_layout.addWidget(QLabel(procedure_name))
        procedure_layout.addWidget(input_label)
        procedure_layout.addWidget(input_field)
        procedure_layout.addWidget(output_label)
        procedure_layout.addWidget(output_field)

        setattr(self, input_name, input_field)
        setattr(self, output_name, output_field)

        layout.addLayout(procedure_layout)

    def run_procedures(self):
        # Get inputs and perform procedures
        input1_text = self.input1.text()
        self.output1.setText(f'Output 1: {self.procedure1(input1_text)}')

        input2_text = self.input2.text()
        self.output2.setText(f'Output 2: {self.procedure2(input2_text)}')

        input3_text = self.input3.text()
        self.output3.setText(f'Output 3: {self.procedure3(input3_text)}')
    def set_cursor(self,cursor):
        self.cursor = cursor

    def procedure1(self, input_text):
        # Replace this with your actual procedure logic
        return f'Procedure 1 result for {input_text}'

    def procedure2(self, input_text):
        # Replace this with your actual procedure logic
        return f'Procedure 2 result for {input_text}'

    def procedure3(self, input_text):
        # Replace this with your actual procedure logic
        return f'Procedure 3 result for {input_text}'
