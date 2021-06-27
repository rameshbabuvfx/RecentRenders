import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class ListWidget(QListWidget):
    def __init__(self):
        super(ListWidget, self).__init__()
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
        self.layout = QGridLayout()
        self.list_widget_render = ListWidget()
        self.layout.addWidget(self.list_widget_render)
        self.setLayout(self.layout)
        self.modify_ui()
        self.add_renders_list()

    def modify_ui(self):
        self.setWindowTitle("Recent Renders")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.resize(700,600)
        self.list_widget_render.setIconSize(QSize(200,200))

    def add_renders_list(self):
        for i in range(10):
            item = QListWidgetItem(r"F:\NukePython\RecentRenders\renders\TLO_206_021_650_ftg-001_v001")
            icon = QIcon(r"F:\NukePython\RecentRenders\renders\TLO_206_021_650_ftg-001_v001\TLO_206_021_650_ftg-001_v001.0001.jpg")
            item.setIcon(icon)

            self.list_widget_render.addItem(item)



def run():
    run.obj = DisplayRenders()
    run.obj.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = DisplayRenders()
    obj.show()
    sys.exit(app.exec_())
