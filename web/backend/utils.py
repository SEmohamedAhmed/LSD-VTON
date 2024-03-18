import os
import shutil

main_dataset_path = r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\dataset'


def delete_files_in_folder(folder_path):
    """
        Deletes all files in the specified folder and its subfolders.
    """
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            if folder_path == main_dataset_path:
                continue
            os.remove(item_path)
        elif os.path.isdir(item_path):
            # Recursively delete files in subfolders
            delete_files_in_folder(item_path)


def make_dataset(person_id, cloth_id):
    """
        we assume we cleared last dataset images using delete_files_in_folder function
        we need to
            - have a dataset of 1 row only which is the target one
            - fill all folders based on current ids
                cloth
                cloth_mask
                cloth_parse
                dense
                image
                openpose_json
                parse
            - create a txt file hase 'pid cid upper'
    """
    test_path = r'D:\Mohamed\FCIS\4th\GP\VITON\Dataset\VITON-HD[DO NOT EDIT]\test'
    CLOTH_LABELS = ['cloth', 'cloth_mask', 'cloth_parse']
    PERSON_LABELS = ['image', 'dense', 'parse']
    for label in CLOTH_LABELS:
        shutil.copy(fr'{test_path}\{label}\{cloth_id}.png',
                    fr'{main_dataset_path}\{label}\{cloth_id}.png')

    for label in PERSON_LABELS:
        shutil.copy(fr'{test_path}\{label}\{person_id}.png',
                    fr'{main_dataset_path}\{label}\{person_id}.png')

    shutil.copy(fr'{test_path}\openpose_json\{person_id}_keypoints.json',
                fr'{main_dataset_path}\openpose_json\{person_id}_keypoints.json')

    path = r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\requirements.txt'
    with open(path, 'w') as file_writer:
        file_writer.write(f'{person_id}.png {cloth_id}.png upper')


delete_files_in_folder(main_dataset_path)