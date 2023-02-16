import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
import pyqtgraph as pg
import math 
sin = math.sin
cos = math.cos
tan = math.tan
def ln(x):
    return np.log(np.abs(x))
def log(x, y):
    return np.log(np.abs(y)) / np.log(np.abs(x))
class GraphOn(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon('GraphOn.png'))
    def initUI(self):
        self.equation_input = QLineEdit(self)
        self.equation_input.move(20, 20)
        self.equation_input.resize(280, 30)
        self.plot_widget = pg.PlotWidget(self)
        self.plot_widget.move(20, 60)
        self.plot_widget.resize(560, 400)
        self.plot_button = QPushButton('Plot', self)
        self.plot_button.move(320, 20)
        self.plot_button.clicked.connect(self.plot_graph)

        
        central_widget = QWidget()
        central_widget.setLayout(QVBoxLayout())
        central_widget.layout().addWidget(self.equation_input)
        central_widget.layout().addWidget(self.plot_widget)
        central_widget.layout().addWidget(self.plot_button)
        self.setCentralWidget(central_widget)

        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('GraphOn')
        self.show()

    def plot_graph(self):
        equation_str = self.equation_input.text()

        x_vals = np.linspace(-100, 100, 1000)
        y_vals = [eval(equation_str.replace('^', '**').replace('x', str(x))) for x in x_vals]
        
        self.plot_widget.clear()
        self.plot_widget.plot(x_vals, y_vals, pen='r')
        self.plot_widget.setRange(xRange=[-100, 100], yRange=[-100, 100])

        self.plot_widget.plot([-100, 100], [0, 0], pen='w')
        self.plot_widget.plot([0, 0], [-100, 100], pen='w')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GraphOn()
    sys.exit(app.exec_())
