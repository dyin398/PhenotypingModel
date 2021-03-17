from dataPrep.tableExtractors.extractor import Extractor
import pandas as pd
pd.options.mode.chained_assignment = None

# Extractor for the patient's .csv
class SuppliesExtractor(Extractor):

    def __init__(self, data, outcomes):
        self.data = data
        self.outcomes = outcomes

    def extractFeatures(self):
        self.manuallyRemoveFeatures()
        self.transformData()
        return super().dataFrameToDict(self.data), self.returnImputeData()

    def manuallyRemoveFeatures(self):
        features_to_keep = ['PATIENT', 'QUANTITY']
        self.data = self.data[features_to_keep]

    def transformData(self):
        supplies_data = self.data.values.tolist()
        newDict = {}
        for i in supplies_data:
            if i[0] in newDict:
                newDict[i[0]] = newDict[i[0]] + i[1]
            else:
                newDict[i[0]] = i[1]
        self.data = pd.DataFrame(newDict.items(), columns=['PATIENT', 'SUPPLY_COUNT'])

    def returnImputeData(self):
        return [0]
