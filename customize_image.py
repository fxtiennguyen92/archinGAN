from PIL import Image
import os

def crop_and_resize(image_path):
    # Open the image
    image = Image.open(image_path)
    # Convert image to RGB mode if it's not already in that mode
    image = image.convert("RGB")
    
    # Get the image data
    pixels = image.load()
    width, height = image.size
    
    # Make white background
    for x in range(width):
        for y in range(height):
            # Get the RGB values of the pixel
            r, g, b = pixels[x, y]
            # Check if the pixel color matches the old color
            if 220 <= r < 255 and 220 <= g < 255 and 220 <= b < 255:
                # Change the pixel color to the new color
                pixels[x, y] = (255, 255, 255)
    
    # Define the minimum and maximum x and y coordinates for non-white pixels
    min_x = width
    max_x = 0
    min_y = height
    max_y = 0
    
    # Iterate over each pixel in the image to find the bounding box of non-white pixels
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            if r != 255 or g != 255 or b != 255:  # If not white
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)
    
    # Crop the image using the bounding box
    image = image.crop((min_x, min_y, max_x, max_y))
    
    # Determine the size of the square image
    padding = 10
    size = max(max_x - min_x + padding, max_y - min_y + padding)
    
    # Create a new square image with white background
    new_image = Image.new("RGB", (size, size), (255, 255, 255))
    
    # Paste the cropped image onto the center of the new square image
    new_image.paste(image, ((size - (max_x - min_x)) // 2, (size - (max_y - min_y)) // 2))
    
    # Resize the image to 256x256
    new_image = new_image.resize((256, 256))
    
    # Save the modified image
    new_image.save(image_path)