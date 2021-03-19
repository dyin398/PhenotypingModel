import os
from os import path
import pandas as pd
import numpy as np
from dataPrep.tableExtractors.patients_extractor import PatientsExtractor
from dataPrep.tableExtractors.supplies_extractor import SuppliesExtractor
from dataPrep.tableExtractors.observations_extractor import ObservationsExtractor
from dataPrep.tableExtractors.procedures_extractor import ProceduresExtractor
from dataPrep.tableExtractors.conditions_extractor import ConditionsExtractor
pd.options.mode.chained_assignment = None

# Class which cleans data in inputData folder and outputs clean data
# formatted and ready to be input into a classifier
class DataWrangler:

    def __init__(self):
        # map of patients to an array of features
        self.patients = {}
        # array of indicating the meaning of features for transparency
        self.feature_names = []
        # map of patients to their outcomes
        self.patient_outcomes = {}

        self.data_folder_path = "resources/inputData"

    # Method to iterate through inputData and calls necessary functions to clean data
    # and returns output data
    def wrangleData(self):
        self.extractPatients()
        self.extractPatientOutcomes()
        resources = os.fsdecode(self.data_folder_path)
        for file in os.listdir(resources):
            filename = os.fsdecode(file)
            if filename.endswith(".csv"):
                filepath = self.data_folder_path + "/" + filename
                data = pd.read_csv(filepath)
                new_features, feature_names, impute_values = self.prepareData(data, filename)
                self.addNewData(new_features, feature_names, impute_values)
        return self.getDataAsArrays()
        
    # Method to set patient_outcomes to 1 for patients who have COVID
    def extractPatientOutcomes(self):
        conditions_path = self.data_folder_path + "/conditions.csv"
        if path.isfile(conditions_path):
            conditions_data = pd.read_csv(conditions_path)
            has_condition = conditions_data[conditions_data['CODE'] == 840539006]
            patients = has_condition['PATIENT']
            for i in patients:
                self.patient_outcomes[i] = 1
    
    # Extract all patients from data
    def extractPatients(self):
        patients_path = self.data_folder_path + "/patients.csv"
        if path.isfile(patients_path):
            patient_data = pd.read_csv(patients_path)
            patients = patient_data['Id']
            for i in patients:
                self.patients[i] = []
                self.patient_outcomes[i] = 0

    # method that obtains data in array format
    def getDataAsArrays(self):
        features_list = []
        outcomes = []
        for key in self.patients:
            if key in self.patient_outcomes:
                features_list.append(self.patients[key])
                outcomes.append(self.patient_outcomes[key])
        return features_list, outcomes

    # function that adds new features to fields
    def addNewData(self, new_features, names, impute_values):
        self.addFeaturesToPatients(new_features, impute_values)
        self.addNamesToFeatures(names)

    def addFeaturesToPatients(self, new_features, impute_values):
        for key in self.patients:
            if key in new_features:
                self.patients[key] = self.patients[key] + new_features[key]
            else:
                self.patients[key] = self.patients[key] + impute_values
    
    def addNamesToFeatures(self, names):
        for i in names:
            if i != 'PATIENT' and i != 'Outcome':
                self.feature_names.append(i)
    
    # create objects to prepare data for each table. if we decide the table has no
    # relevance, then ignore it TODO: choose appropriate features
    def prepareData(self, data, filename):
        new_features = {}
        feature_names = []
        impute_values = []
        extractor = None
        if filename == "medications.csv":#TODO: see how it goes
            pass
        elif filename == "supplies.csv":
            extractor = SuppliesExtractor(data, self.patient_outcomes)
        elif filename == "procedures.csv":
            extractor = ProceduresExtractor(data, self.patient_outcomes)
        elif filename == "conditions.csv":
            extractor = ConditionsExtractor(data, self.patient_outcomes)
        elif filename == "devices.csv":#TODO: see how it goes
            pass
        elif filename == "immunizations.csv":#TODO: see how it goes
            pass
        elif filename == "patients.csv":
            extractor = PatientsExtractor(data, self.patient_outcomes)
        elif filename == "observations.csv":
            extractor = ObservationsExtractor(data, self.patient_outcomes)
        if extractor != None:
            [new_features, feature_names], impute_values = extractor.extractFeatures()
        return new_features, feature_names, impute_values
