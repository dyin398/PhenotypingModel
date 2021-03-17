from dataPrep.tableExtractors.extractor import Extractor
import pandas as pd

# Extractor for the patient's .csv
class ProceduresExtractor(Extractor):

    def __init__(self, data, outcomes):
        self.data = data
        self.outcomes = outcomes

    def extractFeatures(self):
        self.manuallyRemoveFeatures()
        self.transformData()
        return super().dataFrameToDict(self.data), self.returnImputeData()

    def manuallyRemoveFeatures(self):
        features_to_keep = ['PATIENT']
        self.data = self.data[features_to_keep]

    def transformData(self):
        patients = self.data['PATIENT'].tolist()
        patientset = set()
        for patient in patients:
            patientset.add(patient)
        output_dict = {'PATIENT': [], 'HADPROCEDURE' : []}
        for key in self.outcomes:
            output_dict['PATIENT'].append(key)
            if key in patientset:
                output_dict['HADPROCEDURE'].append(1)
            else:
                output_dict['HADPROCEDURE'].append(0)
        self.data = pd.DataFrame(output_dict)

    def returnImputeData(self):
        return [0]
