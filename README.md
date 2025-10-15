<div align="center">
  <h1>Universal Image Viewer</h1>
  <p>
    A simple, lightweight image viewer for Windows, macOS, and Linux that natively opens HEIC/HEIF and other common formats.
  </p>
  
  <p>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Made%20with-Python-blue.svg" alt="Made with Python"></a>
    <a href="#"><img src="https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey" alt="Cross-Platform"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="License"></a>
  </p>
</div>

---

### 🖼️ Key Features

-   ✅ **Native HEIC/HEIF Support**: Open `.heic` and `.heif` files without needing external converters.
-   ✅ **Broad Format Compatibility**: Supports dozens of common image formats.
-   ✅ **User-Friendly**: Uses your system's default image viewer for a familiar experience.
-   ✅ **Preserves Filenames**: Temporarily converts images to PNG but keeps the original filename for easy identification.
-   ✅ **Cross-Platform**: Fully functional on Windows, macOS, and Linux.
-   ✅ **Standalone**: Can be compiled into a single executable with no dependencies required.

### 📁 Supported File Types

This application can open a wide variety of image formats:

| Format        | Extensions                  |
| :------------ | :-------------------------- |
| **HEIF/AVIF** | `.heic`, `.heif`, `.avif`   |
| **Web** | `.jpeg`, `.jpg`, `.png`, `.gif`, `.webp` |
| **Bitmap** | `.bmp`, `.ico`, `.ppm`, `.pcx` |
| **Advanced** | `.tiff`, `.tif`, `.psd`, `.eps`, `.pdf`, `.svg` |

### ⚙️ How It Works

The script leverages the **Pillow** and **pillow-heif** libraries to open a given image file. It then saves a temporary, lossless PNG version of the image to your system's temporary directory. Finally, it calls the default system image viewer to display this temporary file, ensuring the window title reflects the original file's name.

### 🚀 Getting Started

#### Prerequisites

You must have Python 3 installed. Then, install the required libraries using pip:

```bash
pip install Pillow pillow-heif
````

#### Running the Script

To view an image, run the script from your terminal and pass the file path as an argument.

```bash
python Universal_Image_Viewer.py "C:\path\to\your\image.heic"
```

### 📦 Building the Executable

You can compile this script into a single, standalone executable using **PyInstaller**. This allows anyone to use the viewer without installing Python.

1.  **Install PyInstaller:**
    ```bash
    pip install pyinstaller
    ```
2.  **Build the Executable:**
    Run the following command in your terminal from the project's root directory. Make sure `app_icon.ico` and `version_info.txt` are present.
    ```bash
    python -m PyInstaller --onefile --windowed --name="Universal Image Viewer" --icon="app_icon.ico" --version-file="version_info.txt" Universal_Image_Viewer.py
    ```
    The final `.exe` file will be located in the newly created `dist` folder.

\<details\>
\<summary\>\<strong\>Breakdown of the Build Command\</strong\>\</summary\>

  - `--onefile`: Bundles everything into a single executable file.
  - `--windowed`: Prevents a console window from appearing when the application is run.
  - `--name="Universal Image Viewer"`: Sets the name of the final executable.
  - `--icon="app_icon.ico"`: Assigns your custom icon to the application.
  - `--version-file="version_info.txt"`: Embeds file metadata (like company name, product name, and description) into the executable's properties.

\</details\>

-----

### 👨‍💻 Author

  * **N.Z**

### 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
