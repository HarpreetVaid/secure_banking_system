import PySide6
from PySide6.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication([])

button = QPushButton("Click me!")
button.setCheckable(True)

def on_button_clicked():
    if button.isChecked():
        button.setChecked(False)
    else:
        button.setChecked(True)

button.clicked.connect(on_button_clicked)

button.show()

app.exec()