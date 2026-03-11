import os
from PIL import Image

# -------- CONFIG --------
RAW_FOLDER = "../photos/raw"
OUTPUT_FOLDER = "../photos/thumbs"
# Maximum thumbnail size (keeps aspect ratio)
MAX_SIZE = (600, 600)
# JPEG compression quality (0–100)
QUALITY = 80
# Supported image formats
EXTENSIONS = [".jpg", ".jpeg", ".png"]
# ------------------------

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


for file in os.listdir(RAW_FOLDER):

    # Split filename and extension
    name, ext = os.path.splitext(file)

    # Skip files that are not supported image formats
    if ext.lower() not in EXTENSIONS:
        continue

    raw_path = os.path.join(RAW_FOLDER, file)
    output_path = os.path.join(OUTPUT_FOLDER, name + ".jpg")

    
    img = Image.open(raw_path)

    # Create thumbnail while preserving aspect ratio
    thumb = img.copy()
    thumb.thumbnail(MAX_SIZE)

    # Save thumbnail as compressed JPEG
    thumb.save(output_path, "JPEG", quality=QUALITY, optimize=True)

    print(f"Thumbnail: {file}")

print("Thumbnails done.")