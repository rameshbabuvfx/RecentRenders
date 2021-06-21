import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from thumbnails import *


class TableWidget(QTableWidget):
    def __init__(self):
        super(TableWidget, self).__init__()
        self.resize(500, 600)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)

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
        self.resize(800, 600)
        self.gblayout = QGridLayout()
        self.table_widget = TableWidget()
        self.gblayout.addWidget(self.table_widget)
        self.setLayout(self.gblayout)

        self.table_widget.setRowCount(10)
        self.table_widget.setColumnCount(4)
        self.table_widget.setRowHeight(1,160)
        self.table_widget.setColumnWidth(1,205)
        self.table_widget.setIconSize(QSize(100,100))
        self.table_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        item = QTableWidgetItem(r"F:\NukePython\RecentRenders\thumbnails\blackadam.jpg")
        self.table_widget.setItem(1, 1, item)
        label = QLabel()
        pixmap = QPixmap(r"F:\NukePython\RecentRenders\thumbnails\blackadam.jpg")
        label.setPixmap(pixmap.scaled(205,160, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        label.setScaledContents(True)
        label.resize(10,10)
        self.table_widget.setCellWidget(1, 1, label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = DisplayRenders()
    obj.show()
    sys.exit(app.exec_())
