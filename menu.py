import nuke

import recentRenders
import config
from utils import recentRenderUpdate


nuke.knobDefault("Write.afterRender", "recentRenderUpdate.update_renders_data()")

menu = nuke.toolbar('Nodes')
menu.addCommand('Recent Renders', lambda: recentRenders.run(), icon=config.MAIN_ICON.replace("\\", "/"))
