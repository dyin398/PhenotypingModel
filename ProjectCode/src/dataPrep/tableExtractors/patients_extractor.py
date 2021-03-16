from dataPrep.tableExtractors.extractor import Extractor
from utils.data_prep_methods import PCAalgorithm, standardiseData
from datetime import datetime
import pandas as pd
import statistics

# Extractor for the patient's .csv
class PatientsExtractor(Extractor):

    def __init__(self, data, outcomes):
        self.data = data
        self.outcomes = outcomes

    def extractFeatures(self):
        self.manuallyRemoveFeatures()
        self.cleanData()
        self.transformData()
        self.featureSelection()
        return super().dataFrameToDict(self.data), self.returnImputeData()

    def manuallyRemoveFeatures(self):
        features_to_keep = ['Id', 'BIRTHDATE', 'MARITAL', 'RACE', 'GENDER', 'CITY']
        self.data = self.data[features_to_keep]

    # Function which cleans the data we've decided to keep for easier manipulation
    def cleanData(self):
        self.imputeData()

    def transformData(self):
        self.data['BIRTHDATE'] = self.data['BIRTHDATE'].apply(self.getAge)
        self.data['MARITAL'] = self.data['MARITAL'].apply(self.isMarried)
        self.data['GENDER'] = self.data['GENDER'].apply(self.isMale)
        self.data.rename({'BIRTHDATE': 'AGE', 'MARITAL': 'MARRIED', 'GENDER': 'MALE', 'Id': 'PATIENT'}, axis=1, inplace=True)
    
    def featureSelection(self):
        self.data.drop(['RACE', 'CITY'], axis=1, inplace=True)
        features = ['AGE', 'MARRIED', 'MALE']
        newData = self.reduceDimensionality(self.data[features])
        self.data.drop(features, axis=1, inplace=True)
        self.data = pd.concat([self.data, newData], axis=1)

    def imputeData(self):
        self.data['MARITAL'] = self.data['MARITAL'].fillna('S')

    def reduceDimensionality(self, data):
        standardised_features = standardiseData(data)
        components = PCAalgorithm(standardised_features, 1)
        newData = pd.DataFrame(data = components, columns = ['SOCIAL_GROUP'])
        return newData

    def returnImputeData(self):
        output = []
        socialGroup = self.data['SOCIAL_GROUP']
        groupList = socialGroup.values.tolist()
        output.append(statistics.median(groupList))
        return output
    
    def getAge(self, date):
        if isinstance(date, int):
            return date
        curryear = datetime.now().year
        birthyear = datetime.strptime(date, '%Y-%m-%d').year
        return curryear-birthyear

    def isMarried(self, status):
        if status == 'S':
            return 0
        elif status == 'M':
            return 1
        else:
            return status

    def isMale(self, gender):
        if gender == 'F':
            return 0
        elif gender == 'M':
            return 1
        else:
            return gender