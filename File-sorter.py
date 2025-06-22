import os
import shutil

# Set your folder path
source_folder = r""  # ← Change this to your path

# File types and folders
file_types = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Music': ['.mp3', '.wav'],
}

# Dictionary to store file move counts
file_counts = {
    'Images': 0,
    'Videos': 0,
    'Documents': 0,
    'Music': 0,
    'Others': 0
}

print(f"\n📂 Sorting files in: {source_folder}\n")

# Create folders if not present
for folder in file_types:
    os.makedirs(os.path.join(source_folder, folder), exist_ok=True)
os.makedirs(os.path.join(source_folder, 'Others'), exist_ok=True)

# Loop through files
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(source_folder, folder, file))
                file_counts[folder] += 1
                print(f"✅ Moved: {file} → {folder}/")
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(source_folder, 'Others', file))
            file_counts['Others'] += 1
            print(f"📦 Moved: {file} → Others/")

# Summary
print("\n📊 Sorting Summary:")
for folder, count in file_counts.items():
    print(f"   {folder}: {count} files")
print("\n🎉 Sorting complete!\n")
