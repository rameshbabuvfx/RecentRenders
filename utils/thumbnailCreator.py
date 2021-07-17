import json
import os

import nuke

import config


def create_thumbnails():
    """
    Generates thumbnails for main listwidget.
    This module runs in subprocess.

    :return: None
    """
    with open(config.RENDER_DATA_JSON, "r") as file:
        render_json = json.load(file)
    render_paths = render_json['recent_renders']

    for path in render_paths:
        read_node = nuke.nodes.Read(file=path)
        thumbnail_name = "{}.{}".format(os.path.basename(path).split(".")[0], "jpg")
        write_path = os.path.join(config.THUMBNAILS, thumbnail_name)
        write_node = nuke.nodes.Write(file=write_path.replace("\\", "/"))
        write_node.setInput(0, read_node)
        if not os.path.exists(write_path):
            nuke.execute(write_node, 1, 1)


if __name__ == '__main__':
    create_thumbnails()

