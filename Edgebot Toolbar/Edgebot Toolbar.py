# Author: Ryan Perez (c) 2020
# Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

##########################################################################################
#                   Creating new toolbar panel                                           #
##########################################################################################
        workSpace = ui.workspaces.itemById('FusionSolidEnvironment')
        tbPanels = workSpace.toolbarPanels
        
        global tbPanel
        tbPanel = tbPanels.itemById('HAAS EdgeBot')
        if tbPanel:
            tbPanel.deleteMe()
        tbPanel = tbPanels.add('HAAS EdgeBot', 'HAAS Edgebot', 'Corner', False)
##########################################################################################
#                   Creating Button for toolbar panel                                    #
##########################################################################################

        #creating button for the Edgebot Main handler
        #get the command definitons collection
        commandDefinitions = ui.commandDefinitions
        EdgeBotButtonDefinition = commandDefinitions.addButtonDefinition('EdgeBotMainHandler','HAAS Edgebot','Start main Edgebot program','resources')

        #grabbing the correct toolbar panel to add the button to
        addinsToolbarPanel = ui.allToolbarPanels.itemById('HAAS EdgeBot')
        #Adding the Edgebot button to the toolbar panel
        EdgeBotButtonControl=addinsToolbarPanel.controls.addCommand(EdgeBotButtonDefinition, 'EdgeBotButtonControl')
        #making the button visible without having to use the dropdown
        EdgeBotButtonControl.isPromotedByDefault = True
        EdgeBotButtonControl.isPromoted = True

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


def stop(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('Stop addin')
        if tbPanel:
            tbPanel.deleteMe()

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
