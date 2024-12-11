# Genetic Inheritance Visualizer

A Python-based visualization tool that demonstrates genetic inheritance patterns across multiple generations. The program creates SVG diagrams showing how genetic traits are passed down through families, using a grid-based representation for genetic information.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/DigitalArchivst/genetic-inheritance-visualizer.git
cd genetic-inheritance-visualizer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Features

- Visualizes 2-4 generations of genetic inheritance
- Uses an 8x8 grid to represent 64 pieces of genetic information for each individual
- Simulates inheritance through independent probability for each genetic position
- Generates clear, scalable SVG diagrams
- Supports multiple trait pairs with different colors

## Usage

Run the script and follow the prompts to specify the number of generations (2-4):

```bash
python genetic-inheritance-complete-v21.py
```

The program will generate an SVG file that can be viewed in any web browser.

## How It Works

Each person is represented by an 8x8 grid of cells, where each cell represents a piece of genetic information. When creating a child:
- For each of the 64 positions in the grid
- A coin is flipped to determine which parent contributes that piece
- The trait (color) is inherited from the chosen parent for that position

This simulates how genetic information is passed down through generations, with each piece of genetic information having an equal chance of coming from either parent.

## Author

DigitalArchivst

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
