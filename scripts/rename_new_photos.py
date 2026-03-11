import os
import re

# -------- CONFIG --------
RAW_FOLDER = "../photos/raw"
# Tracks the highest existing number in filenames
max_number = 0

# Edit regex pattern and prefix as needed
# Prefix used for renamed files (e.g., photo1.jpg, photo2.jpg)
PREFIX = "photo"
# Regex pattern to detect already-renamed files
# Example match: photo12
REGEX_PATTERN = r"^photo(\d+)$"
EXTENSIONS = [".jpg", ".jpeg", ".png"]
# ------------------------

# Compile regex for faster matching
pattern = re.compile(REGEX_PATTERN, re.IGNORECASE)

files = os.listdir(RAW_FOLDER)

# Detect the highest number already used in filenames
for file in files:

    name, ext = os.path.splitext(file)

    # Skip unsupported file types
    if ext.lower() not in EXTENSIONS:
        continue

    # Check if filename already follows the naming pattern
    match = pattern.match(name)

    if match:
        num = int(match.group(1))
        max_number = max(max_number, num)
        
# Start numbering from the next available number
counter = max_number + 1

# Rename new files
for file in files:

    path = os.path.join(RAW_FOLDER, file)

    if not os.path.isfile(path):
        continue

    name, ext = os.path.splitext(file)

    if ext.lower() not in EXTENSIONS:
        continue

    if pattern.match(name):
        continue

    # Generate new sequential filename
    new_name = f"{PREFIX}{counter}{ext.lower()}"
    new_path = os.path.join(RAW_FOLDER, new_name)

    # Rename file
    os.rename(path, new_path)

    print(f"{file} → {new_name}")

    counter += 1

print("Rename complete.")