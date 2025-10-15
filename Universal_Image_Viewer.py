import sys
import os
import tempfile
import subprocess
from PIL import Image
import pillow_heif

# Add HEIC/HEIF support to Pillow
pillow_heif.register_heif_opener()

def show_with_original_name(image_obj, original_path):
    """
    Saves an image to a temporary file with a meaningful name and opens it
    with the system's default viewer.
    """
    try:
        # 1. Get the base name of the original file without the extension
        # e.g., "C:/Photos/image.heic" -> "image"
        base_name = os.path.splitext(os.path.basename(original_path))[0]
        
        # 2. Create a new path for our temporary PNG file
        # e.g., "C:/Users/You/AppData/Local/Temp/image.png"
        temp_png_path = os.path.join(tempfile.gettempdir(), f"{base_name}.png")
        
        # 3. Save the image as a PNG (lossless) to that path
        image_obj.convert("RGB").save(temp_png_path)
        
        # 4. Open the temporary file using the correct command for the OS
        if sys.platform == "win32":
            # For Windows
            os.startfile(temp_png_path)
        elif sys.platform == "darwin":
            # For macOS
            subprocess.call(["open", temp_png_path])
        else:
            # For Linux
            subprocess.call(["xdg-open", temp_png_path])
            
    except Exception as e:
        # Handle potential errors, though unlikely
        print(f"Failed to show image: {e}")

def open_image(file_path):
    """Opens and displays any supported image file."""
    try:
        image = Image.open(file_path)
        # Use our new custom show function instead of the default one
        show_with_original_name(image, file_path)
    except Exception:
        pass # Fail silently if an error occurs

if __name__ == "__main__":
    # Check if a file path was passed as an argument
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        open_image(image_path)
