from os import path
import pandas as pd
from csv import writer
import os

from featureSelectors.tableExtractors.extractor_factory import createExtractor
pd.options.mode.chained_assignment = None

# Class which cleans data in inputData folder and outputs clean data
# formatted and ready to be input into a classifier
class FeatureSelector():

    def __init__(self, tables):
        # list of table names to extract
        self.tables = tables
        # map of patients to an array of features
        self.patients = {}
        # array of indicating the meaning of features for transparency
        self.feature_names = []
        # map of patients to their outcomes
        self.patient_outcomes = {}
        # input folder path
        self.data_folder_path = "resources/largeInputData"
        self.output_path = "resources/outputData/features.csv"

    # Method to iterate through inputData and calls necessary functions to clean data
    # and returns output data
    def wrangleData(self):
        self.extractPatients()
        self.extractPatientOutcomes()
        for filename in self.tables:
            filepath = self.data_folder_path + "/" + filename
            if path.isfile(filepath):
                data = pd.read_csv(filepath)
                new_features, feature_names, impute_values = self.prepareData(data, filename)
                self.addNewData(new_features, feature_names, impute_values)
        self.printData()
        return self.getDataAsArrays(), self.feature_names
        
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
    
    # create objects to prepare data for each table
    def prepareData(self, data, filename):
        new_features = {}
        feature_names = []
        impute_values = []
        extractor = createExtractor(filename, data, self.patient_outcomes)
        if extractor != None:
            [new_features, feature_names], impute_values = extractor.extractFeatures()
        return new_features, feature_names, impute_values

    def printData(self):
        self.removeOutputFile()
        csv_output = ["PATIENT"] + self.feature_names  + ["Outcome"]
        write_obj = open(self.output_path, 'w', newline='')
        csv_writer = writer(write_obj)
        csv_writer.writerow(csv_output)
        for key in self.patients:
            with open(self.output_path, 'a+', newline='') as write_obj:
                list_of_elem = [key] + self.patients[key] + [self.patient_outcomes[key]]
                csv_writer = writer(write_obj)
                csv_writer.writerow(list_of_elem)

    def removeOutputFile(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)