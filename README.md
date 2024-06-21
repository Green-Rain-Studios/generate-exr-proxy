# OpenEXR Proxy Generator

This utility processes `.exr` files from a specified input folder, converts them to proxy files at a specified scale, and saves them to an output folder in the specified image format. The utility is designed to be multithreaded for faster processing.

## Features
- Converts EXR files to proxy images.
- Supports multithreading for faster processing.
- Configurable output resolution and image format.
- Easy setup with a Windows batch script.

## Requirements
- Python 3.6 or later
- `pip` (Python package installer)

## Installation

1. **Clone the repository or download the source code.**

2. **Run the installation script to set up the virtual environment and install dependencies:**

   ```sh
   install.bat
   ```

   This script will:
   - Check if Python is installed.
   - Create a virtual environment in the `venv` directory.
   - Activate the virtual environment.
   - Install the required Python packages from `requirements.txt`.

## Usage

### Generating Proxies

#### Command Line Options

- `--input, -i` (required): Input folder for EXR processing.
- `--output, -o` (optional): Output folder (defaults to `input folder/proxy_<proxy_scale>`).
- `--proxy_scale, -s` (optional): Resolution scale of output frames (default: 0.5).
- `--img_format, -f` (optional): Output format of frames (default: png).
- `--threads, -t` (optional): Max threads to use (default: 5).

#### Example

```sh
bin\generate-exr-proxy.bat --input "C:\path\to\input" --output "C:\path\to\output" --proxy_scale 0.5 --img_format jpg --threads 10
```

This command will:
- Process all EXR files in `C:\path\to\input`.
- Save the proxy images to `C:\path\to\output`.
- Scale the output images to 50% of the original resolution.
- Save the output images in JPG format.
- Use up to 10 threads for processing.

## Notes

- This utility currently supports Windows due to the batch scripts. For other operating systems, you will need to create equivalent shell scripts for setting up the environment and running the main script.
- Ensure that the `OpenEXR` and `Imath` libraries are correctly installed in your Python environment.

## Contributions

Contributions are welcome. Please adhere to the following guidelines:

1. **Fork the repository** and create a new branch for your feature or bugfix.
2. **Write clear, concise commit messages**.
3. **Ensure your code follows the existing style** and includes relevant tests.
4. **Submit a pull request** with a detailed description of your changes.

All contributions will be reviewed before merging.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.