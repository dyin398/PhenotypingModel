import os
from os import path
import pandas as pd
import numpy as np
from .tableExtractors.patients_extractor import PatientsExtractor

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

        self.data_folder_path = "../resources/inputData"

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
                new_features, feature_names = self.prepareData(data, filename)
                self.addNewData(new_features, feature_names)
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

    #TODO: function that adds new features to fields
    def addNewData(self, new_features, feature_names):
        return
    
    # create objects to prepare data for each table. if we decide the table has no
    # relevance, then ignore it TODO: choose appropriate features
    def prepareData(self, data, filename):
        new_features = []
        feature_names = []
        extractor = None
        if filename == "careplans.csv":#TODO
            pass
        elif filename == "medications.csv":#TODO
            pass
        elif filename == "providers.csv":#TODO
            pass
        elif filename == "payer_transitions.csv":#TODO
            pass
        elif filename == "imaging_studies.csv":#TODO
            pass
        elif filename == "supplies.csv":#TODO
            pass
        elif filename == "payers.csv":#TODO
            pass
        elif filename == "procedures.csv":#TODO
            pass
        elif filename == "organizations.csv":#TODO
            pass
        elif filename == "conditions.csv":#TODO
            pass
        elif filename == "encounters.csv":#TODO
            pass
        elif filename == "devices.csv":#TODO
            pass
        elif filename == "immunizations.csv":#TODO
            pass
        elif filename == "patients.csv":#TODO
            extractor = PatientsExtractor(data, self.patient_outcomes)
        elif filename == "observations.csv":#TODO
            pass
        if extractor != None:
            new_features, feature_names = extractor.extractFeatures()
        return new_features, feature_names
