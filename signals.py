
from PyQt5.QtWidgets import *

app = QApplication([])
btn = QPushButton("Click Me")

def on_click():
    alert = QMessageBox()
    alert.setText("You have clicked me")
    alert.exec()

btn.clicked.connect(on_click)
btn.resize(100,100)
btn.show()
app.exec()
