from workflows.workflow_factory import createClassificationWorkflow

# Inputs:
# List of tables to extract
tables = ["supplies.csv", "procedures.csv", "conditions.csv", "patients.csv", "observations.csv"]
# Name of desired classifier
classifier = "resources/outputData/trainedClassifier.sav"
# classifier = "Logistic Regression"
# Name of desired analyser
analyser = "COVID"
# Name of workflow required
workflow = "COVID"

def main():
    createClassificationWorkflow(workflow, tables, classifier, analyser)

if __name__ == "__main__":
    main()