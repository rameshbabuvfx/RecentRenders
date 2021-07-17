import sys
import json
import subprocess

try:
    import nuke
except:
    pass

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import config


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

    def modify_ui(self):
        """
        Modifies UI widgets.

        :return:
        """
        self.setWindowTitle("Recent Renders")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.resize(700, 600)
        self.list_widget_render.setIconSize(QSize(200, 200))

    def add_renders_list(self):
        """
        Displays renders list in list widget.

        :return: None
        """
        for render_path in self.recent_renders_list():
            item = QListWidgetItem(render_path)
            icon = QIcon(r"D:\PythonProjects\NukePython\RecentRenders\renders\tmp_icon.png")
            item.setIcon(icon)
            self.list_widget_render.addItem(item)


def create_thumbnail():
    """
    Runs thumbnailCreator in subprocess.

    :return: None
    """
    subprocess.call("{} -t {}".format(sys.executable, config.THUMBNAIL_FILE_PATH))


def run():
    """
    Runs Application.

    :return:
    """
    create_thumbnail()
    run.obj = DisplayRenders()
    run.obj.show()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     obj = DisplayRenders()
#     obj.show()
#     sys.exit(app.exec_())
