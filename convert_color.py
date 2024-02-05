from PIL import Image
import os

def change_color(image_path, dest_path):
    # Open the image
    image = Image.open(image_path)
    # Convert image to RGB mode if it's not already in that mode
    image = image.convert("RGB")
    
    # Get the image data
    pixels = image.load()
    width, height = image.size
    
    # Iterate over each pixel
    for x in range(width):
        for y in range(height):
            # Get the RGB values of the pixel
            r, g, b = pixels[x, y]
            # Check if the pixel color matches the old color
            if (r, g, b) == (195, 164, 110):
                # Change the pixel color to the new color
                pixels[x, y] = (0, 255, 5)
    
    # Iterate over each pixel
    for x in range(width):
        for y in range(height):
            # Get the RGB values of the pixel
            r, g, b = pixels[x, y]
            # Check if the pixel color matches the old color
            if (r, g, b) == (141, 171, 86) or (r, g, b) == (62, 145, 90):
                # Change the pixel color to the new color
                pixels[x, y] = (251, 7, 0)
                
    # Save the modified image
    image.save(dest_path)

input_folder = 'dataset/fenestration'
dest_folder = 'dataset/fenestration/val'

filenames = os.listdir(input_folder)
for filename in filenames:
    image_path = os.path.join(input_folder, filename)
    dest_path = os.path.join(dest_folder, filename)
    change_color(image_path, dest_path)