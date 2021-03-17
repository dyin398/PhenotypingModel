from dataPrep.data_preparation import DataWrangler
from utils.classifiers import logisticRegression, getClassificationReport, getConfusionMatrix, getAccuracyScore

wrangler = DataWrangler()
patient_features, patient_outcomes = wrangler.wrangleData()
y_test, predictions = logisticRegression(patient_features, patient_outcomes)
print(getClassificationReport(y_test, predictions))
print(getConfusionMatrix(y_test, predictions))
print(getAccuracyScore(y_test, predictions))