import pyautogui
from PIL import Image, ImageFilter, ImageEnhance
import pytesseract

# Step 1: Define the coordinates of the region of interest (ROI)
top_left_x, top_left_y = 915, 335
bottom_right_x, bottom_right_y = 1315, 735


# Step 2: Capture the screenshot within the specified ROI
screenshot = pyautogui.screenshot(region=(top_left_x, top_left_y, bottom_right_x - top_left_x, bottom_right_y - top_left_y))

# Step 3: Split the image into smaller sections and process each section
count = 1
section_width = screenshot.width // 5
section_height = screenshot.height // 5
crop_margin = 27  # Additional margin for cropping

for row in range(5):
    for col in range(5):
        # Calculate the coordinates for each section
        section_top_left_x = col * section_width
        section_top_left_y = row * section_height
        section_bottom_right_x = section_top_left_x + section_width
        section_bottom_right_y = section_top_left_y + section_height

        # Apply the additional margin for cropping
        section_top_left_x += crop_margin
        section_top_left_y += crop_margin
        section_bottom_right_x -= crop_margin
        section_bottom_right_y -= crop_margin

        # Extract the smaller section from the screenshot
        section = screenshot.crop((section_top_left_x, section_top_left_y, section_bottom_right_x, section_bottom_right_y))

        # Resize the section to a larger size
        resize_factor = 3  # Increase this value for larger size
        resized_section = section.resize((section.width * resize_factor, section.height * resize_factor), Image.BOX)

        # Apply image filters to enhance the edges and contrast
        sharpened_section = resized_section.filter(ImageFilter.SHARPEN)
        enhanced_section = ImageEnhance.Contrast(sharpened_section).enhance(100.0)  # Increase the contrast factor as needed

        # Perform letter recognition on the enhanced section
        letter = pytesseract.image_to_string(enhanced_section, config='--psm 6').strip()

        # Save the section as an individual image for verification
        enhanced_section.save(f'section_{count}.png')

        # Print the result
        print(f"Image {count}: {letter}")

        count += 1