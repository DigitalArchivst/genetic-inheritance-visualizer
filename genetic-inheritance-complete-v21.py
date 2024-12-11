"""
Genetic Inheritance SVG Generator

This script creates visual diagrams showing how genetic traits are passed down through families.
Each person is represented by a square block containing 64 smaller cells (in an 8x8 grid).
These cells represent genetic information - imagine each cell as a piece of DNA that can be passed down.

For Genealogists:
- Each block represents one person in a family tree
- The colored cells show different versions (alleles) of a genetic trait
- Children inherit exactly half their DNA from each parent (32 cells from each)
- This helps visualize concepts like genetic recombination and inheritance patterns

For Python Beginners:
- This script shows how to create graphics using Python code
- We'll use classes (like templates) to organize our code
- Comments marked with '#' explain what each part does
- Don't worry if you don't understand everything - focus on the basic concepts first!
"""

# Import required Python libraries
import random
import xml.etree.ElementTree as ET
from typing import List, Tuple, Dict, Optional, Union
from pathlib import Path
from datetime import datetime

# These are our "settings" - we can easily change these numbers to adjust our diagram
# In genetics terms, these control the size and layout of our family tree visualization
MIN_GENERATIONS = 2     # Minimum number of generations to show (like grandparents to grandchildren)
MAX_GENERATIONS = 4     # Maximum number of generations (like great-great-grandparents to children)
BLOCK_SIZE = 80        # How big each person's block will be (doubled from 40)
BLOCK_SPACING = 120    # Space between blocks (doubled to maintain proportions)
VERTICAL_SPACING = 220 # Space between generations (doubled to maintain proportions)
CELL_SIZE = 10        # Size of each DNA "piece" in the block
CELLS_PER_SIDE = 8    # Makes our 8x8 grid (increased from 4)
CELLS_FROM_EACH_PARENT = 32  # Each parent gives exactly half their DNA (32 of 64 cells)

class Block:
    """
    A Block represents one person in our family tree.
    
    Genetic Concept:
    - Each person has 64 "pieces" of genetic information (cells in an 8x8 grid)
    - These pieces could represent different versions of a trait (like eye color)
    - In real genetics, we inherit 50% from each parent - that's why we take 32 cells from each!
    
    Python Concept:
    - This is a 'class' - think of it as a template for creating person blocks
    - Each block we create is an 'instance' of this class
    - The class keeps track of which cells have which colors (representing genetic traits)
    """
    
    def __init__(self, cells: Optional[Dict[Tuple[int, int], str]] = None):
        """
        Create a new person block.
        
        Genetic Concept:
        - When we first create a person, they might start with no genetic information
        - Or they might be created with specific genetic traits (colors) already set
        
        Python Concept:
        - This is called a 'constructor' - it runs when we create a new Block
        - The 'Optional' means cells can be None (empty) or have values
        - Dict[Tuple[int, int], str] means we store colors (str) at grid positions (row, col)
        """
        self.cells: Dict[Tuple[int, int], str] = cells if cells else {}
    
    def set_solid_color(self, color: str) -> None:
        """
        Make all cells the same color (used for first generation).
        
        Genetic Concept:
        - Sometimes we want to start with a "pure" genetic trait
        - This is like having a parent with a completely dominant trait
        
        Python Concept:
        - This is a 'method' - a function that belongs to our Block class
        - We use a 'dictionary comprehension' to fill all cells with one color
        - The -> None means this function doesn't return anything
        """
        self.cells = {(row, col): color 
                     for row in range(CELLS_PER_SIDE) 
                     for col in range(CELLS_PER_SIDE)}
    
    def inherit_from_parents(self, parent1: 'Block', parent2: 'Block') -> None:
        """
        Create a child's genetic makeup from two parents.
        
        Genetic Concept:
        - For each position in the 8x8 grid, we flip a coin
        - If heads (True), take that position from parent1
        - If tails (False), take that position from parent2
        - This simulates how each piece of genetic information comes from one parent or the other
        
        Python Concept:
        - We iterate through all 64 positions in order
        - random.choice([True, False]) simulates a coin flip
        - We build the child's genetic makeup one position at a time
        """
        # Create the child's genetic makeup by flipping a coin for each position
        self.cells = {}
        for row in range(CELLS_PER_SIDE):
            for col in range(CELLS_PER_SIDE):
                pos = (row, col)
                # Flip a coin for each position
                take_from_parent1 = random.choice([True, False])
                # Take the gene from whichever parent won the coin flip
                self.cells[pos] = parent1.cells[pos] if take_from_parent1 else parent2.cells[pos]

class GeneticInheritanceSVG:
    """
    This class creates the visual family tree showing genetic inheritance.
    
    Genetic Concept:
    - Shows how genetic traits pass through 2-4 generations of a family
    - Uses different colors to represent different versions of traits
    - Connects parents to children with lines to show relationships
    - Labels each generation (Great-grandparents, Grandparents, etc.)
    
    Python Concept:
    - This is our main visualization class
    - Uses SVG (Scalable Vector Graphics) to create clear, resizable images
    - Manages the layout and connections between family members
    """
    
    def __init__(self, num_generations: int):
        """
        Set up a new family tree visualization.
        
        Genetic Concept:
        - We can show 2-4 generations of inheritance
        """
        if not MIN_GENERATIONS <= num_generations <= MAX_GENERATIONS:
            raise ValueError(f"Number of generations must be between {MIN_GENERATIONS} and {MAX_GENERATIONS}")
        
        self.num_generations = num_generations
        
        # Color pairs represent different versions of traits
        # Each pair could represent things like:
        # - Brown eyes (black) vs Blue eyes (white)
        # - Curly hair (red) vs Straight hair (green)
        self.colors = [
            ("black", "white"),
            ("#ff0000", "#008000"),  # red, green
            ("#0000ff", "#ffa500"),  # blue, orange
            ("#ffff00", "#800080")   # yellow, purple
        ]

    def create_grid_pattern(self) -> ET.Element:
        """
        Create the grid lines that divide each person's block into 64 cells.
        
        Genetic Concept:
        - The 8x8 grid shows 64 pieces of genetic information
        - This makes it easy to see how traits are inherited
        - Each cell could represent a different genetic marker
        
        Python Concept:
        - We use SVG 'pattern' elements to create reusable grid lines
        - The -> ET.Element tells Python this function returns an SVG element
        - We use f-strings (f'...') to insert numbers into our SVG paths
        """
        pattern = ET.Element('pattern', {
            'id': 'grid8x8',
            'width': str(BLOCK_SIZE),
            'height': str(BLOCK_SIZE),
            'patternUnits': 'userSpaceOnUse'
        })
        
        # Create the grid lines using SVG path commands
        # M = Move to, L = Line to
        path = ET.SubElement(pattern, 'path', {
            'd': f'M {CELL_SIZE},0 L {CELL_SIZE},{BLOCK_SIZE} '  # First vertical line
                 f'M {CELL_SIZE*2},0 L {CELL_SIZE*2},{BLOCK_SIZE} '  # Second vertical line
                 f'M {CELL_SIZE*3},0 L {CELL_SIZE*3},{BLOCK_SIZE} '  # Third vertical line
                 f'M {CELL_SIZE*4},0 L {CELL_SIZE*4},{BLOCK_SIZE} '  # Fourth vertical line
                 f'M {CELL_SIZE*5},0 L {CELL_SIZE*5},{BLOCK_SIZE} '  # Fifth vertical line
                 f'M {CELL_SIZE*6},0 L {CELL_SIZE*6},{BLOCK_SIZE} '  # Sixth vertical line
                 f'M {CELL_SIZE*7},0 L {CELL_SIZE*7},{BLOCK_SIZE} '  # Seventh vertical line
                 f'M 0,{CELL_SIZE} L {BLOCK_SIZE},{CELL_SIZE} '  # First horizontal line
                 f'M 0,{CELL_SIZE*2} L {BLOCK_SIZE},{CELL_SIZE*2} '  # Second horizontal line
                 f'M 0,{CELL_SIZE*3} L {BLOCK_SIZE},{CELL_SIZE*3} '  # Third horizontal line
                 f'M 0,{CELL_SIZE*4} L {BLOCK_SIZE},{CELL_SIZE*4} '  # Fourth horizontal line
                 f'M 0,{CELL_SIZE*5} L {BLOCK_SIZE},{CELL_SIZE*5} '  # Fifth horizontal line
                 f'M 0,{CELL_SIZE*6} L {BLOCK_SIZE},{CELL_SIZE*6} '  # Sixth horizontal line
                 f'M 0,{CELL_SIZE*7} L {BLOCK_SIZE},{CELL_SIZE*7}',  # Seventh horizontal line
            'fill': 'none',
            'stroke': 'black',
            'stroke-width': '1'
        })
        return pattern

    def create_block_svg(self, x: int, y: int, block: Block) -> ET.Element:
        """
        Create a visual representation of one person's genetic makeup.
        
        Genetic Concept:
        - Each block shows one person's genetic information
        - The colored cells show which traits they inherited
        - The grid makes it easy to count and compare traits
        
        Python Concept:
        - We create an SVG group ('g') to hold all parts of the block
        - We use loops to create all the cells and grid lines
        - The x,y coordinates position this person in the family tree
        """
        # Create a group to hold all parts of this person's block
        group = ET.Element('g', {'transform': f'translate({x},{y})'})
        
        # Create the white background rectangle
        ET.SubElement(group, 'rect', {
            'width': str(BLOCK_SIZE),
            'height': str(BLOCK_SIZE),
            'stroke': 'black',
            'stroke-width': '1',
            'fill': 'white'
        })
        
        # Draw each colored cell representing genetic traits
        for (row, col), color in block.cells.items():
            ET.SubElement(group, 'rect', {
                'x': str(col * CELL_SIZE),
                'y': str(row * CELL_SIZE),
                'width': str(CELL_SIZE),
                'height': str(CELL_SIZE),
                'fill': color
            })
        
        # Add the grid lines to separate cells
        for i in range(1, CELLS_PER_SIDE):
            # Create vertical lines
            ET.SubElement(group, 'line', {
                'x1': str(i * CELL_SIZE),
                'y1': '0',
                'x2': str(i * CELL_SIZE),
                'y2': str(BLOCK_SIZE),
                'stroke': 'black',
                'stroke-width': '1'
            })
            # Create horizontal lines
            ET.SubElement(group, 'line', {
                'x1': '0',
                'y1': str(i * CELL_SIZE),
                'x2': str(BLOCK_SIZE),
                'y2': str(i * CELL_SIZE),
                'stroke': 'black',
                'stroke-width': '1'
            })
        
        return group

    def create_connection(self, svg: ET.Element, parent1_x: int, parent2_x: int, 
                         parent_y: int, child_x: int, child_y: int) -> None:
        """
        Draw lines connecting parents to their child.
        
        Genetic Concept:
        - Lines show how genetic information flows from parents to children
        - The horizontal line connects the parents as a couple
        - The vertical line shows their child inheriting from both parents
        
        Python Concept:
        - We use SVG paths to draw the connecting lines
        - The lines are created using move (M) and line (L) commands
        - We calculate the center point between parents for the vertical line
        """
        # Draw horizontal line connecting the parents
        ET.SubElement(svg, 'path', {
            'd': f'M {parent1_x + BLOCK_SIZE},{parent_y + BLOCK_SIZE//2} '
                 f'L {parent2_x},{parent_y + BLOCK_SIZE//2}',
            'stroke': 'black',
            'stroke-width': '1'
        })
        
        # Draw vertical line down to the child
        center_x = (parent1_x + parent2_x + BLOCK_SIZE) // 2
        ET.SubElement(svg, 'path', {
            'd': f'M {center_x},{parent_y + BLOCK_SIZE//2} L {center_x},{child_y}',
            'stroke': 'black',
            'stroke-width': '1'
        })

    def generate_svg(self) -> str:
        """
        Create the complete family tree visualization.
        
        Genetic Concept:
        - This builds a full family tree showing inheritance patterns
        - Each generation inherits traits from the generation above
        - We can see how traits are passed down through up to 4 generations
        
        Python Concept:
        - This is our main drawing function that puts everything together
        - We use nested loops to create multiple generations
        - We keep track of positions to properly space and connect everyone
        
        Returns:
            A string containing the complete SVG image code
        """
        try:
            # Create the main SVG canvas
            svg = ET.Element('svg', {
                'xmlns': 'http://www.w3.org/2000/svg',
                'viewBox': f'-200 -50 1800 {300 * self.num_generations}'  # Wider and taller viewBox with more margins all around
            })
            
            # Add the grid pattern we'll use for all blocks
            defs = ET.SubElement(svg, 'defs')
            defs.append(self.create_grid_pattern())
            
            # Keep track of all blocks so we can connect them properly
            generation_blocks = []
            
            # Create the first generation (the oldest generation)
            first_gen = []
            num_pairs = 2 ** (self.num_generations - 2)  # Calculate how many pairs we need
            
            # Center the blocks horizontally with more space
            total_width = 1400  # Increased total width
            start_x = (total_width - (num_pairs * 2 * (BLOCK_SIZE + BLOCK_SPACING))) // 2
            
            # Create the first generation's blocks with solid colors
            for i in range(num_pairs * 2):
                x = start_x + i * (BLOCK_SIZE + BLOCK_SPACING)
                y = 50  # First generation y-position
                color = self.colors[i // 2][i % 2]  # Pick colors from our pairs
                
                block = Block()
                block.set_solid_color(color)
                
                svg.append(self.create_block_svg(x, y, block))
                first_gen.append((x, y, block))
            
            generation_blocks.append(first_gen)
            
            # Create each subsequent generation
            for gen in range(1, self.num_generations):
                current_gen = []
                y = 50 + gen * VERTICAL_SPACING  # Move down for each generation
                
                # Each generation has half as many people as the previous one
                num_blocks = 2 ** (self.num_generations - gen - 1)
                
                # Create children for each pair of parents
                for i in range(num_blocks):
                    parent_idx = i * 2
                    parent1_x, parent1_y, parent1_block = generation_blocks[gen-1][parent_idx]
                    parent2_x, parent2_y, parent2_block = generation_blocks[gen-1][parent_idx + 1]
                    
                    # Position child block between its parents
                    child_x = (parent1_x + parent2_x + BLOCK_SIZE) // 2 - BLOCK_SIZE // 2
                    
                    # Create child block and inherit traits from parents
                    child_block = Block()
                    child_block.inherit_from_parents(parent1_block, parent2_block)
                    
                    # Add child's block to the visualization
                    svg.append(self.create_block_svg(child_x, y, child_block))
                    current_gen.append((child_x, y, child_block))
                    
                    # Draw lines connecting child to parents
                    self.create_connection(svg, parent1_x, parent2_x, parent1_y, child_x, y)
                
                generation_blocks.append(current_gen)
            
            return ET.tostring(svg, encoding='unicode')
            
        except Exception as e:
            raise ValueError(f"Error generating SVG: {e}")

    def save_svg(self, filename: Union[str, Path]) -> None:
        """
        Save the family tree visualization as an SVG file.
        
        Genetic Concept:
        - This saves our inheritance diagram in SVG format
        - SVG files can be viewed in any web browser
        - The diagram will stay sharp and clear at any size
        """
        try:
            # Generate and save SVG
            svg_content = self.generate_svg()
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(svg_content)
            
        except OSError as e:
            raise OSError(f"Error saving file: {e}")

def main() -> None:
    """
    Run the Genetic Inheritance Visualization program.
    
    This is where our program starts! It:
    1. Asks how many generations you want to see (2-4)
    2. Creates and saves your family tree diagram as an SVG file
    """
    print("\nGenetic Inheritance Visualization Generator")
    print("==========================================")
    
    # Ask the user how many generations they want to see
    while True:
        try:
            num_generations = int(input(f"\nEnter number of generations ({MIN_GENERATIONS}-{MAX_GENERATIONS}): "))
            if MIN_GENERATIONS <= num_generations <= MAX_GENERATIONS:
                break
            print(f"Please enter a number between {MIN_GENERATIONS} and {MAX_GENERATIONS}.")
        except ValueError:
            print("Please enter a valid number.")
    
    try:
        # Create the family tree visualization
        generator = GeneticInheritanceSVG(num_generations)
        
        # Generate timestamp for unique filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = Path(f'genetic_inheritance_{num_generations}gen_{timestamp}.svg')
        
        # Save the SVG file
        generator.save_svg(output_file)
        
        print(f"\nYour {num_generations}-generation genetic inheritance diagram has been created!")
        print(f"File generated: {output_file}")
        print("\nThis diagram shows how genetic traits pass from generation to generation,")
        print("with each person inheriting half their traits from each parent.")
        print("\nYou can open this SVG file in any web browser to view it.")
        
    except (ValueError, OSError) as e:
        print(f"\nError: {e}")
        return

if __name__ == "__main__":
    main()
