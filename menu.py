import nukescripts
import recentRenders

# nukescripts.registerWidgetAsPanel('DisplayRenders', "RecentRenders", 'uk.co.thefoundry.DisplayRenders', True)

menu = nuke.toolbar('Nodes')
menu.addCommand('RRenders', 'recentRenders.run()')
