# Green Areas Detection Tool

This tool is part of the work presented in the conference paper:  
**"Methodology for Automatic Detection of Trees and Shrubs in Aerial Pictures from UAS"**  
[Read the paper on ResearchGate](https://www.researchgate.net/publication/288994191_Methodology_for_automatic_detection_of_trees_and_shrubs_in_aerial_pictures_from_UAS)

## Overview

This project provides tools for analyzing and segmenting green areas in aerial images using HSV color space. It consists of two main components:

1. **Hue Selection Tool** (`hSelection.py`): Analyzes Hue values in a selected region of interest (ROI)
2. **Color Segmentation Tool** (`colorSegmentation.py`): Segments images based on specified Hue ranges

## Installation

```bash
git clone https://github.com/yourusername/green_areas_detection.git
cd green_areas_detection
pip install -r requirements.txt
```

## Usage

### Hue Selection Tool

Analyzes Hue values in a region of interest and saves HSV channel visualizations.

```bash
python hSelection.py --input <image_path> \
                    --output-dir <output_directory> \
                    --roi <x1> <x2> <y1> <y2>
```

Options:
- `--input, -i`: Input image path (default: images/lena.png)
- `--output-dir, -o`: Output directory for saved images (default: images)
- `--roi`: Region of Interest coordinates [x1 x2 y1 y2] (default: 200 230 200 230)

### Color Segmentation Tool

Segments images based on specified Hue ranges in HSV color space.

```bash
python colorSegmentation.py --input <image_path> \
                          --output <output_path> \
                          --hue-range <min> <max>
```

Options:
- `--input, -i`: Input image path (default: images/lena.png)
- `--output, -o`: Output image path (default: images/result.png)
- `--hue-range`: Hue range [min max] (default: 133 168)

## Examples

```bash
# Analyze ROI in a custom image
python hSelection.py -i aerial_image.jpg --roi 100 200 100 200

# Segment green areas
python colorSegmentation.py -i aerial_image.jpg -o result.jpg --hue-range 60 120
```

## Requirements

- Python 3.6+
- Core dependencies:
  - OpenCV (opencv-python==4.11.0.86)
  - NumPy (numpy==2.2.3)
  - Matplotlib (matplotlib==3.10.0)

Full list of dependencies with versions:
```txt
contourpy==1.3.1
cycler==0.12.1
fonttools==4.56.0
kiwisolver==1.4.8
matplotlib==3.10.0
numpy==2.2.3
opencv-contrib-python==4.11.0.86
opencv-python==4.11.0.86
packaging==24.2
pillow==11.1.0
pyparsing==3.2.1
python-dateutil==2.9.0.post0
six==1.17.0
```

You can install all dependencies using:
```bash
pip install -r requirements.txt
```

## License

MIT License

## Citation

If you use this tool in your research, please cite:
```bibtex
@conference{paper_reference,
    title={Methodology for Automatic Detection of Trees and Shrubs in Aerial Pictures from UAS},
    author={MA Garduño-Ramón, JI Sánchez-Gómez, LA Morales Hernández, JP Benítez-Rangel, RA Osornio-Rios},
    year={2016}
}
```