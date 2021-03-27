from workflows.COVID_workflow import COVID_Workflow

def createClassificationWorkflow(workflow):
    newWorkflow = None
    if workflow == "COVID":
        newWorkflow = COVID_Workflow()
    return newWorkflow