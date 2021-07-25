import os
import json
import datetime

import nuke

import config

import recentRenderUpdate

def create_thumbnails():
    """
    Generates thumbnails for main listwidget.
    This module runs in subprocess.

    :return: None
    """
    render_json = recentRenderUpdate.read_json_data()
    render_paths = render_json['recent_renders']

    for path in render_paths:
        read_node = nuke.nodes.Read(file=path)
        reformat_node = nuke.nodes.Reformat(format="PC_Video", black_outside=True)

        reformat_node.setInput(0, read_node)
        time_now = datetime.datetime.now().strftime("%H_%M_%S")
        thumbnail_name = "{}_{}.{}".format(os.path.basename(path).split(".")[0], "jpg")
        write_path = os.path.join(config.THUMBNAILS, thumbnail_name)
        write_node = nuke.nodes.Write(file=write_path.replace("\\", "/"))
        write_node.setInput(0, reformat_node)
        if not os.path.exists(write_path):
            nuke.execute(write_node, 1, 1)


if __name__ == '__main__':
    create_thumbnails()

