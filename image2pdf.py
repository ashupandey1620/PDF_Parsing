from PIL import Image
import os

def images_to_pdf(image_folder, output_path):
    images = [Image.open(os.path.join(image_folder, f)) for f in sorted(os.listdir(image_folder)) if f.endswith(('.png', '.jpg'))]
    images[0].save(output_path, save_all=True, append_images=images[1:])
