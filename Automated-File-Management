import os
import shutil

# Set the folder to organize
folder_to_track = 'C:/Users/Preethi/Downloads'  # Change this to your target folder

# Define categories and their file types
file_categories = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif'],
    "Documents": ['.pdf', '.docx', '.doc', '.txt'],
    "Python_Files": ['.py'],
    "Spreadsheets": ['.xls', '.xlsx', '.csv'],
    "Compressed": ['.zip', '.rar'],
    "Others": []
}

# Make folders if not exist
for category in file_categories:
    folder_path = os.path.join(folder_to_track, category)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files
for filename in os.listdir(folder_to_track):
    file_path = os.path.join(folder_to_track, filename)
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(filename)
        moved = False
        for category, extensions in file_categories.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(folder_to_track, category, filename))
                print(f"Moved '{filename}' to {category}/")
                moved = True
                break
        if not moved:
            shutil.move(file_path, os.path.join(folder_to_track, "Others", filename))
            print(f"Moved '{filename}' to Others/")
