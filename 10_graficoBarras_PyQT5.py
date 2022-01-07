
#CRIA UMA JANELA COM PYQT5 E INSERE UM GRÁFICO CRIADO COM MATPLOTLIB

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg\
    as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget

#CRIA A CLASSE QUE USARÁ OS CÓDIGOS DO MATPLOTLIB
class Canvas(FigureCanvas):
    def __init__(self, parent):

        #CRIA A FIGURA OU ÁREA DO GRÁFICO
        fig, self.ax = plt.subplots(figsize=(3, 2), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

        #CÓDIGO PARA A CRIAÇÃO DO GRÁFICO
        x=[1,2,3,4,5,6,7,8,9]
        y=[5,4,3,1,7,6,9,8,2]
        plt.bar(x, y, label = 'Dados')
        plt.title("Gráfico com PyQT5")
        plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
        plt.yticks([0,1,2,3,4,5,6,7,8,9,10])
        plt.legend()

# CRIA A CLASSE DA JANELA COM AS DEFINIÇÕES ESCOLHIDAS
class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        chart = Canvas(self)

#FUNÇÃO QUE CHAMA A JANELA CRIADA
app = QApplication(sys.argv)

#REFERENCIA A CLASSE QUE CRIA A JANELA
demo = AppDemo()

#MOSTRA A JANELA CRIADA
demo.show()

#MANTÉM A JANELA ATIVA ATÉ O FECHAMENTO MANUAL
sys.exit(app.exec_())



