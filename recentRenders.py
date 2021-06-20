import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from thumbnails import *


class ListWidget(QListWidget):
    def __init__(self):
        super(ListWidget, self).__init__()
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
        self.resize(500, 600)
        self.gblayout = QGridLayout()
        self.list_widget = ListWidget()
        self.gblayout.addWidget(self.list_widget)
        self.setLayout(self.gblayout)
        self.list_widget.setViewMode(QListWidget.IconMode)

        for i in range(10):
            item = QListWidgetItem("D:\personal\RedChillies Docs\RameshBabu-Photo.jpg")
            # item.setIcon(QIcon(r"F:\NukePython\RecentRenders\thumbnails\blackadam.jpg"))
            self.list_widget.addItem(item)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = DisplayRenders()
    obj.show()
    sys.exit(app.exec_())
