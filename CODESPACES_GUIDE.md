# Running in GitHub Codespaces

GitHub Codespaces provides a complete, cloud-based development environment. Here's how to use it with the Genetic Inheritance Visualizer:

## 🚀 Starting a Codespace

1. Visit the [repository page](https://github.com/DigitalArchivst/genetic-inheritance-visualizer)
2. Click the green `Code` button
3. Select the `Codespaces` tab
4. Click `Create codespace on main`

## 💻 Running the Visualizer

Once your Codespace loads (it looks like VS Code in the browser):

1. Open a terminal (View → Terminal or `` Ctrl + ` ``)
2. Install requirements:
```bash
pip install -r requirements.txt
```
3. Run the script:
```bash
python genetic-inheritance-complete-v21.py
```

## 👀 Viewing Generated SVGs

1. The SVG file will appear in the file explorer (left sidebar)
2. Right-click the SVG file and select "Open Preview" to view it directly in Codespaces

## 💡 Tips

- Codespaces automatically saves your work
- You get 60 hours of free Codespaces usage per month
- You can connect your local VS Code to a Codespace
- The environment persists until you delete it

## ⚡ Advantages of Codespaces

- Full development environment in your browser
- All dependencies pre-installed
- Built-in version control
- No local setup required
- Consistent environment across devices

## 📝 Note

While both Colab and Codespaces work well, Colab is better for quick runs and visualization, while Codespaces provides a full development environment if you want to modify or contribute to the code.

---
*See also: [COLAB_GUIDE.md](COLAB_GUIDE.md) for running in Google Colab*
