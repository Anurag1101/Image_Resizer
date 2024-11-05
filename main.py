import cv2

# Define the source image and the destination file where the resized image will be saved
source = "srk.jpg"           # Path to the original image
destination = "newSrk.png"   # Path where the resized image will be saved

# Set the percentage by which to resize the image (e.g., 50% of the original size)
scale_percent = 50

# Load the original image from the specified source path
# `cv2.IMREAD_UNCHANGED` means the image is loaded as-is with no color or size adjustments
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# Check if the image was loaded successfully
if src is None:
    print("Error: Could not load the image.")
    exit()

# Calculate the new dimensions based on the scaling percentage
# Multiply original dimensions by the scale percentage and divide by 100 to get the scaled dimensions
new_width = int(src.shape[1] * scale_percent / 100)   # New width in pixels
new_height = int(src.shape[0] * scale_percent / 100)  # New height in pixels

# Resize the image to the new dimensions
output = cv2.resize(src, (new_width, new_height))

# Save the resized image to the specified destination path
cv2.imwrite(destination, output)
print(f"Resized image saved as {destination}")

# Display the resized image in a window (optional)
cv2.imshow("Resized Image", output)
cv2.waitKey(0)              # Wait until a key is pressed to close the window
cv2.destroyAllWindows()      # Close all OpenCV windows
