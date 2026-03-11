import os
import re

# -------- CONFIG --------
RAW_FOLDER = "../photos/raw"
max_number = 0
#edit regex pattern and prefix as needed
PREFIX = "photo"
REGEX_PATTERN = r"^photo(\d+)$"
EXTENSIONS = [".jpg", ".jpeg", ".png"]
# ------------------------

pattern = re.compile(REGEX_PATTERN, re.IGNORECASE)

files = os.listdir(RAW_FOLDER)

# Detect highest existing number
for file in files:

    name, ext = os.path.splitext(file)

    if ext.lower() not in EXTENSIONS:
        continue

    match = pattern.match(name)

    if match:
        num = int(match.group(1))
        max_number = max(max_number, num)

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

    new_name = f"{PREFIX}{counter}{ext.lower()}"
    new_path = os.path.join(RAW_FOLDER, new_name)

    os.rename(path, new_path)

    print(f"{file} → {new_name}")

    counter += 1

print("Rename complete.")