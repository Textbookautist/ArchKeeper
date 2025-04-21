from PIL import Image
import os

script_path = os.path.dirname(os.path.abspath(__file__))

# Define directory and image filename
directory = os.path.join(script_path,"image_dir")  # Change to the actual directory path
filename = "sword.png"  # Adjust to the correct filename

# Construct full path to the image
image_path = os.path.join(directory, filename)

# Check if the image exists
if os.path.exists(image_path):
    # Open the image
    image = Image.open(image_path)

    # Rotate the image by 90 degrees (transposing)
    rotated_image = image.transpose(Image.ROTATE_90)

    # Save the rotated image
    rotated_image_path = os.path.join(directory, "rotated_" + filename)
    rotated_image.save(rotated_image_path)

    print(f"Rotated image saved as: {rotated_image_path}")
else:
    print("Image not found. Please check the path.")
