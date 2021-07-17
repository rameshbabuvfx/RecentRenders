import nuke

import recentRenders

from utils import recentRenderUpdate


nuke.knobDefault("Write.afterRender", "recentRenderUpdate.update_renders_data()")

menu = nuke.toolbar('Nodes')
menu.addCommand('RRenders', 'recentRenders.run()')
