from workflows.COVID_workflow import COVID_Workflow

# factory for specific workflows
def createClassificationWorkflow(workflow):
    newWorkflow = None
    if workflow == "COVID":
        newWorkflow = COVID_Workflow()
    return newWorkflow