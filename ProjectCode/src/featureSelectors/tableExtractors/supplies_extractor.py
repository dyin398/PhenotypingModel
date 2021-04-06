from featureSelectors.tableExtractors.extractor import Extractor
import pandas as pd
pd.options.mode.chained_assignment = None

# Extractor for the supplies .csv
class SuppliesExtractor(Extractor):

    def __init__(self, data, outcomes):
        self.data = data
        self.outcomes = outcomes

    def extractFeatures(self):
        self.manuallyRemoveFeatures()
        self.transformData()
        return super().dataFrameToDict(self.data), self.returnImputeData()

    # keep only patients and their quantity of supplies
    def manuallyRemoveFeatures(self):
        features_to_keep = ['PATIENT', 'QUANTITY']
        self.data = self.data[features_to_keep]

    # sum up the quantity of supplies for each patient
    def transformData(self):
        supplies_data = self.data.values.tolist()
        newDict = {}
        for i in supplies_data:
            if i[0] in newDict:
                newDict[i[0]] = newDict[i[0]] + i[1]
            else:
                newDict[i[0]] = i[1]
        self.data = pd.DataFrame(newDict.items(), columns=['PATIENT', 'SUPPLY_COUNT'])

    # 0 supplies if not in table
    def returnImputeData(self):
        return [0]
