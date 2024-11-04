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

		# Format for copy/paste into spreadsheet
		formatAsHeaders=False
		formatResult=ui.messageBox("Print as comma seperated headers?", "Print Format", adsk.core.MessageBoxButtonTypes.YesNoButtonType) 
		if formatResult == adsk.core.DialogResults.DialogYes:
			formatAsHeaders=True
		elif formatResult == adsk.core.DialogResults.DialogCancel:
			return

		# Get each configuration
		topTable = design.configurationTopTable

		app.log("Configurations Columns: ")
		
		if formatAsHeaders:
			app.log(",".join([col.title for col in topTable.columns]))
		else:
			for col in topTable.columns:
				#app.log("Column: {}: {}".format(col.objectType, col.title)) # Include types
				if col.objectType == adsk.fusion.ConfigurationFeatureAspectColumn.classType():
					app.log("Column: {} [Aspect: {}, Type: {}, Feature: {}]".format(col.title, col.aspectType, col.objectType, col.feature.objectType)) # No types
				else:
					app.log("Column: {} [Type: {}]".format(col.title, col.objectType)) # No types

		app.log("Done")

	except:
		if ui:
			ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
