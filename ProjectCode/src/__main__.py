from workflows.workflow_factory import createClassificationWorkflow

# Name of workflow required
workflow = "COVID"

def main():
    createClassificationWorkflow(workflow)

if __name__ == "__main__":
    main()