from utils import *
from kaggle_api import *
import time


def tryon(person_id, cloth_id):
    # to erase .png from the string id
    person_id = remove_file_extension(person_id)
    cloth_id = remove_file_extension(cloth_id)

    # prepare the dataset
    make_dataset(person_id, cloth_id)

    time.sleep(5)

    # upload a new dataset version in kaggle
    update_kaggle_dataset()

    time.sleep(20)

    # get inference notebook.ipynb and its metadata
    pull_kaggle_notebook()

    time.sleep(5)

    # enable gpu for the notebook
    edit_json_file(r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web'
                   r'\notebook\kernel-metadata.json', 'enable_gpu', True)

    run_kaggle_notebook()

    # wait until finishing the notebook run
    while True:
        current_notebook_status = get_kaggle_notebook_status()
        if 'complete' in current_notebook_status:
            break

    # get tryon result (notebook output)
    get_kaggle_notebook_output()

    # copy our result into tryon_results directory
    shutil.copy(fr'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\notebook_output\{person_id}.png___{cloth_id}.png',
                fr'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\frontend\static\tryon_results\{person_id}___{cloth_id}.png')

    return person_id, cloth_id
