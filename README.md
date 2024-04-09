# Orange FHIR Widget development project

## Overview
The project aims to explore and analyze Fast Healthcare Interoperability Resources (FHIR) through the combined use of the Orange tool and Python. The project aims to improve the efficiency of day-to-day operations by providing eventual healthcare providers with easy access to detailed, relevant and readily understandable information. Through the creation of custom widgets in Python and integration with Orange, the project aims to simplify the process of FHIR data extraction while ensuring clear visualization and in-depth understanding of medical information. In this way, it aims to increase the quality of clinical decisions and foster collaboration among health professionals, thus contributing to a more efficient and patient-centered healthcare environment.
The project, has the potential to become a starting point for future developments. Its flexible structure and ability to implement additional features not only make it suitable for user learning, but also likely to be adopted and developed by health professionals. Its dynamic nature could help fill specific analytical gaps in the context of FHIR resources, providing added value even for more advanced professional needs and promoting innovation in health informatics.

## Results
1. ***EDA Patient resource***:
   The first workflow focused on descriptive analysis of the Patient resource with graphs and tables.
   Among the results of this analysis were the relationship between QALYs (Quality-adjusted life years) and DALYs (Disability-adjusted life years) values, taking into account the marital status and age of the patients.
   
<img width="483" alt="image" src="https://github.com/marinoalfonso/FHIRresources_Orange/assets/166382565/6318932d-368d-4367-9850-66691702793d">


2. ***Analysis of PHQ-2 and Tobacco Smocking Status NHIS surveys***:
Workflow number 2 is concerned with the examination related to information from patient surveys, specifically regarding the PHQ-2 and Tobacco Smocking Status NHIS. 
The intent of this workflow is to explain how survey results are distributed among patients of different genders.

<img width="412" alt="image" src="https://github.com/marinoalfonso/FHIRresources_Orange/assets/166382565/4c8a11bd-9b2b-470f-adc0-85e1381ffdb2">


3. ***BMI classification***: The third workflow was developed with the objective of classifying individuals according to their BMI (Body Mass Index) and defining which category has the most occurrences in the sample.

<img width="482" alt="image" src="https://github.com/marinoalfonso/FHIRresources_Orange/assets/166382565/10863cfd-c33e-4503-8bce-8e64ffd755ea">


## Repository structure
* ***setup.py***: used to ensure smooth deployment and proper integration of widgets into the Orange environment.
* ***init.py***: related to the setup file. 
* ***fhirCaricamento.py***: the first widget file, designed to load FHIR resources from JSON files. 
* ***FHIRinputPatient.py & FHIRinputObservation.py***: Once the files are loaded, it will be necessary to extract from them the resources of our interest and then prepare the data for subsequent analysis and transformation into table format, respecting the parameters provided by Orange for the creation of Data Tables. An in-depth discussion is made here about the Observation and Patient resources and their loading widgets.
* ***WORKFLOW.ows***: workflow files developed in Orange environment
* ***Analisi dati FHIR in Orange.docx***: project documentation in docx format.
* ***Presentazione.pptx***: presentation of the project in power point format. 

## Usage

To use the Orange FHIR Widget:
1. Install Orange and its dependencies and [Synthea sample syntetic patients records](https://synthea.mitre.org/downloads), that are the JSON files used.
2. Clone this repository to your local machine in according to [guidelines](https://orange3.readthedocs.io/projects/orange-development/en/latest/tutorial.html).
3. Run the setup.py file to integrate the widget into Orange.
4. Use the provided scripts to load and extract FHIR resources.
5. To install widgets from Python to Orange, you need to operate in the same working environment, then interact with the terminal with "***pip install .***". 
6. Explore the Orange workflows for data analysis and visualization.

## Contact

For any questions, suggestions, or feedback, feel free to contact me.

Happy coding! 🚀
