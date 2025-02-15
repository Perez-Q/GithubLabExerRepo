import tkinter as tk
from tkinter import filedialog
import os  # For extracting the file name from the path

# Initialize the Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open a file dialog to select a text file
file_path = filedialog.askopenfilename(
    title="Select a Text File",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
)

# Extract and print the file name if a file is selected
if file_path:
    file_name = os.path.basename(file_path)  # Get the file name from the full path
    print(f"Selected file name: {file_name}")
else:
    print("No file selected.")
