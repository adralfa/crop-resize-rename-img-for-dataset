# Image Resizing and Renaming Script
This Python script processes a set of image files by cropping them to a 1:1 aspect ratio (if needed), resizing them to a specified resolution, and renaming them according to the folder structure. The script ensures the images are saved in a new destination folder while maintaining the original subfolder structure.

## Features
- Automatic Cropping: Images that are not square (1:1 aspect ratio) are automatically cropped to make them square before resizing.
- Resizing: Images are resized to the specified resolution (e.g., 128x128 pixels) using high-quality resampling (LANCZOS).
- Folder Structure Preservation: The script recreates the folder structure from the source directory in the destination directory.
- File Renaming: Each image file is renamed based on its original folder name and a counter, ensuring unique filenames in the destination.

## Requirements
- Python 3.x
- Pillow (Python Imaging Library)

## Installing Pillow
Before running the script, install the required library: `pip install pillow`

## How to Use
1. Clone this repository or copy the script to your local machine.
2. Set the `parent_folder` variable to the path where your source images are stored.
3. Set the `destination_folder` variable to the path where you want the processed images to be saved.
4. Specify the desired image size by adjusting the `final_size` variable (e.g., `(128, 128)`).
5. Run the script: `python image_resizing_script.py`

## Example Code Snippet
```
parent_folder = 'your_parent_folder_path'
destination_folder = 'your_destination_folder_path'
final_size = (128, 128)
```

## Output
- Images will be saved in the destination folder with the same subfolder structure as the source.
- Files will be renamed based on the folder they originated from, followed by a unique counter. For example, if the image is in a folder named `ship`, the output file could be `ship1.jpg`, `ship2.jpg`, etc. You can change the name format on `new_name = f"{folder_name}{counter}{ext}"`.

## Notes
- The script only processes image files with the following extensions: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`.
- If the destination folder does not exist, the script will create it.
- High-quality resampling is used for image resizing to preserve as much detail as possible.
