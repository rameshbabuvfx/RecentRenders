import json
import os.path

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

    render_json["recent_renders"].append(render_path)

    with open(config.RENDER_DATA_JSON, "w") as file:
        json.dump(render_json, file, indent=4)
