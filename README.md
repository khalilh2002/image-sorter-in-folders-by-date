# Image File Manager by Date

This Python script serves as a simple image file manager, organizing images based on the date embedded in their filenames. The script works by creating folders corresponding to the years extracted from image filenames, then moving the images into their respective year folders.

## How It Works

The script prompts the user to choose a directory and automatically organizes image files within it. It identifies images with specific prefixes, such as 'IMG,' 'PANO,' 'Scre,' and 'Snapchat,' or images with a valid year in the filename. For example, an image named "IMG20210522_12018.jpg" will be moved to the folder "2021_folder."

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

## How to Use

1. **Run the Script:**
   ```bash
   python image_file_manager_date.py
