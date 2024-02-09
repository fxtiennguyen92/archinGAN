from handle_image import *
import subprocess
import shutil

def run_batch_fenestration():
    print("Running fenestration model")
    batch_script = "python test.py --dataroot ./uploads/temps/ --name fenestration"
    subprocess.run(batch_script, shell=True, capture_output=True, text=True)

def run_batch_roomlayouts():
    print("Running room layout model")
    batch_script = "python test.py --dataroot ./uploads/temps/ --name roomlayouts"
    subprocess.run(batch_script, shell=True, capture_output=True, text=True)

def run_batch_furnishing():
    print("Running furnishing model")
    batch_script = "python test.py --dataroot ./uploads/temps/ --name furnishing"
    subprocess.run(batch_script, shell=True, capture_output=True, text=True)

def clear_temps_data():
    print("Clear temps data")
    shutil.rmtree('uploads/temps')

if __name__ == '__main__':
    image = 'francis.png'
    
    #if (after_uploaded(image)):
    #    run_batch_fenestration()
    #if (after_fenestration_batch(image)):
    #    run_batch_roomlayouts()
    #if (after_roomlayout_batch(image)):
    #    run_batch_furnishing()
    
    after_uploaded(image)
    run_batch_roomlayouts()
    after_roomlayout_batch(image)
    run_batch_furnishing()
    
    clear_temps_data()
    
    