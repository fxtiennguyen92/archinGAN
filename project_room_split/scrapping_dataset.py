import requests
from bs4 import BeautifulSoup
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

#input_url = "_mir_-1-inputs.png"
#output_url = "_mir_-1-outputs.png"
#base_url = "https://stanislaschaillou.com/thesis/GAN/unit_opening_results/images/"
#ifrom = 139
#ito = 169

input_url = "-input.png"
output_url = "-targets.png"
base_url = "https://stanislaschaillou.com/thesis/GAN/images/"
ifrom = 501
ito = 600

for i in range(ifrom, ito):
    base_input_url = base_url + str(i) + input_url
    # Download the image
    download_image(base_input_url, "space/inputs")  
    
    base_output_url = base_url + str(i) + output_url
    download_image(base_output_url, "space/outputs")

