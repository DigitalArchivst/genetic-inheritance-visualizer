# Running the Genetic Inheritance Visualizer in Google Colab

This guide will help you run this project in Google Colab, a free cloud-based Python environment that requires no setup.

## 🚀 Getting Started with Google Colab

1. Visit [Google Colab](https://colab.research.google.com)
2. Sign in with your Google account
3. Click `File` → `New Notebook` to create a new notebook

## 📥 Downloading the Script from GitHub

1. In your Colab notebook, add a new code cell by clicking the `+ Code` button
2. Copy and paste the following commands:

```python
# Clone the repository
!git clone https://github.com/DigitalArchivst/genetic-inheritance-visualizer.git
%cd genetic-inheritance-visualizer

# Install required packages
!pip install -r requirements.txt
```

3. Run the cell by clicking the play button ▶️ or pressing `Shift + Enter`

## 🎨 Running the Genetic Inheritance Visualizer

1. Create a new code cell and paste the following:

```python
# Import and run the script
with open('genetic-inheritance-complete-v21.py', 'r') as file:
    script_content = file.read()
    
# Save the script with a .py extension
with open('run_visualizer.py', 'w') as file:
    file.write(script_content)

# Run the script
!python run_visualizer.py
```

2. Run the cell to generate your genetic inheritance diagram

## 📊 Viewing the Generated SVG

1. The script will create an SVG file in your Colab workspace
2. To view it, create a new code cell with:

```python
# List the generated SVG file
!ls *svg

# Display the most recent SVG file
from IPython.display import SVG, display
import glob
latest_svg = max(glob.glob('*.svg'), key=os.path.getctime)
display(SVG(filename=latest_svg))
```

## 💡 Tips

- Colab sessions expire after a period of inactivity. Save your work using `File` → `Save a copy in Drive`
- To run the script again with different generations, just re-run the cell
- You can download the generated SVG files to your local machine using the file browser in the left sidebar

## 🤝 Contributing

Found a bug or want to contribute? Visit our [GitHub repository](https://github.com/DigitalArchivst/genetic-inheritance-visualizer) to:
- Open an issue
- Submit a pull request
- Fork the project

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Created by [DigitalArchivst](https://github.com/DigitalArchivst)*
