import os
from PIL import Image

# -------- CONFIG --------
RAW_FOLDER = "../photos/raw"
# Folder where optimized images for the website will be saved
OUTPUT_FOLDER = "../photos/optimize"

# Maximum width/height for website viewing images
MAX_SIZE = (2500, 2500)

# JPEG compression quality (0–100)
QUALITY = 90
EXTENSIONS = [".jpg", ".jpeg", ".png"]
# ------------------------

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file in os.listdir(RAW_FOLDER):
    # Separate filename and extension
    name, ext = os.path.splitext(file)

    # Skip unsupported file types
    if ext.lower() not in EXTENSIONS:
        continue

    raw_path = os.path.join(RAW_FOLDER, file)
    output_path = os.path.join(OUTPUT_FOLDER, name + ".jpg")

    img = Image.open(raw_path)

    # Resize image while keeping aspect ratio
    optimized = img.copy()
    optimized.thumbnail(MAX_SIZE)

    # Save optimized version as compressed JPEG
    optimized.save(output_path, "JPEG", quality=QUALITY, optimize=True)

    print(f"Optimized: {file}")

print("Full images done.")