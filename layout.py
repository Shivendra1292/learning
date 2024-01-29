from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
app = QApplication([])
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
app.setPalette(palette)
window = QWidget()
layout = QVBoxLayout() # prints Horizontally
# layout = QVBoxLayout() # prints Vertically
layout2 = QHBoxLayout() # prints Vertically]
layout2.addWidget(QPushButton('Top'))
layout2.addWidget(QPushButton('Bottom'),1)
layout2.addWidget(QPushButton('Top'),5)
layout2.addWidget(QPushButton('Top'),2)
window2 = QWidget()
window2.setLayout(layout2)
layout.addWidget(window2)
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'),1)
layout.addWidget(QPushButton('Top'),5)
layout.addWidget(QPushButton('Top'),2)
# layout.addWidget(QPushButton('Bottom'),3)
window.setLayout(layout)

window.show()
app.exec()