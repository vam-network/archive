from PIL import Image

# Open the main image
main_image = Image.open('sample.png')

# Open the logo image
logo_image = Image.open('fflogo.png')

# Resize the logo image to 100% of the main image
logo_size = tuple([int(1 * x) for x in logo_image.size])
logo_image = logo_image.resize(logo_size)

# Calculate the positions of the center and corners
main_width, main_height = main_image.size
logo_width, logo_height = logo_image.size
center_x = (main_width - logo_width) // 2
center_y = (main_height - logo_height) // 2
corner_x = [0, main_width - logo_width, 0, main_width - logo_width, center_x]
corner_y = [0, 0, main_height - logo_height, main_height - logo_height, center_y]

# Paste the logos onto the main image at the center and corner positions
for i in range(5):
    main_image.paste(logo_image, (corner_x[i], corner_y[i]), logo_image)

# Save the modified image
main_image.save('watermarkedSample.png')
