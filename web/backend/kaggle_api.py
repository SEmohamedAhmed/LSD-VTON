import subprocess
import kaggle

project_path = r' D:\Mohamed\FCIS\4th\GP\VITON\VITONY'
notebook_id = 'mrmody476/isthisgppretrained-gp-vton'


def execute_cmd_command(command):
    # Execute the command
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    # Print the output of the command
    return result.stdout


def pull_kaggle_dataset(dataset_id):
    command = fr'kaggle datasets metadata -p {project_path}\web\dataset {dataset_id}'
    return execute_cmd_command(command)


def update_kaggle_dataset():
    # dataset folder should have dataset-metadat.json and you dataset
    command = (fr'kaggle datasets version -r tar -p {project_path}\web\dataset '
               '-m "Updated data using mody kaggle public api"')
    return execute_cmd_command(command)


def pull_kaggle_notebook():
    command = fr'kaggle kernels pull -m {notebook_id} -p {project_path}\web\notebook'
    return execute_cmd_command(command)


def run_kaggle_notebook():
    """
        To run (push) a kaggle notebook You Must Do a pull before running
        You Should have the ipynb & metadata of the notebook
        you are trying to push in notebook directory
    """
    command = fr'kaggle kernels push -p {project_path}\web\notebook'
    return execute_cmd_command(command)


def get_kaggle_notebook_status():
    # We need "complete" status to retrieve our target output
    command = f'kaggle kernels status {notebook_id}'
    return execute_cmd_command(command)


def get_kaggle_notebook_output():
    command = fr'kaggle kernels output {notebook_id} -p {project_path}\web\notebook_output'
    return execute_cmd_command(command)

