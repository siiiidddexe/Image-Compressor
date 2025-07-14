import os
from PIL import Image
import sys

def compress_image(input_path, output_path, quality=85, resize_factor=0.8):
    """
    Compress an image by reducing quality and optionally resizing it.
    
    Args:
        input_path (str): Path to the input image
        output_path (str): Path to save the compressed image
        quality (int): JPEG quality (1-100, lower = more compression)
        resize_factor (float): Factor to resize the image (0.8 = 80% of original size)
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Get original format
            original_format = img.format
            
            # Get original dimensions
            original_width, original_height = img.size
            
            # Calculate new dimensions
            new_width = int(original_width * resize_factor)
            new_height = int(original_height * resize_factor)
            
            # Resize the image
            img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Save the compressed image in original format
            if original_format in ['JPEG', 'JPG']:
                # Convert to RGB if necessary (for JPEG compatibility)
                if img_resized.mode in ('RGBA', 'LA', 'P'):
                    img_resized = img_resized.convert('RGB')
                img_resized.save(output_path, 'JPEG', quality=quality, optimize=True)
            elif original_format == 'PNG':
                img_resized.save(output_path, 'PNG', optimize=True)
            elif original_format == 'WEBP':
                img_resized.save(output_path, 'WEBP', quality=quality, optimize=True)
            else:
                # For other formats (BMP, TIFF, etc.), save as JPEG
                if img_resized.mode in ('RGBA', 'LA', 'P'):
                    img_resized = img_resized.convert('RGB')
                img_resized.save(output_path, 'JPEG', quality=quality, optimize=True)
            
            # Get file sizes for comparison
            original_size = os.path.getsize(input_path)
            compressed_size = os.path.getsize(output_path)
            compression_ratio = (original_size - compressed_size) / original_size * 100
            
            print(f"✓ Compressed: {os.path.basename(input_path)}")
            print(f"  Original size: {original_size:,} bytes")
            print(f"  Compressed size: {compressed_size:,} bytes")
            print(f"  Size reduction: {compression_ratio:.1f}%")
            print(f"  Dimensions: {original_width}x{original_height} → {new_width}x{new_height}")
            print("-" * 50)
            
    except Exception as e:
        print(f"✗ Error processing {input_path}: {str(e)}")

def process_images(input_folder, output_folder, quality=85, resize_factor=0.8):
    """
    Process all images in the input folder and save compressed versions to output folder.
    
    Args:
        input_folder (str): Path to the input folder containing images
        output_folder (str): Path to the output folder for compressed images
        quality (int): JPEG quality (1-100)
        resize_factor (float): Factor to resize images
    """
    # Supported image formats
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.webp')
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Get list of image files
    image_files = []
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(supported_formats):
            image_files.append(filename)
    
    if not image_files:
        print("No supported image files found in the input folder.")
        print(f"Supported formats: {', '.join(supported_formats)}")
        return
    
    print(f"Found {len(image_files)} image(s) to process...")
    print("=" * 50)
    
    # Process each image
    for filename in image_files:
        input_path = os.path.join(input_folder, filename)
        
        # Keep the same filename as input
        output_filename = filename
        output_path = os.path.join(output_folder, output_filename)
        
        compress_image(input_path, output_path, quality, resize_factor)

def main():
    # Default paths
    input_folder = "input"
    output_folder = "output"
    
    # Default compression settings
    quality = 85  # JPEG quality (1-100)
    resize_factor = 0.8  # Resize to 80% of original size
    
    print("🖼️  Image Compressor")
    print("=" * 50)
    
    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"❌ Input folder '{input_folder}' not found!")
        print("Please create the 'input' folder and add your images to it.")
        return
    
    # Check if there are any files in the input folder
    if not os.listdir(input_folder):
        print(f"📁 Input folder '{input_folder}' is empty!")
        print("Please add some images to the input folder.")
        return
    
    # Allow user to customize settings
    print(f"Current settings:")
    print(f"  - Quality: {quality}% (lower = more compression)")
    print(f"  - Resize factor: {resize_factor} (smaller = more size reduction)")
    print()
    
    # Ask user if they want to change settings
    change_settings = input("Do you want to change the compression settings? (y/n): ").lower().strip()
    
    if change_settings == 'y':
        try:
            new_quality = input(f"Enter JPEG quality (1-100, current: {quality}): ").strip()
            if new_quality:
                quality = max(1, min(100, int(new_quality)))
            
            new_resize = input(f"Enter resize factor (0.1-1.0, current: {resize_factor}): ").strip()
            if new_resize:
                resize_factor = max(0.1, min(1.0, float(new_resize)))
                
        except ValueError:
            print("Invalid input, using default settings.")
    
    print()
    print("Starting compression...")
    print("=" * 50)
    
    # Process the images
    process_images(input_folder, output_folder, quality, resize_factor)
    
    print("✅ Compression complete!")
    print(f"Compressed images saved to '{output_folder}' folder.")

if __name__ == "__main__":
    main()
