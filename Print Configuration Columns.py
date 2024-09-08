#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        design=adsk.fusion.Design.cast(app.activeProduct)

        # Check if this is a configured design.
        if not design.isConfiguredDesign:
            ui.messageBox("Error: The current design is not configured! This script can only run on configured designs.")
            return
        
        # Get each configuration
        topTable = design.configurationTopTable

        app.log("Configurations Columns: ")
        
        for col in topTable.columns:
            app.log("Column: {}".format(col.title))

        app.log("Done")

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
