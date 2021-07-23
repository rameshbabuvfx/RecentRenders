import json
import os

import nuke

import config


def update_renders_data():
    """
    Update write node render path in renders json file.

    :return: None
    """
    write_node = nuke.thisNode()

    render_path = write_node['file'].value()

    with open(config.RENDER_DATA_JSON, "r") as file:
        render_json = json.load(file)

    render_json["recent_renders"].insert(0, render_path)

    with open(config.RENDER_DATA_JSON, "w") as file:
        json.dump(render_json, file, indent=4)


def remove_older_renders(render_limit=1):

    with open(config.RENDER_DATA_JSON, "r") as file:
        render_json = json.load(file)

    updated_render_list = []
    for count, render_path in enumerate(render_json["recent_renders"]):
        if count <= render_limit:
            updated_render_list.append(render_path)
        else:
            thumbnail_name = "{}.{}".format(os.path.basename(render_path).split(".")[0], "jpg")
            os.remove(os.path.join(config.THUMBNAILS, thumbnail_name))

    render_json["recent_renders"] = updated_render_list
    with open(config.RENDER_DATA_JSON, "w") as file:
        json.dump(render_json, file, indent=4)
