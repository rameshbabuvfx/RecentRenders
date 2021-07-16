import os
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
        thumbnail_file = "{}/thumbnailCreator.py".format(os.path.dirname(__file__))
        print(thumbnail_file)
        subprocess.call("{} -t {}".format(sys.executable, thumbnail_file))

    def modify_ui(self):
        self.setWindowTitle("Recent Renders")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.resize(700, 600)
        self.list_widget_render.setIconSize(QSize(200, 200))

    def add_renders_list(self):
        for render_path in self.recent_renders_list():
            item = QListWidgetItem(render_path)
            icon = QIcon(r"D:\PythonProjects\NukePython\RecentRenders\renders\tmp_icon.png")
            item.setIcon(icon)
            self.list_widget_render.addItem(item)

    def update_renders_data(self):
        renders_list = [
            r"D:\PythonProjects\NukePython\RecentRenders\renders\TLO_206_021_650_ftg-001_v001",
            r"D:\PythonProjects\NukePython\RecentRenders\renders\TLO_206_021_670_ftg-001_v001",
            r"D:\PythonProjects\NukePython\RecentRenders\renders\A445C007_151223_R5B7",
            r"D:\PythonProjects\NukePython\RecentRenders\renders\Shot_132_A619C026_160817_R5B7_v005",
            r"D:\PythonProjects\NukePython\RecentRenders\renders\TLO_206_021_800_ftg-002_v001",
            r"D:\PythonProjects\NukePython\RecentRenders\renders\SHOT_76_Additional_v001",
                        ]
        data = {"recent_renders": renders_list}
        print(data)

        with open("./render_data/renders.json", "r") as file:
            json_file = json.load(file)
            print(json_file)

        with open("./render_data/renders.json", "w") as file:
            json.dump(data, file, indent=4)

def run():
    run.obj = DisplayRenders()
    run.obj.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = DisplayRenders()
    obj.show()
    sys.exit(app.exec_())

