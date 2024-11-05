# Image Resizer

A simple Python script for resizing images using `OpenCV`. This tool allows you to resize an image by a specified percentage and save the resized image in a new file.

## Features:

Resize an image to a custom scale percentage.

Save the resized image in a specified output file format.

Preview the resized image in a display window.

## Requirements:

### Python 3.x

### OpenCV (cv2)

## Installation:

#### Clone this repository to your local machine:

    git clone https://github.com/your-username/Image_Resizer.git
    cd Image_Resizer

#### Install the required OpenCV library if not already installed:

    pip install opencv-python

## Usage:

Place the **source image** (e.g., `srk.jpg`) in the repository folder.

Set the `source`, `destination`, and `scale_percent` variables in the script:

    source = "srk.jpg"        # Path to the original image
    destination = "newSrk.png"  # Path for saving the resized image
    scale_percent = 50         # Resize percentage (e.g., 50% of original size)

Run the script:

bash
Copy code
python image_resizer.py
The resized image will be saved as newSrk.png in the same folder. The script will display the resized image in a preview window. Press any key to close the window.

Code Overview
The script follows these steps:

Load the Image: Loads the specified image using cv2.imread().
Calculate New Dimensions: Calculates the new width and height based on the specified scale_percent.
Resize the Image: Uses cv2.resize() to resize the image.
Save and Display the Image: Saves the resized image using cv2.imwrite() and optionally displays it in a new window.
Example
For a 50% resize of an image named srk.jpg, set scale_percent = 50, then run the script. The output file (newSrk.png) will be half the size of the original image.

Potential Enhancements
Command-line Arguments: Allow setting parameters like source image, destination file, and scale percentage via command-line options.
Aspect Ratio Resize: Enable resizing by specifying a target width or height while maintaining the original aspect ratio.
Batch Processing: Resize multiple images at once.
License
This project is licensed under the MIT License.

