from PIL import Image
import os
from customize_image import crop_and_resize

def concat_images_horizontally(image_name, image1, image2):
    width1, height1 = image1.size
    width2, height2 = image2.size
    total_width = width1 + width2
    max_height = max(height1, height2)

    new_image = Image.new("RGB", (total_width, max_height))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (width1, 0))
    
    folder_path = 'uploads/temps/test'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    save_path = os.path.join(folder_path, image_name)
    new_image.save(save_path)

def create_blank_image_like(image):
    width, height = image.size
    return Image.new("RGB", (width, height), "white")

def after_uploaded(image_name):
    folder_path = 'uploads'
    image_path = os.path.join(folder_path, image_name)
    
    crop_and_resize(image_path)
    
    given_image = Image.open(image_path)
    blank_image = create_blank_image_like(given_image)
    
    concat_images_horizontally(image_name, given_image, blank_image)
    return True

def after_fenestration_batch(image_name):
    folder_path = 'results/fenestration'
    image_fake_name = image_name[:-4] + '_fake_B' + image_name[-4:]

    image_path = os.path.join(folder_path, image_fake_name)
    given_image = Image.open(image_path)
    blank_image = create_blank_image_like(given_image)
    concat_images_horizontally(image_name, given_image, blank_image)
    return True

def after_roomlayout_batch(image_name):
    folder_path = 'results/roomlayouts'
    image_fake_name = image_name[:-4] + '_fake_B' + image_name[-4:]

    image_path = os.path.join(folder_path, image_fake_name)
    given_image = Image.open(image_path)
    blank_image = create_blank_image_like(given_image)
    concat_images_horizontally(image_name, given_image, blank_image)
    return True

