from Orange.data import Domain, StringVariable, DiscreteVariable, ContinuousVariable, Table, Values, Tuple
from Orange.widgets import widget, gui, settings
from Orange.widgets.utils.signals import Input, Output
import json
from Orange.widgets.utils import widgetpreview
import re 
import requests
import pandas as pd


class OWFhirTestInput(widget.OWWidget):
    name = "Input FHIR Patient"
    description = "test input"
    #category = "Prove widget fhir"
    
    class Inputs:
        list_of_paths = widget.Input("Bundle Resource Paths", list, auto_summary=False)

    class Outputs:
        processed_table = widget.Output("Processed Patient Table", Table)


    def __init__(self):
        super().__init__()

        self.result_dict = {} # dict for extracting all the nested info. in the resource
        self.data_values = [] # rows to append in the final table
        self.selected_files = [] # list of selected files
        self.string_values = [] # list of string values
        self.input_received = None # input received from the previous widget
        self.df = pd.DataFrame()
        self.all_dfs = [] # list of all dataframes
        box = gui.widgetBox(self.controlArea,"")
        box.setFixedHeight(100)
        self.test_input = "" # inital default value for input
        
        # input line for the fhir api
        self.input_line = gui.lineEdit(widget=box, master=self,value="test_input", 
                                       label="Input a fhir server endpoit to retrieve data for a patient ",validator=None,callback=self.validate_api)
        gui.button(box, master = self, label = "send", callback=self.validate_api) # button to send the input

        gui.separator(self)
        box2  = gui.widgetBox(self.controlArea,"") # box for displaying messages
        self.display_message = gui.widgetLabel(box2," ") # label for displaying messages   


    def validate_api(self): 
        api_pattern = r'^https?://(?:\w+\.)?\w+\.\w+(?:/\S*)?$' # regex for validating the input
        if re.match(api_pattern, self.test_input): 
            self.make_request()
        else:
            print("input a valid fhir api")
            self.display_message.setText("ERROR: Input a valid FHIR API")


    def make_request(self):
        try:
            response = requests.get(self.test_input)
        except:
            print("error while making request")
            self.display_message.setText("error while making request")
            return
        json_results = response.json()
        self.flatten_dict(json_results)
        print("results of processing: ", self.result_dict)
        self.create_table()
        
            
    def flatten_dict(self, d, key='', sep='_'):
        items = []
        for k, v in d.items():
            new_key = f"{key}{sep}{k}" if key else k

            if isinstance(v, dict):
                items.extend(self.flatten_dict(v, new_key, sep=sep).items())
            elif isinstance(v, list):
                for i, val in enumerate(v):
                    if isinstance(val, (dict, list)):
                        items.extend(self.flatten_dict(val, f"{new_key}_{i}", sep=sep).items())
                    else:
                        items.append((f"{new_key}_{i}", val))
            else:
                items.append((new_key, v))

        return dict(items)

        
    def commit_table(self):     
        self.data = [self.numeric_values[i] + self.string_values[i] for i in range(len(self.numeric_values))]
        output_table = Table.from_list(self.domain, self.data)

        self.Outputs.processed_table.send(output_table)

    def create_table(self):
        self.string_features = []
        self.cont_features = []
        
        final_df = pd.concat(self.all_dfs, ignore_index=True)
        self.data = final_df.values.tolist()
        
        numeric_columns = final_df.select_dtypes(include='number').columns # select numeric columns
        self.numeric_values = final_df[numeric_columns].values.tolist() # get the values of the numeric columns
        self.cont_features = [ContinuousVariable(name) for name in numeric_columns] # create a list of continuous variables

        string_columns = final_df.select_dtypes(exclude='number').columns # select string columns
        self.string_values = final_df[string_columns].values.tolist() # get the values of the string columns
        self.string_features = [StringVariable(name) for name in string_columns] # create a list of string variables

        self.domain = Domain(self.cont_features, metas=self.string_features) # create the domain
        
        
    def extract_resource(self, path):
        with open(path, "r") as f:
            bundle_data = json.load(f)
            entries = bundle_data.get("entry", [])
            for entry in entries:
                resource = entry.get("resource", {})
                if resource.get("resourceType") == "Patient":
    
                    self.result_dict = self.flatten_dict(resource)
                    self.df = pd.DataFrame([self.result_dict])
                    self.all_dfs.append(self.df)
                    self.create_table()
     
    @Inputs.list_of_paths
    def set_input(self, value):

        self.input_value = value
        if self.input_value is not None :
            self.data_values = []  # Clear previous data
            self.string_values = []  # Clear previous string data
            self.all_dfs = [] # Clear previous dataframes
        
            for path in self.input_value:
                self.extract_resource(path)
        
        self.commit_table()


#if __name__ == "__main__":
    #widgetpreview.WidgetPreview(OWFhirTestInput).run()


