import os
import shutil
import json

from PIL import Image

main_dataset_path = r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\dataset\test'


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
        clear last dataset
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
    delete_files_in_folder(main_dataset_path)
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

    path = r'D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\dataset\inference.txt'
    with open(path, 'w', encoding='utf-8') as file_writer:
        file_writer.write(f'{person_id}.png {cloth_id}.png upper')


def remove_file_extension(filename):
    """
    Removes the file extension from the given filename.

    Parameters:
    filename (str): The filename from which to remove the extension.

    Returns:
    str: The filename without the extension.
    """
    # Split the filename into the name and the extension
    name, _ = os.path.splitext(filename)
    return name


def edit_json_file(json_file_path, key, new_value):
    # Load the JSON data from a file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Change the 'enable_gpu' value to true
    data[key] = new_value

    # Write the modified data back to the file
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=2)


def crop_image(input_image_path, output_image_path, left=0, top=0, right=384, bottom=512):
    with Image.open(input_image_path) as img:
        # Crop the image
        cropped_img = img.crop((top, left, right, bottom))
        # Save the cropped image
        cropped_img.save(output_image_path)
