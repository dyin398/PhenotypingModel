from featureSelectors.tableExtractors.extractor import Extractor
from utils.extractor_methods import kendallTau, standardiseData, PCAalgorithm
import pandas as pd
import statistics
pd.options.mode.chained_assignment = None

# Extractor for the patient's .csv
class ConditionsExtractor(Extractor):

    def __init__(self, data, outcomes):
        self.data = data
        self.outcomes = outcomes
        self.codes = data.CODE.unique()

    def extractFeatures(self):
        self.manuallyRemoveFeatures()
        self.transformData()
        self.featureSelection()
        return super().dataFrameToDict(self.data), self.returnImputeData()

    def manuallyRemoveFeatures(self):
        features_to_keep = ['PATIENT', 'CODE']
        self.data = self.data[features_to_keep]
        self.data = self.data[self.data.CODE != 840539006]
        self.data = self.data[self.data.CODE != 840544004]

    def transformData(self):
        feature_dict = self.getEmptyFeatureDict()
        feature_dict = self.populateFeatureDict(feature_dict)
        feature_array_dict = self.getFeatureArrayDict(feature_dict)
        self.alterData(feature_array_dict)

    def featureSelection(self):
        newData = self.data
        input = newData.drop(['PATIENT', 'Outcome'], axis=1)
        input = standardiseData(input)
        output = PCAalgorithm(input, 3)
        output = pd.DataFrame(output)
        self.data = self.data[['PATIENT', 'Outcome']]
        self.data = pd.concat([self.data, output], axis=1)
        self.data.rename(columns={0 : 'conditions1', 1 : 'conditions2', 2 : 'conditions3'}, inplace=True)
        self.data = self.data.drop('Outcome', axis=1)

    # Returns dictionary of all patients to empty set
    def getEmptyFeatureDict(self):
        feature_dict = {}
        for i in self.outcomes:
            feature_dict[i] = set()
        return feature_dict

    # Populates an empty feature dict with patient to set of condition codes
    def populateFeatureDict(self, feature_dict):
        list = self.data.values.tolist()
        for i in list:
            feature_dict[i[0]].add(i[1])
        return feature_dict

    # Turn feature dictionary to array of patient to boolean list of conditions
    # matching self.codes
    def getFeatureArrayDict(self, feature_dict):
        feature_array_dict = {}
        for i in feature_dict:
            arr = []
            for code in self.codes:
                if code in feature_dict[i]:
                    arr.append(1)
                else:
                    arr.append(0)
            feature_array_dict[i] = arr
        return feature_array_dict

    def alterData(self, feature_array_dict):
        newDict = {}
        newDict['PATIENT'] = []
        newDict['Outcome'] = []
        for code in self.codes:
            newDict[code] = []
        for key in feature_array_dict:
            newDict['PATIENT'].append(key)
            newDict['Outcome'].append(self.outcomes[key])
            for i in range(len(self.codes)):
                newDict[self.codes[i]].append(feature_array_dict[key][i])
        self.data = pd.DataFrame(newDict)

    def returnImputeData(self):
        columns = ['conditions1', 'conditions2', 'conditions3']
        imputeData = []
        for column in columns:
            group = self.data[column]
            groupList = group.values.tolist()
            imputeData.append(statistics.median(groupList))
        return imputeData
