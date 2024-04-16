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
    pull_kaggle_dataset(r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\dataset',
                        r'mrmody476/vitonhdmody')

    update_kaggle_dataset(r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\dataset')

    time.sleep(20)

    # get inference notebook.ipynb and its metadata
    pull_kaggle_notebook(r'mrmody476/isthisgppretrained-gp-vton',
                         r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\notebook')

    time.sleep(5)

    # enable gpu for the notebook
    edit_json_file(r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web'
                   r'\notebook\kernel-metadata.json', 'enable_gpu', True)

    run_kaggle_notebook(r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\notebook')

    # wait until finishing the notebook run
    while True:
        current_notebook_status = get_kaggle_notebook_status(r'mrmody476/isthisgppretrained-gp-vton')
        if 'complete' in current_notebook_status:
            break

    # get tryon result (notebook output)
    get_kaggle_notebook_output(r'mrmody476/isthisgppretrained-gp-vton')

    # copy our result into tryon_results directory
    shutil.copy(fr'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\notebook_output\{person_id}.png___{cloth_id}.png',
                fr'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\frontend\static\tryon_results\{person_id}___{cloth_id}.png')

    return person_id, cloth_id


def mody_vton(person_id, cloth_id):
    os.rename(fr'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\notebook_output\upper___{person_id}___{cloth_id}',
              r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\mody_contribution_dataset\lfgp_warping_result.jpg')

    crop_image(r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\mody_contribution_dataset\lfgp_warping_result.jpg',
               r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\mody_contribution_dataset\lfgp_warping_result.jpg')

    with open(r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\mody_contribution_dataset\testContribution.txt', 'w') as f:
        f.write(f'{person_id} {cloth_id}')

    # update the dataset mody_contribution_dataset
    pull_kaggle_dataset(r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\mody_contribution_dataset',
                        r'mrmody476/warping-results-mody-contribution')

    update_kaggle_dataset(r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\mody_contribution_dataset')

    # run HuntingDenosingUnet notebook via kaggl api
    pull_kaggle_notebook(r'mrmody476/huntingdenosingunet',
                         r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\notebook')

    # enable gpu for the notebook
    edit_json_file(r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web'
                   r'\notebook\kernel-metadata.json', 'enable_gpu', True)

    # enable gpu for the notebook
    edit_json_file(r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web'
                   r'\notebook\kernel-metadata.json', 'enable_internet', True)

    run_kaggle_notebook(r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\notebook')

    # wait until finishing the notebook run
    while True:
        current_notebook_status = get_kaggle_notebook_status(r'mrmody476/huntingdenosingunet')
        if 'complete' in current_notebook_status:
            break

    # get tryon result (notebook output)
    get_kaggle_notebook_output(r'mrmody476/huntingdenosingunet')

    # copy our result into tryon_results directory
    shutil.copy(fr'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\notebook_output\unpaired\upper_body\{person_id}.png',
                fr'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\frontend\static\tryon_results\{person_id}___{cloth_id}___mody_vton.png')
