from featureSelectors.tableExtractors.patients_extractor import PatientsExtractor
from featureSelectors.tableExtractors.supplies_extractor import SuppliesExtractor
from featureSelectors.tableExtractors.observations_extractor import ObservationsExtractor
from featureSelectors.tableExtractors.procedures_extractor import ProceduresExtractor
from featureSelectors.tableExtractors.conditions_extractor import ConditionsExtractor

# Factory for data extractors. Returns specific extractor for specific file
def createExtractor(filename, data, outcomes):
    extractor = None
    if filename == "supplies.csv":
        extractor = SuppliesExtractor(data, outcomes)
    elif filename == "procedures.csv":
        extractor = ProceduresExtractor(data, outcomes)
    elif filename == "conditions.csv":
        extractor = ConditionsExtractor(data, outcomes)
    elif filename == "patients.csv":
        extractor = PatientsExtractor(data, outcomes)
    elif filename == "observations.csv":
        extractor = ObservationsExtractor(data, outcomes)
    return extractor