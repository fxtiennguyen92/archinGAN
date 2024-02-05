from cvc_fp import *
import os

folder_path = "dataset/ImagesGT"
files = [file for file in os.listdir(folder_path) if file.endswith('.svg')]
file_paths = [(folder_path + '/' + file_name)  for file_name in files]

classes = (
    'Door',
    'Window',
    'Room',
    'Wall',
)
parsed = {path: parse_svg(path, classes) for path in file_paths}

directory = './dataset/footprints'

FootprintInputLayer.samples_to_imgs(parsed, directory)