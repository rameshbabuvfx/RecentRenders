import nuke


def create_thumbnails():
    read_node = nuke.nodes.Read(file="D:/Footages/masterLayer_beauty.exr")
    write_node = nuke.nodes.Write(file="D:/Footages/masterLayer_.png")
    write_node.setInput(0, read_node)
    nuke.execute(write_node, 1, 1)


if __name__ == '__main__':
    create_thumbnails()

