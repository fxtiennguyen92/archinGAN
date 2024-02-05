import requests
import os
from urllib.parse import urlparse

# Function to download image
def download_image(url, folder):
    # Create folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Get the filename from the URL
    filename = os.path.join(folder, os.path.basename(urlparse(url).path))
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Write the content to a file
    with open(filename, "wb") as f:
        f.write(response.content)


###--- Room Layouts ---###
# input_url = "_mir_-1-inputs.png"
# output_url = "_mir_-1-outputs.png"
# base_url = "https://stanislaschaillou.com/thesis/GAN/unit_opening_results/images/"
# ifrom = 139
# ito = 169
# base_path = "dataset/roomlayouts"
        
###--- Furnishing ---###
input_url = "-outputs-inputs.png"
output_url = "-outputs-outputs.png"
base_url = "https://stanislaschaillou.com/thesis/GAN/unit_furnishing_results/images/"
ifrom = 140
ito = 168
base_path = "dataset/furnishing"


for i in range(ifrom, ito):
    base_input_url = base_url + str(i) + input_url
    # Download the image
    download_image(base_input_url, base_path + "/inputs")  
    
    base_output_url = base_url + str(i) + output_url
    download_image(base_output_url, base_path + "/outputs")

