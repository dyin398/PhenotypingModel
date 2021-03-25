from featureSelectors.tableExtractors.extractor import Extractor
import pandas as pd
pd.options.mode.chained_assignment = None

# Extractor for the patient's .csv
class ObservationsExtractor(Extractor):

    def __init__(self, data, outcomes):
        self.data = data
        self.outcomes = outcomes
        self.keepCodes = ['8310-5', '9279-1', '8867-4', '2708-6', '8462-4', '8480-6', '29463-7']

    def extractFeatures(self):
        self.manuallyRemoveFeatures()
        self.transformData()
        return super().dataFrameToDict(self.data), self.returnImputeData()

    def manuallyRemoveFeatures(self):
        features_to_keep = ['PATIENT', 'CODE', 'VALUE']
        self.data = self.data[features_to_keep]

    def transformData(self):
        feature_dict = {}
        keepCodesSet = {'8310-5', '9279-1', '8867-4', '2708-6', '8462-4', '8480-6', '29463-7'}
        values = self.data.values
        for i in values:
            if i[0] not in feature_dict:
                feature_dict[i[0]] = {}
            if i[1] in keepCodesSet and (i[1] not in feature_dict[i[0]] or i[2] > feature_dict[i[0]][i[1]]):
                feature_dict[i[0]][i[1]] = i[2]
        formattedValues = self.formatValues(feature_dict)
        self.data = self.valuesToDataFrame(formattedValues)

    def formatValues(self, dict):
        feature_dict = {}
        averageValues = [37.2, 16, 80, 95, 70, 105, 62]
        for key in dict:
            arr = []
            for i in range(len(self.keepCodes)):
                code = self.keepCodes[i]
                if code in dict[key]:
                    arr.append(dict[key][code])
                else:
                    arr.append(averageValues[i])
            feature_dict[key] = arr
        return feature_dict

    def valuesToDataFrame(self, formattedValues):
        newdict = {'PATIENT' : [], '8310-5' : [], '9279-1' : [], '8867-4' : [], '2708-6' : [], '8462-4' : [], '8480-6' : [], '29463-7' : []}
        for key in formattedValues:
            newdict['PATIENT'].append(key)
            data = formattedValues[key]
            newdict['8310-5'].append(data[0])
            newdict['9279-1'].append(data[1])
            newdict['8867-4'].append(data[2])
            newdict['2708-6'].append(data[3])
            newdict['8462-4'].append(data[4])
            newdict['8480-6'].append(data[5])
            newdict['29463-7'].append(data[6])
        return pd.DataFrame(newdict)

    def returnImputeData(self):
        return [37.2, 16, 80, 95, 70, 105, 62]