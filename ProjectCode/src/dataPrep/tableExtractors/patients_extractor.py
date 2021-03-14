from .extractor import Extractor

# Extractor for the patient's .csv
class PatientsExtractor(Extractor):

    def __init__(self, data, outcomes):
        self.data = data
        self.outcomes = outcomes

    def extractFeatures(self):
        
        return [], []