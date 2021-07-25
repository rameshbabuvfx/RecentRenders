import os
import json

try:
    import nuke
except:
    pass

import config


def read_json_data():
    """
    Reads renders data from json database.

    :return dict: renders data.
    """
    with open(config.RENDER_DATA_JSON, "r") as file:
        render_json = json.load(file)
    return render_json


def write_json_data(write_json):
    """
    Writes renders data to json databse.

    :param write_json:
    :return:
    """
    with open(config.RENDER_DATA_JSON, "w") as file:
        json.dump(write_json, file, indent=4)


def update_renders_data():
    """
    Update write node render path in renders json file.

    :return: None
    """
    write_node = nuke.thisNode()
    render_path = write_node['file'].value()
    render_json = read_json_data()
    render_json["recent_renders"].insert(0, render_path)
    write_json_data(render_json)


def remove_older_renders():
    """
    Removes older renders thumbnails and json data depends on renders limit.

    :return: None.
    """
    render_json = read_json_data()

    updated_render_list = []
    for count, render_path in enumerate(render_json["recent_renders"]):
        if count <= render_json["renders_limit"]:
            updated_render_list.append(render_path)
        else:
            thumbnail_name = "{}.{}".format(os.path.basename(render_path).split(".")[0], "jpg")
            os.remove(os.path.join(config.THUMBNAILS, thumbnail_name))

    render_json["recent_renders"] = updated_render_list
    write_json_data(render_json)

