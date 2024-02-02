import os
import random
import shutil

def split_dataset(input_folder, output_folder, split_ratio=(0.7, 0.2, 0.1)):
    # Create output folders if they don't exist
    for folder in ['train', 'val', 'test']:
        os.makedirs(os.path.join(output_folder, folder), exist_ok=True)

    # Get list of image filenames
    filenames = os.listdir(input_folder)
    random.shuffle(filenames)

    # Calculate number of images for each split
    num_images = len(filenames)
    num_train = int(num_images * split_ratio[0])
    num_val = int(num_images * split_ratio[1])

    # Split filenames into train, val, and test sets
    train_filenames = filenames[:num_train]
    val_filenames = filenames[num_train:num_train + num_val]
    test_filenames = filenames[num_train + num_val:]

    # Move files to respective folders
    move_files(train_filenames, input_folder, os.path.join(output_folder, 'train'))
    move_files(val_filenames, input_folder, os.path.join(output_folder, 'val'))
    move_files(test_filenames, input_folder, os.path.join(output_folder, 'test'))

def move_files(filenames, source_folder, dest_folder):
    for filename in filenames:
        source_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(dest_folder, filename)
        shutil.copy(source_path, dest_path)

# Room layouts
#input_folder = 'room_layouts/combine'
#output_folder = 'dataset/room_layouts'

# Footprints
input_folder = 'footprints/combine'
output_folder = 'dataset/footprints'


split_ratio = (0.6, 0.2, 0.2)  # Train: 70%, Validation: 20%, Test: 10%

split_dataset(input_folder, output_folder, split_ratio)