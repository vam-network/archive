from PIL import Image

# Open the image
image = Image.open('sample.png')

# Define the maximum size
max_length = 300
max_width = 800

# Get the original size of the image
original_width, original_height = image.size

# Calculate the new size while maintaining aspect ratio
width_ratio = original_width / max_width
height_ratio = original_height / max_length
if width_ratio > 1 or height_ratio > 1:
    resize_ratio = max(width_ratio, height_ratio)
    new_width = int(original_width / resize_ratio)
    new_height = int(original_height / resize_ratio)
else:
    new_width = original_width
    new_height = original_height

# Resize the image
image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

# Save the resized image
image.save('resizedSample.png')
