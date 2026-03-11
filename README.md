# web-photo-prep-tools
This repository contains simple Python scripts used to prepare photographs for a portfolio website. 
The tools can also be used more generally to rename image files into a consistent naming structure and to optimize photo sizes for different purposes. 

The scripts can batch rename photos, convert high-resolution images into optimized web images, and generate thumbnails so the website loads faster while maintaining good visual quality.

## Features

- Batch rename images sequentially
- Optimize images size for the web
- Generate thumbnails

## Requirements

- Python 3
- Pillow

Install Pillow:

```bash
pip install pillow
```

## Directory Structure

```
web-photo-prep-tools/
├── scripts/              # Python scripts for processing images
│   ├── rename.py         # Renames images sequentially
│   ├── optimize.py       # Creates optimized images for the website
│   └── thumbnails.py     # Generates thumbnail images
│
├── photos/               # Image directories used by the scripts
│   ├── raw/              # Original images
│   ├── optimize/         # Optimized web images
│   └── thumbs/           # Generated thumbnails
```