from pathlib import Path
import OpenEXR
import Imath
import numpy as np
from PIL import Image

def linear_to_srgb(linear):
    """Convert linear color space to sRGB."""
    srgb = np.where(linear <= 0.0031308,
                    12.92 * linear,
                    1.055 * np.power(linear, 1.0 / 2.4) - 0.055)
    return np.clip(srgb, 0, 1)

def process_exr_to_proxy(input_file: Path, output_dir: Path, proxy_scale: float, img_format: str, progress_callback=None):
    output_file = output_dir / f"{input_file.stem}.{img_format}"
    
    exr_file = OpenEXR.InputFile(str(input_file))
    
    dw = exr_file.header()['dataWindow']
    width, height = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)

    dpw = exr_file.header()['displayWindow']
    dp_w, dp_h = (dpw.max.x - dpw.min.x + 1, dpw.max.y - dpw.min.y + 1)
    
    # Read the channels
    channels = ['R', 'G', 'B']
    data = [np.frombuffer(exr_file.channel(c, Imath.PixelType(Imath.PixelType.FLOAT)), dtype=np.float32) for c in channels]
    data = [d.reshape((height, width)) for d in data]
    
     # Stack channels into an image
    img = np.dstack(data)
    
    # Convert linear to sRGB
    img = linear_to_srgb(img)
    
    # Convert to PIL Image for saving
    img = Image.fromarray((img * 255).astype(np.uint8))

    # Calculate the cropping box
    left = (width - dp_w)/2
    top = (height - dp_h)/2
    right = left + dp_w
    bottom = top + dp_h
    
    # Center crop the image to the display window size
    img = img.crop((left, top, right, bottom))
    
    # Resize image
    new_size = (int(dp_w * proxy_scale), int(dp_h * proxy_scale))
    pil_img = img.resize(new_size, Image.Resampling.NEAREST)
    
    # Save image
    pil_img.save(output_file)

     # Call the callback function if provided
    if progress_callback:
        progress_callback()
