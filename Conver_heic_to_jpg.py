import os
from PIL import Image
import pillow_heif

# Register HEIF format
pillow_heif.register_heif_opener()


def convert_heic_to_jpg(heic_path, jpg_path):
    # Open HEIC file using PIL directly as pillow_heif registers the format
    image = Image.open(heic_path)

    # Convert to RGB mode if not already
    if image.mode in ("RGBA", "P"):  # Convert palette mode images to RGB
        image = image.convert("RGB")

    # Save the image as a JPG file
    image.save(jpg_path, "JPEG")


def convert_folder_heic_to_jpg(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(folder_path, filename)
            jpg_path = os.path.splitext(heic_path)[0] + ".jpg"
            print(f"Converting {heic_path} to {jpg_path}")
            convert_heic_to_jpg(heic_path, jpg_path)


# Example usage:
folder_path = r"F:\Pics\New folder"
convert_folder_heic_to_jpg(folder_path)
