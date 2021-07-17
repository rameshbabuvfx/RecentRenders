import json
import os

import nuke

import config


def create_thumbnails():
    """
    Generates thumbnails for mail listwidget.
    This file runs in subprocess.

    :return: None
    """
    with open(config.RENDER_DATA_JSON, "r") as file:
        render_json = json.load(file)
    render_paths = render_json['recent_renders']
    for path in render_paths:
        read_node = nuke.nodes.Read(file=path)
        write_path = os.path.join(config.THUMBNAILS, os.path.basename(path)).replace("\\", "/")
        write_node = nuke.nodes.Write(file="D:/PythonProjects/NukePython/RecentRenders/thumbnails/test.jpg")
        write_node.setInput(0, read_node)
        nuke.execute(write_node, 1, 1)


if __name__ == '__main__':
    create_thumbnails()

