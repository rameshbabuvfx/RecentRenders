import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from thumbnails import *


class TableWidget(QTableWidget):
    def __init__(self):
        super(TableWidget, self).__init__()
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setStyleSheet("QTableWidget{background-color: transparent}")

    def mouseMoveEvent(self, event):
        current_value = self.currentItem()
        mime = QMimeData()
        mime.setText(current_value.text())
        drag = QDrag(self)
        drag.setMimeData(mime)
        print(current_value.text())
        drag.exec_(Qt.CopyAction)

    def dropEvent(self, event):
        event.ignore()


class DisplayRenders(QWidget):
    def __init__(self):
        super(DisplayRenders, self).__init__()
        self.resize(500, 600)


        self.animation = QPropertyAnimation(self, b'geometry')
        self.animation.setDuration(250)
        self.animation.setStartValue(QRect(700,300,600,5))
        self.animation.setEndValue(QRect(700,300,500,600))
        self.animation.setEasingCurve(QEasingCurve.OutCurve)
        self.animation.start()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.row_height = 110
        self.column_width = 110
        self.gblayout = QGridLayout()
        self.table_widget = TableWidget()
        self.gblayout.addWidget(self.table_widget)
        self.setLayout(self.gblayout)
        self.table_widget.setRowCount(10)
        self.table_widget.setColumnCount(4)
        self.table_widget.setRowHeight(1,self.row_height)
        self.table_widget.setColumnWidth(1,self.column_width)
        self.table_widget.setShowGrid(False)
        self.table_widget.horizontalHeader().hide()
        self.table_widget.verticalHeader().hide()
        self.table_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)





        item = QTableWidgetItem(r"F:\NukePython\RecentRenders\thumbnails\blackadam.jpg")
        self.table_widget.setItem(1, 1, item)
        label = QLabel()
        pixmap = QPixmap(r"F:\NukePython\RecentRenders\thumbnails\blackadam.jpg")
        label.setPixmap(pixmap.scaled(self.column_width, self.row_height, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        label.setScaledContents(True)
        label.resize(10,10)
        self.table_widget.setCellWidget(1, 1, label)


def run():
    run.obj = DisplayRenders()
    run.obj.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = DisplayRenders()
    obj.show()
    sys.exit(app.exec_())
