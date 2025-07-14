# Image Compressor

A simple Python application that compresses images using Pillow (PIL) library.

## Features

- Compresses images by reducing quality and resizing
- Supports multiple image formats (JPEG, PNG, BMP, TIFF, WebP)
- Batch processing of all images in input folder
- Customizable compression settings
- Shows compression statistics
- Preserves image quality while reducing file size

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your images in the `input` folder
2. Run the application:
```bash
python app.py
```
3. Follow the prompts to customize compression settings (optional)
4. Compressed images will be saved in the `output` folder

## Default Settings

- **Quality**: 85% (JPEG compression quality)
- **Resize Factor**: 0.8 (images resized to 80% of original dimensions)

## Supported Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff, .tif)
- WebP (.webp)

## Output

- All compressed images are saved as JPEG format
- Original filename + "_compressed" suffix
- Displays compression statistics for each image

## Example

```
Original: photo.png (2.5 MB, 1920x1080)
Compressed: photo_compressed.jpg (450 KB, 1536x864)
Size reduction: 82%
```
