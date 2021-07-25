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

import config
from utils import recentRenderUpdate


class ListWidget(QListWidget):
    def __init__(self):
        super(ListWidget, self).__init__()
        self.setDragEnabled(True)
        self.setAcceptDrops(True)

    def mouseMoveEvent(self, event):
        current_value = self.currentItem()
        mime = QMimeData()
        render_path = current_value.text()
        if not render_path.endswith(("mov", "mp4")):
            render_path = os.path.dirname(render_path)
        mime.setText(render_path)
        drag = QDrag(self)
        drag.setMimeData(mime)
        print(render_path)
        drag.exec_(Qt.CopyAction)

    def dropEvent(self, event):
        event.ignore()


class DisplayRenders(QWidget):
    def __init__(self):
        super(DisplayRenders, self).__init__()
        self.vlayout = QVBoxLayout()
        self.glayout = QGridLayout()
        self.hlayout = QHBoxLayout()
        self.list_widget_render = ListWidget()
        self.renders_limit_spinbox = QSpinBox()
        self.renders_limit_button = QPushButton("Set Renders Limit")
        self.glayout.addWidget(self.list_widget_render)
        self.hlayout.addWidget(self.renders_limit_spinbox)
        self.hlayout.addWidget(self.renders_limit_button)
        self.hlayout.addStretch()
        self.vlayout.addLayout(self.glayout)
        self.vlayout.addLayout(self.hlayout)
        self.setLayout(self.vlayout)
        self.modify_ui()
        self.connect_ui()
        self.add_renders_list()

    def modify_ui(self):
        """
        Modifies UI widgets.

        :return:
        """
        self.setWindowTitle("Recent Renders")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.resize(700, 600)
        self.list_widget_render.setIconSize(QSize(200, 200))
        self.renders_limit_spinbox.setMaximumWidth(50)
        self.renders_limit_button.setMaximumWidth(150)
        render_json = recentRenderUpdate.read_json_data()
        self.renders_limit_spinbox.setValue((render_json["renders_limit"]) + 1)

    def connect_ui(self):
        """
        Connects ui with custom functions.

        :return:
        """
        self.renders_limit_button.clicked.connect(self.set_render_limit)

    def set_render_limit(self):
        """
        Sets renders limit in json database.

        :return:
        """
        render_json = recentRenderUpdate.read_json_data()

        render_json["renders_limit"] = int(self.renders_limit_spinbox.text())-1

        recentRenderUpdate.write_json_data(render_json)

    def add_renders_list(self):
        """
        Displays renders list in list widget.

        :return: None
        """
        with open(config.RENDER_DATA_JSON, "r") as file:
            render_json = json.load(file)
        render_paths = render_json['recent_renders']

        for path in render_paths:
            item = QListWidgetItem(path)
            thumbnail_name = "{}.{}".format(os.path.basename(path).split(".")[0], "jpg")
            icon = QIcon(os.path.join(config.THUMBNAILS, thumbnail_name))
            item.setIcon(icon)
            self.list_widget_render.addItem(item)


class LoadingLabel(QWidget):
    def __init__(self):
        super(LoadingLabel, self).__init__()
        self.resize(500, 50)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.layout = QGridLayout()
        self.label = QLabel()
        self.label.setText("Loading...")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


def create_thumbnail():
    """
    Runs thumbnailCreator in subprocess.

    :return: None
    """
    subprocess.call("{} -t {}".format(sys.executable, config.THUMBNAIL_FILE_PATH))


def run():
    """
    Runs Application.

    :return: None
    """
    recentRenderUpdate.remove_older_renders()
    create_thumbnail()
    run.display = DisplayRenders()
    run.display.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = DisplayRenders()
    obj.show()
    sys.exit(app.exec_())
