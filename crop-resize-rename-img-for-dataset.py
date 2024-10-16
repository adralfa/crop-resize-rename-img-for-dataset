import os
from PIL import Image

# Set the parent folder and destination folder path
parent_folder = 'your_parent_folder_path'
destination_folder = 'your_destination_folder_path'
final_size = (width, height)  # Define the final size (e.g., 128x128)

# If the destination folder doesn't exist, create it
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# Function to create the same folder structure in the destination
def create_destination_folder(subfolder):
    destination_subfolder = os.path.join(destination_folder, os.path.relpath(subfolder, parent_folder))
    if not os.path.exists(destination_subfolder):
        os.makedirs(destination_subfolder)
    return destination_subfolder

# Traverse all subfolders and files within the parent folder
for root, dirs, files in os.walk(parent_folder):
    # Filter only image files with specific extensions (.jpg, .png, .jpeg, etc.)
    image_files = [f for f in files if f.endswith(('.jpg', '.png', '.jpeg', '.gif', '.bmp'))]

    # Create the corresponding destination folder structure
    destination_subfolder = create_destination_folder(root)

    # Get the current subfolder name to use in the new file name
    folder_name = os.path.basename(root)

    # Initialize a counter for file renaming
    counter = 1

    # Loop through each image file
    for image_file in image_files:
        # Set the source and destination image paths
        source_image_path = os.path.join(root, image_file)

        # Open the image
        with Image.open(source_image_path) as img:
            # Check if the image needs to be cropped to a 1:1 aspect ratio
            if img.width != img.height:
                # Determine the new crop size
                crop_size = min(img.width, img.height)
                left = (img.width - crop_size) // 2
                top = (img.height - crop_size) // 2
                right = (img.width + crop_size) // 2
                bottom = (img.height + crop_size) // 2

                # Crop the image
                img = img.crop((left, top, right, bottom))
            
            # Resize the image to the final size (e.g., 128x128) using resampling
            img = img.resize(final_size, resample=Image.LANCZOS)

            # Get the file extension
            ext = os.path.splitext(image_file)[1]
            
            # Create a new file name with the format: subfolder_name + counter + extension
            new_name = f"{folder_name}{counter}{ext}"
            counter += 1

            # Set the destination path with the new file name
            destination_image_path = os.path.join(destination_subfolder, new_name)

            # Save the resized image to the destination folder
            img.save(destination_image_path)

        print(f"Image {image_file} from folder {root} has been resized and saved as {new_name} in {destination_subfolder}.")

print("Process complete.")
