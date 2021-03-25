from workflows.COVID_workflow import COVID_Workflow

def createClassificationWorkflow(workflow, tables, classifier, analyser):
    newWorkflow = None
    if workflow == "COVID":
        newWorkflow = COVID_Workflow(tables, classifier, analyser)
    return newWorkflow