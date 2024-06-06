from PySide6.QtWidgets import QApplication
import sys
from main_application import mainApplication

app = QApplication(sys.argv)
window = mainApplication()

window.show()
app.exec()