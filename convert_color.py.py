from PIL import Image

def change_color(image_path):
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
    image.save("modified_image.png")

# Example usage
image_path = "dataset/s2_floorplan/FootprintInputLayer__RepartitionInputLayer/train/2_gt_16.png"
change_color(image_path)