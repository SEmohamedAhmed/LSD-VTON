import subprocess

project_path = r' D:\Mohamed\FCIS\4th\GP\VITON\VITONY'


def execute_cmd_command(command):
    # Execute the command
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    # Print the output of the command
    return result.stdout


def pull_kaggle_dataset(dataset_folder_path, dataset_id):
    command = fr'kaggle datasets metadata -p {dataset_folder_path} {dataset_id}'
    return execute_cmd_command(command)


def update_kaggle_dataset(dataset_folder_path):
    # dataset folder should have dataset-metadat.json and you dataset
    command = (fr'kaggle datasets version -r tar -p {dataset_folder_path} '
               '-m "Updated data using mody kaggle public api"')
    return execute_cmd_command(command)


def pull_kaggle_notebook(notebook_id, notebook_path):
    command = fr'kaggle kernels pull -m {notebook_id} -p {notebook_path}'
    return execute_cmd_command(command)


def run_kaggle_notebook(notebook_path):
    """
        To run (push) a kaggle notebook You Must Do a pull before running
        You Should have the ipynb & metadata of the notebook
        you are trying to push in notebook directory
    """
    command = fr'kaggle kernels push -p {notebook_path}'
    return execute_cmd_command(command)


def get_kaggle_notebook_status(notebook_id):
    # We need "complete" status to retrieve our target output
    command = f'kaggle kernels status {notebook_id}'
    return execute_cmd_command(command)


def get_kaggle_notebook_output(notebook_id):
    command = fr'kaggle kernels output {notebook_id} -p {project_path}\web\notebook_output'
    return execute_cmd_command(command)

