from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QFileDialog, QTextEdit
from Orange.widgets.widget import OWWidget, Output

class OWFhirLoading(OWWidget):
    name = "Caricamento FHIR"
    description = "Upload a FHIR resource bundle from a JSON file"
    #category = "Analisi dati FHIR"

    class Outputs:
        list_of_paths = Output("Bundle Resource Paths", list, auto_summary= False)

    def __init__(self):
        super().__init__()
        
        self.file_paths = [] # list of file paths
        self.init_ui() # initialize the user interface

    def init_ui(self):
        layout = QVBoxLayout() # create a vertical layout

        select_button = QPushButton("Select JSON file(s)") # create a button
        select_button.clicked.connect(self.upload_action) # connect the button to the upload action
        layout.addWidget(select_button) # add the button to the layout

        self.text_edit = QTextEdit() # create a text edit widget
        self.text_edit.setReadOnly(True) # make the text edit read-only
        layout.addWidget(self.text_edit) # add the text edit to the layout

        self.controlArea.layout().addLayout(layout) # add the layout to the widget's control area

    def upload_action(self): # this method is called when the user clicks the button
        app = QApplication.instance() # get the current application instance
        if app is None:
            app = QApplication([]) 

        dialog = QFileDialog() # create a file dialog
        dialog.setFileMode(QFileDialog.ExistingFiles) # set the file mode to allow multiple files to be selected
        dialog.setNameFilter("JSON files (*.json)") # set the name filter to only show JSON files
        
        #initial_directory = "/Users/alfonsomarino/Desktop/proveFHIR/fhir_example"
        #dialog.setDirectory(initial_directory)
        
        if dialog.exec_(): 
            file_paths = dialog.selectedFiles() # get the paths of the selected files
            print("Selected file paths:", file_paths) 
            self.file_paths = file_paths 
            self.update_display() # update the text edit widget
            self.commit() # send the file paths to the output
        else:
            print("No files selected")

    def update_display(self): 
        paths_text = "\n".join(self.file_paths)
        self.text_edit.setPlainText(paths_text) # set the text edit's text to the file paths

    def commit(self):
        self.Outputs.list_of_paths.send(self.file_paths)

#if __name__ == "__main__":
    #from AnyQt.QtWidgets import QApplication
    #from Orange.widgets.utils import widgetpreview

    #app = QApplication([])
    #widget_preview = widgetpreview.WidgetPreview(OWFhirLoading)
    #widget_preview.run()
    #app.exec_()





