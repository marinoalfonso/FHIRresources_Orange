from setuptools import setup

setup(
    name="Analisi dati FHIR",
    packages=["orangedemo"],
    package_data={"orangedemo": ["icons/*.svg"]},
    classifiers=["Example :: Invalid"],
    entry_points={"orange.widgets": "Analisi dati FHIR = orangedemo"},
)

