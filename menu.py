import nukescripts
import recentRenders

# nukescripts.registerWidgetAsPanel('DisplayRenders', "RecentRenders", 'uk.co.thefoundry.DisplayRenders', True)

menu = nuke.toolbar('Nodes')
render_menu = menu.addMenu('Recent_Renders')
render_menu.addCommand('Recent_Renders', 'recentRenders.run()')
