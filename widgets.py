from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Click Me")

        wid = QWidget(self)
        self.setCentralWidget(wid)
        layout = QVBoxLayout()
        wid.setLayout(layout)
        btn = QPushButton("1")
        btn.pressed.connect(self.on_click)
        layout.addWidget(btn)

        btn = QPushButton("2")
        btn.pressed.connect(self.on_click)
        layout.addWidget(btn)

        btn = QPushButton("3")
        btn.pressed.connect(self.on_click)
        layout.addWidget(btn)
    
    def on_click(self, e):
        alert = QMessageBox()
        alert.setText(f"You have cliked x")
        alert.exec_()

    def on_click_1(self):
        alert = QMessageBox()
        alert.setText(f"You have cliked 1")
        alert.exec_()

    def on_click_2(self):
        alert = QMessageBox()
        alert.setText(f"You have cliked 2")
        alert.exec_()

    def on_click_3(self):
        alert = QMessageBox()
        alert.setText(f"You have cliked 3")
        alert.exec_()

if __name__=="__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())

