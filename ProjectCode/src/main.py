from dataPrep.data_preparation import DataWrangler

wrangler = DataWrangler()
patient_features, patient_outcomes = wrangler.wrangleData()