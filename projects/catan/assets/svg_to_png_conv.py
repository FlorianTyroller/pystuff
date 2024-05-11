import os
import cairosvg

def convert_svgs_to_pngs(input_directory, output_directory=None):
    """
    Converts all SVG files found in the input_directory to PNG format,
    saving them in the output_directory. If output_directory is not specified,
    the PNG files are saved in the same directory as the SVG files.
    """
    # If no output directory provided, use the input directory
    if output_directory is None:
        output_directory = input_directory

    # Make sure output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate over all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".svg"):
            # Construct full file path
            svg_path = os.path.join(input_directory, filename)
            png_path = os.path.join(output_directory, filename.replace(".svg", ".png"))

            # Convert SVG to PNG
            cairosvg.svg2png(url=svg_path, write_to=png_path)
            print(f"Converted '{svg_path}' to '{png_path}'")

if __name__ == "__main__":
    # Set the directory containing SVG files and the directory to save PNG files
    folder = ["cards", "cities", "roads", "settlements", "tiles"]
    for f in folder:
        input_dir = f"C:/Users/Flori/Desktop/pypy/projects/catan/assets/svgs/{f}"  # Replace with your SVG directory path
        output_dir = f"C:/Users/Flori/Desktop/pypy/projects/catan/assets/pngs/{f}" # Replace with your desired output directory path

        # Convert all SVG files in the directory
        convert_svgs_to_pngs(input_dir, output_dir)
