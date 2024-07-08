from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader







app = QApplication([])

loader= QUiLoader()

window =loader.load("calculator.ui")

window.show()
app.exec()


