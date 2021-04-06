from featureSelectors.tableExtractors.extractor import Extractor
import pandas as pd
pd.options.mode.chained_assignment = None

# Extractor for the procedures.csv
class ProceduresExtractor(Extractor):

    def __init__(self, data, outcomes):
        self.data = data
        self.outcomes = outcomes

    def extractFeatures(self):
        self.manuallyRemoveFeatures()
        self.transformData()
        return super().dataFrameToDict(self.data), self.returnImputeData()

    # only keep a list of patients
    def manuallyRemoveFeatures(self):
        features_to_keep = ['PATIENT']
        self.data = self.data[features_to_keep]

    # If patient is in table then HADPROCEDURE = 1 else 0
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

    # Return 0 if not in table
    def returnImputeData(self):
        return [0]
