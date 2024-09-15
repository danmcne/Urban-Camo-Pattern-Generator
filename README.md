# Urban Camo Pattern Generator

## Overview

`urban_camo_gen.py` is a Python script that generates unique camouflage patterns using geometric shapes. The patterns are inspired by urban camouflage designs, featuring various geometric shapes and colors. The script provides an interactive GUI for customizing pattern parameters and saving the generated designs.

## Features

- **Color Palettes**: Two color palettes are available for generating patterns:
  - **Muted Urban**: A set of urban-inspired muted colors (greys, blues, greens, beiges).
  - **Neon**: A vibrant neon color palette for a more striking appearance.
- **Customizable Parameters**: Control the seed, number of colors, number of loops, recursion depth, and line thickness.
- **Background Handling**: The generated images have a white background by default, making it easier to convert to transparent backgrounds in post-processing.

## Prerequisites

Ensure you have the following Python packages installed:
- `turtle`
- `tkinter` (included with standard Python distributions)
- `Pillow` (install via `pip install pillow`)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/urban_camo_gen.git
   ```

2. Navigate to the directory:
   ```bash
   cd urban_camo_gen
   ```

3. Install the required packages (if not already installed):
   ```bash
   pip install pillow
   ```

## Usage

1. Open a terminal and navigate to the script directory.
2. Run the script:
   ```bash
   python urban_camo_gen.py
   ```

3. The GUI will appear with options to configure:
   - **Seed**: Seed value for random number generation.
   - **Number of Colors**: Number of colors to use from the palette.
   - **Number of Loops**: Number of patterns to generate.
   - **Recursion Depth**: Depth of recursion for pattern complexity.
   - **Line Thickness**: Thickness of the lines drawn.

4. Use the buttons to:
   - **Draw Pattern**: Generate the camouflage pattern based on current settings.
   - **Save Pattern**: Save the generated pattern as a PNG file.
   - **Clear Pattern**: Clear the current pattern from the canvas.
   - **Exit**: Close the application.

## Color Palettes

To switch between color palettes, comment out the palette you do not wish to use and uncomment the desired one in the code:

```python
# Muted Urban Color Palette
COLOR_PALETTE = ['#708090', '#2f4f4f', '#d3d3d3', '#4682b4', '#778899', 
                 '#a9a9a9', '#696969', '#bdb76b', '#8b4513', '#556b2f']

# Neon Color Palette
# COLOR_PALETTE = ['#ff00ff', '#00ffff', '#ff4500', '#32cd32', '#ff1493', 
#                  '#00ff00', '#ff6347', '#8a2be2', '#ffb6c1', '#00fa9a']
```

## Background Handling

The generated images have a white background by default. This is intentional, as it simplifies converting the white background to transparent using image editing software.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue.
