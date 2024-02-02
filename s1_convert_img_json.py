import os
from raster_to_json import *

RPLAN_PATH = "rplan_image"

def main():
    args = parse_args()
    folder_path=args.path
    if (folder_path == None):
        folder_path = RPLAN_PATH
    
    # read all files
    files = os.listdir(folder_path)

    try:
        for file_name in files:
            line = folder_path + '/' + file_name
            raster_to_json(line, print_door_warning=False)
    except (AssertionError, ValueError, IndexError) as e:
        fp_id = line.split("/")[-1].split(".")[0]

        with open(f"rplan_json_failed/{fp_id}", "w") as f:
            f.write(str(e))

if __name__ == "__main__":
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        main()